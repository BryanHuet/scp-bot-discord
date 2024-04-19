#!/bin/bash
mkdir -p logs
pip install --upgrade pip
pip install -r requirements.txt
python -m unittest tests/operators_test.py
echo 'start scp-bot'
python src/bot.py