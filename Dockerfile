FROM python:3.11-slim

RUN apt-get update \
    && apt-get install -y \
        build-essential \
        libxml2-dev \
        libxslt-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /usr/app/
RUN pip install --upgrade pip \
    && pip install -r /usr/app/requirements.txt
RUN mkdir /var/log/bots

WORKDIR /usr/app
