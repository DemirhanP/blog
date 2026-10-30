A website for logging blogs 


setup:

## Setup (Docker)

Requires Docker with Compose.

```
docker compose up --build
```

Then open http://localhost:5000

The database is created automatically from `schema.sql` and `data.sql`.
To reset it to that state: `docker compose down -v`, then run the command above again.

To let an account write posts:

```
docker compose exec db psql -U blog -d blog -c "UPDATE users SET is_writer = TRUE WHERE username = 'yourname';"
```

Log out and back in for the change to take effect.
