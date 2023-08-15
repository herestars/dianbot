FROM python:3.11.4-bullseye


ENV POETRY_HOME=/opt/poetry

RUN apt-get -y install curl
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

