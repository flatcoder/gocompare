# GoCompare Supermarket Checkout

## Discussion

From the brief:

	"item ‘A’ might cost 50 pounds individually, but this week we have a special offer: buy three ‘A’s and they’ll cost you 130"
	"Our checkout accepts items in any order, so that if we scan a B, an A, and another B, we’ll recognize the two B’s and price them at..."

Are offers once per basket or unlimited?, i.e., if you have 7 "A"s in total it can be:

	a) 2 x offer, 1x full price
	b) 1 x offer, 4x full price

Simiarly, there could be multiple offers for the same product:

	- 2xA or 8xA or 50xA price break points
		- e.g., 3 for £5 or 6 for £8

Or offers spanning products:

	- 2xA and 1xB
		- e.g., a Tesco Meal Deal!

Current solution:

	- offers repeat
	- one offer per product
	- offers do not span products

## Installation

Note in `manager.py` the environment is set to "test" as there is no UI, only testing.  You can adjust `app/config.py` to suit (note it supports dev, test and production).  Then:

## Developer Installation - Python virtual environment

	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	python manage.py database init
	python manage.py database migrate
	python manage.py database upgrade
	python manage.py seed_database

## Usage and Test Execution

With everything ready, we can run the automated tests:

	python manage.py run_tests

Coverage is included in the installation. To assess the test code coverage, you can:

	coverage run --source='.' manage.py run_tests
	# The greps just remove the venv files and ergo incorrect totals, run without if you wish :)
	coverage report | grep -v "venv" | grep -v "TOTAL"

In reality, we would use a tool like Travis CI to run the tests automatically on a git (or similar) commit. A UI will be needed eventually as will a "real" web server.  For development, we can use:

	python manage.py runserver

You can also pass `-h 0.0.0.0` (host) and `-p 5000` (port) options to the runserver command.  Again, there is no UI presently, just a default route and placeholder. With the server running, visit the following URL in your browser:

	http://127.0.0.1:5000/

## Real World Install - using Docker

	docker-compose up --build

When done, remember to `docker-compose down` or expect it to magically re-appear on reboot!  The docker container will automatically create/seed the database using the `docker_launcher.sh` script which you can edit to suit.  It will then run tests, before finally launching a web server (no UI presently, placeholder).

In other words, the Docker version warrants a big "TL;DR" over the "Usage and Test Execution" section earlier!

## Technologies Used

- Python 3
- Flask, Flask Script, Flask Migrate
- SQLite **
- Docker
- SQLAlchemy

** For actual production, a real database. We're using sqlite here because it's easy to give you a ZIP that'll work out the box! Flask ought to be database agnostic, and it is, to a point.  Until you try a decimal with SQLite....

	Warning: "Dialect sqlite+pysqlite does *not* support Decimal objects natively".

...it will cast, but that's just asking for trouble with precision and rounding.  For now, in this exercise, we use Float for money, not Decimal.

## Closing Notes

- Depending on requirements, Django may be a better fit than Flask, it depends on the bigger picture, really.
- Currently assuming "no auth" but you'll see the hooks are included ready to add users.
- Be useful to add automated documentation (Pydoc or similar)?
