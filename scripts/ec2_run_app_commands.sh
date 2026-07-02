#!/bin/bash
# Run these manually after SSH/EC2 Instance Connect into your EC2 instance.
# Assumes Docker is installed.

git clone <YOUR_GITHUB_REPO_URL>
cd cloudops-helpdesk-api

docker build -t cloudops-helpdesk-api:v1 .
docker run -d --name helpdesk-api -p 80:8000 cloudops-helpdesk-api:v1

docker ps
curl http://localhost/health
