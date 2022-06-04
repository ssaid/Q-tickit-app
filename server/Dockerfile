FROM python:3.8-slim-buster

WORKDIR /server

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat libpq-dev gcc postgresql \
  && apt-get clean \
  && pip install psycopg2

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /server/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /server


