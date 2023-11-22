@echo off
cd newspost\aaa\aaa\simpleui_demo-master
start cmd /k "python manage.py runserver"
start "" "http://127.0.0.1:8000"