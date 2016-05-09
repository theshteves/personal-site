all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

#
# ++++++++++++++++++++++++++++++++++++++
# +++                                +++
# ++  Steven Kneiser's Personal Site  ++
# +++                                +++
# ++++++++++++++++++++++++++++++++++++++
#
# TARGETS:
#	+ clean - remove all .pyc's
clean:
	find . -name '*.pyc' -delete

#	+ help - display all targets
help:
	@egrep "^#" [Mm]akefile

#	+ migrate - update database schema
migrate:
	python manage.py migrate

#	+ rebuild - rebuild server
rebuild: update migrate test
	python manage.py runserver

#	+ run - run server
run: migrate
	python manage.py runserver

#	+ test - run tests
test:
	python manage.py test

#	+ update - install/update all packages
update:
	pip install -U pip
	pip install -U -r requirements.txt

#
