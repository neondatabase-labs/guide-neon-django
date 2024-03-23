# Running migrations in a Neon-Django project

This application is a simple python API using the Django framework and Neon Postgres database. It returns a list of authors and books written by them. We illustrate how to generate and run schema change migrations.

To build this project from scratch, check out the [guide in Neon's documentation](https://neon.tech/docs/guides/django-migrations).

## Set up locally

You will need the following:

- A [Neon](https://neon.tech) account and a project
- Python 3.8 or higher

1. Clone this repository:

```bash
git clone https://github.com/neondatabase/guide-neon-django
```

2. Navigate to the project directory and create a new virtual environment:

```bash
cd guide-neon-django
python -m venv myenv
```

3. Activate the virtual environment and install the project dependencies:

```bash
source myenv/bin/activate
pip install -r requirements.txt
```

4. Create a `.env` file in the root of the project and add the following environment variable with your Neon database URL:

```bash
DATABASE_URL=
```

5. Run the Django migrations:

```bash
python manage.py migrate
```

6. Start the Django development server:

```bash
python manage.py runserver
```

7. Visit `http://localhost:8000` in your browser to see the list of authors and books. Or use curl to access the api from the terminal.

```bash
# Get the list of authors
curl http://localhost:8000/catalog/authors

# Get books by author with id 1
curl http://localhost:8000/catalog/books/1
```
