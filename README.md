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

# Install dependencies
pip install -r requirements.txt
```

## Start Server

```bash
python manage.py run
```
