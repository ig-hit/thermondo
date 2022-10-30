.PHONY: build start test

build:
	docker-compose build

start:
	docker-compose up

stop:
	docker-compose stop

test:
	docker-compose run --rm app sh -c "python manage.py test && make ci"

install:
	@./.bin/install.sh

mypy:
	@mypy .

black:
	@black --check .

lint:
	@flake8 .

ci: mypy black lint
