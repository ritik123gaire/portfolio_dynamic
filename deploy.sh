#!/bin/bash

# Pull the latest code
git pull origin main  # Adjust if your branch is different

# Build the containers
docker-compose -f docker-compose.prod.yml up --build -d

# Restart the services
docker-compose -f docker-compose.prod.yml restart