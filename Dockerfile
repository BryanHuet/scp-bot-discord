FROM python:3.11-slim

WORKDIR /usr/bot
COPY . /usr/bot/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

RUN mkdir /var/log/bots

CMD ["python", "src/bot.py"]

