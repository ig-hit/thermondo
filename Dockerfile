FROM python:3.10.4

WORKDIR /usr/src/app

RUN useradd app
RUN chown -R app:app /usr/src/app

COPY --chown=app:app . .

RUN pip install --upgrade pip
RUN pip install 'poetry==1.2.1'
RUN poetry config virtualenvs.create false
RUN poetry install

USER app
