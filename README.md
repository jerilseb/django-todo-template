# Todo App with Google Sign-In

A simple and elegant Todo application built with Django, featuring Google Sign-In authentication.

## Features

- Google Sign-In authentication (no username/password required)
- Create, update, and delete todos
- Mark todos as completed
- Clean and responsive UI with Tailwind CSS

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd todo-app
```

2. Create a virtual environment and activate it:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create the site object:
```bash
python manage.py shell -c "from django.contrib.sites.models import Site; Site.objects.update_or_create(id=1, defaults={'domain': 'localhost:8000', 'name': 'localhost'})"
```

6. Set up Google OAuth credentials:
   - Follow the instructions in [Google OAuth Setup](docs/google_oauth_setup.md)
   - Update the `SOCIALACCOUNT_PROVIDERS` setting in `core/settings.py` with your credentials

7. Run the development server:
```bash
python manage.py runserver
```

8. Visit http://localhost:8000 in your browser and sign in with Google!

## Environment Variables

Create a `.env` file in the root directory with the following variables:
```
SECRET_KEY=your-secret-key
REDIS_HOST=localhost
REDIS_PORT=6379
LAB_TOKEN=your-lab-token
```

## Project Structure

- `core/` - Main Django project settings
- `todos/` - Todo application
- `templates/` - HTML templates
- `static/` - Static files (CSS, JS)
- `docs/` - Documentation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.