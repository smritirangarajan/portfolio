#!/bin/bash

# Navigate to your project directory
cd ~/your-project-folder-name || exit

# Pull latest changes from GitHub main branch
git fetch && git reset origin/main --hard

# Stop and remove old containers
docker compose -f docker-compose.prod.yml down

# Rebuild and start new containers
docker compose -f docker-compose.prod.yml up -d --build

