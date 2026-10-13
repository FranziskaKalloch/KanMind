# KanMind

KanMind is a REST API backend for an Kanban task management application. Built with Django and Django REST Framework, it suppurts user registration and login, boards, tasks, and tasks comments.

Access to boards and tasks is controlled through authentication and permissions.

## Features

- User registration and token-based authentication
- Board creation and management
- Task creation, updates, and deletion
- Task assignment and review responsibilities
- Task comments with deletion restricted to their authors

## Prerequisites

- Python 3
- pip
- A local copy of this repository

Run the following commands from the project directory containing
`manage.py`.

Windows instructions below use PowerShell.

## Installation

### 1. Create a virtual environment

macOS

```bash
python3 -m venv .venv
```

Windows

```powershell
py -m venv .venv
```

### 2. Activate the virtual environment

macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, allow it for the current terminal
session and activate the environment again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

macOS and Windows

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example environment file.

macOS

```bash
cp .env.example .env
```

Windows

```powershell
Copy-Item .env.example .env
```

Open `.env` and configure the variables listed in `.env.example`.

| Variable | Description |
| --- | --- |
| `SECRET_KEY` | A secret key for the Django application. |

Keep your `.env` file private and exclude it from version control.

### 5. Apply database migrations

macOS and Windows

```bash
python manage.py migrate
```

### 6. Start the development server

macOS and Windows

```bash
python manage.py runserver
```

The development server runs at:

```http://127.0.0.1:8000/

API endpoints are available under `/api/`.

## Authentication

After registration or login, the API returns an authentication token.
Include it in the `Authorization` header when calling protected endpoints:

```text
Authorization: Token <your-token>
```

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite

## Stop the Server

Press `Ctrl+C` in the terminal.

To deactivate the virtual environment, run:

```bash
deactivate
```
