#!/bin/bash
python manage.py database init || true
python manage.py database migrate 
python manage.py database upgrade
python manage.py seed_database 
python manage.py run_tests
python manage.py runserver -h 0.0.0.0 -p 5000
