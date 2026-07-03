#!/bin/bash
tmux kill-server

cd ~/MLH-portfoilo

git fetch && git reset origin/main --hard

source venv/bin/activate
pip install -r requirements.txt

tmux new-session -d -s flask 'cd ~/MLH-portfoilo && source venv/bin/activate && flask run --host=0.0.0.0'
