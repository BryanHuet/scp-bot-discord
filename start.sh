#!/bin/bash
pip install --upgrade pip
pip install -r requirements.txt
echo 'start scp-bot'
python src/bot.py