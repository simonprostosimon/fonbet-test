FROM ubuntu:16.04

RUN apt-get update
RUN apt-get dist-upgrade -y

RUN apt-get -y upgrade

RUN apt-get -y install python3.5
RUN apt-get -y install python3.5-dev
RUN apt-get -y install python3-pip
RUN apt-get -y install mongodb-server

RUN mkdir -p /data/db

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
CMD mongod --fork --logpath mongo.log & uwsgi -w app:app --socket 0.0.0.0:80 --protocol http