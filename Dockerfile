FROM python:3.11-slim

COPY requirements.txt /usr/app/
RUN pip install --upgrade pip \
    && pip install -r /usr/app/requirements.txt
RUN mkdir /var/log/bots

WORKDIR /usr/app
