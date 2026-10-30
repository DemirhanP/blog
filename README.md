A website for logging blogs 


setup:

I will move the project to docker to avoid database issues 

at first it the database might rejects you by saying role $USER does not exists to fix that after you set it up run this command 

sudo -u postgres createuser --createdb "$USER"
createdb blog
psql blog -f schema.sql
psql blog -f data.sql


[I used ai to specify how it should be setup with the database as I have not ported a database to git ever]


1. Install PostgreSQL and make sure it is running.
2. Create the database, tables and data:
   ```
   createdb blog
   psql blog -f schema.sql
   psql blog -f data.sql
   ```
3. Create a virtual environment and install the dependencies:
   ```
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. Start the server:
   ```
   flask --app app run --debug
   ```
5. Open http://127.0.0.1:5000

To start over with a fresh copy of the data, run `dropdb blog` and repeat step 2.

## Accounts

`data.sql` is a snapshot of the database, so these accounts already exist after setup.

| Username          | Password          | Can write posts |
|-------------------|-------------------|-----------------|
| `WRITER_USERNAME` | `WRITER_PASSWORD` | yes             |
| `READER_USERNAME` | `READER_PASSWORD` | no              |

The database contains password hashes, not passwords. These two passwords are throwaway ones used only for this project.

## Configuration

Both variables are optional.

| Variable       | Default           | Purpose                       |
|----------------|-------------------|-------------------------------|
| `SECRET_KEY`   | a development key | Signs the session cookie      |
| `DATABASE_URL` | `dbname=blog`     | PostgreSQL connection string  |


## Allowing an account to write posts

Register an account on the site, then run:

```
psql blog -c "UPDATE users SET is_writer = TRUE WHERE username = 'yourname';"
```

Log out and back in for the change to take effect.
