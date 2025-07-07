#!/bin/bash

# Step 1: Kill existing tmux sessions
tmux list-sessions -F '#S' 2>/dev/null | xargs -I {} tmux kill-session -t {}

# Step 2: Go to your project directory
cd ~/portfolio || exit

# Step 3: Pull the latest code
git fetch
git reset origin/main --hard

# Step 4: Activate virtual environment and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Step 5: Start Flask server in new detached tmux session
tmux new-session -d -s flaskapp "cd ~/portfolio && source python3-virtualenv/bin/activate && flask run --host=0.0.0.0"
