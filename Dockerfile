FROM python:3.11.4-bullseye


ENV POETRY_HOME=/opt/poetry

RUN apt-get -y install curl
RUN curl -sSL https://install.python-poetry.org | python - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

WORKDIR /bot
RUN cd /bot
COPY . /bot/
RUN poetry install 

ENTRYPOINT ["sh", "-c", "python3 ./main.py"]