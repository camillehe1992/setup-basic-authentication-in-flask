# Setup Basic Authentication in Flask

The project demonstrates a Flask application with basic authentication implementation

## Setup Environment

### 1. Create a virtual environment for your project

```bash
# Check python version
python3 --version
# Python 3.11.6

# create a virtual environment named env
python3 -m venv env  

# Activate the created virtual environment
source env/bin/activate
```

### 2. Setup Environment Variable

```bash
# Create a `.env` file from `.env.template`, Update `REPLACE_ME` for local setup
cp .env.template .env

# Export variables in .env to environment variables
source .env

# Install dependencies
pip install -r requirements.txt
```

## Start Server

```bash
flask run
```

The local server is running on <http://127.0.0.1:5000>.

## Database Migration

**Flask-Migrate** is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. In the project, we leverage it to sync the models' change with database.

Find more information from <https://flask-migrate.readthedocs.io/en/latest/>

```bash
# Initiate a migration folder using init command for alembic to perform the migrations.
# The contents of this folder need to be added to version control along with your other source files.
flask db init

# Create a migration script from the detected changes in the model using the migrate command
# This doesn’t affect the database yet
flask db migrate -m "Initial migration"

# Apply the migration script to the database by using the upgrade command
flask db upgrade
```

> Each time the database model changes, repeat the migrate and upgrade commands.
>
> The migration script needs to be reviewed and edited, as Alembic is not always able to detect every change you make to your models. In particular, Alembic is currently unable to detect table name changes, column name changes, or anonymously named constraints.

To see all the commands that are available run this command:

```bash
flask db --help
```

## Testing

Run below command to execute unit test cases.

```bash
python app.py test
```
