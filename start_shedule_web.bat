@echo off
cd /d "%~dp0"
set FLASK_APP=run.py
set FLASK_ENV=development
flask run
pause
