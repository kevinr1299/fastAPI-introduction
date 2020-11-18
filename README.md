# Grader

## First time setup

To install the project do the following steps:

1. Install the project dependencies with `pipenv install --dev`
1. Copy `.env.example` to `.env`
1. Create the docker containers with `docker-compose build`
1. Create the database for the first time with `docker-compose up db`
1. Run the whole project again with `docker-compose up`, migrations and seeding will be run when staring up the project

## Other commands

* To apply migrations run `docker-compose run web alembic upgrade head`
