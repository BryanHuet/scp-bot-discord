#!/bin/bash
pip install --upgrade pip
pip install -r requirements.txt
python -m unittest bot/tests/operators_test.py
echo 'start scp-bot'
python bot/src/bot.py