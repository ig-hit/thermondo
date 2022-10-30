#!/bin/sh

set -e

# copy default env vars
if [ ! -f .env ]; then
    cp .env.dist .env || true
fi
export $(grep -v '^#' .env | xargs -d '\n')

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

python_version=$(grep "FROM python:" < Dockerfile | cut -d : -f2)
pyenv install ${python_version} || true
virtualenv -p /home/${USER}/.pyenv/versions/${python_version}/bin/python3 .venv

. .venv/bin/activate

pip3 install --upgrade pip
pip3 install 'poetry==1.2.1'
poetry config virtualenvs.create false
poetry install

docker-compose up -d
sleep 10

./manage.py migrate
./manage.py setup

# show result
if [ $? -eq 0 ]; then
    echo ""
    echo "Successfully installed!"
    echo "source .venv/bin/activate"
    echo ""
else
    echo ""
    echo "Something went wrong. Fix the errors and try again."
    echo ""
fi
