# KanMind

Description for the project. KanMind is a backend project... etc.

## How to install

Step 1: Create a virtuel environment

Unix
'''bash
python3 -m venv .venv
'''

Windows
'''bash

'''

Step 2: Activate virtuell environment

Unix
'''bash
source .venv/bin/activate
'''

Windows
'''bash

'''

Step 3: Install the requirements

'''bash
pip install -r requirements
'''

Step 4: Create your .env file

Unix
'''bash
cp .env.example .env
'''

Windows
'''bash

'''

Then set your values:

Key | Value
SECRET_KEY | Value

Step 5: Migrate the migrations

'''bash
python manage.py migrate
'''

Step 6: Start the server

'''bash
python manage.py runserver
'''

## Tech stack

- python
- django
- drf
- squlite

## Routes

## Aufteilung und Aufgaben

user_app -> Registrierung, Login und E-Mail-Check
boards_app -> Boards erstellen, anzeigen, ändern und löschen; Eigentümer und Mitglieder verwalten
tasks_app -> Aufgaben erstellen, ändern und löschen; eigene zugewiesene Aufgaben und eigene Review-Aufgaben abrufen
comments_app -> Kommentare einer Aufgabe anzeigen, erstellen und löschen

## Beziehungen

Ein Board hat einen Owner und Mitglieder.
Eine Aufgabe gehört zu einem Board und kann einen Bearbeiter sowie einen Reviewer haben.
Ein Kommentar gehört zu einer Aufgabe und hat einen Autor.
