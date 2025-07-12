#!/bin/bash

# Step 1: Go to project folder
cd ~/portfolio || exit

# Step 2: Pull latest code from GitHub
git fetch && git reset origin/main --hard

# Step 3: Activate virtual environment and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Step 4: Restart systemd service
sudo systemctl restart myportfolio
