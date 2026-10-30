import os
from functools import wraps

import psycopg
from flask import (Flask, abort, redirect, render_template, request,
                   session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from db import get_conn

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-key-change-me")


def writer_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        if not session.get("is_writer"):
            abort(403)
        return view(*args, **kwargs)
    return wrapped


@app.route("/")
def index():
    with get_conn() as conn:
        posts = conn.execute(
            "SELECT posts.id, posts.title, posts.created_at, users.username "
            "FROM posts JOIN users ON users.id = posts.author_id "
            "ORDER BY posts.created_at DESC"
        ).fetchall()
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        if not username or not password:
            error = "Fill in both fields."
        else:
            try:
                with get_conn() as conn:
                    conn.execute(
                        "INSERT INTO users (username, password_hash) "
                        "VALUES (%s, %s)",
                        (username, generate_password_hash(password)),
                    )
                return redirect(url_for("login"))
            except psycopg.errors.UniqueViolation:
                error = "Username taken."

    return render_template("register.html", error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        with get_conn() as conn:
            user = conn.execute(
                "SELECT id, username, password_hash, is_writer "
                "FROM users WHERE username = %s",
                (username,),
            ).fetchone()

        if user and check_password_hash(user["password_hash"], password):
            session.clear()
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            session["is_writer"] = user["is_writer"]
            return redirect(url_for("index"))

        error = "Invalid username or password."

    return render_template("login.html", error=error)


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/post/<int:post_id>")
def show_post(post_id):
    with get_conn() as conn:
        post = conn.execute(
            "SELECT posts.id, posts.title, posts.body, posts.created_at, "
            "posts.author_id, users.username "
            "FROM posts JOIN users ON users.id = posts.author_id "
            "WHERE posts.id = %s",
            (post_id,),
        ).fetchone()

    if post is None:
        abort(404)

    return render_template("post.html", post=post)


@app.route("/new", methods=["GET", "POST"])
@writer_required
def new_post():
    if request.method == "POST":
        with get_conn() as conn:
            row = conn.execute(
                "INSERT INTO posts (title, body, author_id) "
                "VALUES (%s, %s, %s) RETURNING id",
                (request.form["title"], request.form["body"],
                 session["user_id"]),
            ).fetchone()
        return redirect(url_for("show_post", post_id=row["id"]))

    return render_template("form.html", post={"title": "", "body": ""})


@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
@writer_required
def edit_post(post_id):
    with get_conn() as conn:
        post = conn.execute(
            "SELECT id, title, body FROM posts "
            "WHERE id = %s AND author_id = %s",
            (post_id, session["user_id"]),
        ).fetchone()

        if post is None:
            abort(404)

        if request.method == "POST":
            conn.execute(
                "UPDATE posts SET title = %s, body = %s WHERE id = %s",
                (request.form["title"], request.form["body"], post_id),
            )
            return redirect(url_for("show_post", post_id=post_id))

    return render_template("form.html", post=post)