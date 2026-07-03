#!/bin/bash
set -e

# Replace this bucket name.
S3_BUCKET_NAME="REPLACE_WITH_YOUR_BUCKET_NAME"
AWS_REGION="us-east-1"

mkdir -p data
sudo docker rm -f helpdesk-api || true
sudo docker build -t cloudops-helpdesk-api:v2 .
sudo docker run -d   --name helpdesk-api   -p 80:8000   -v "$(pwd)/data:/app/data"   -e S3_BUCKET_NAME="$S3_BUCKET_NAME"   -e AWS_REGION="$AWS_REGION"   cloudops-helpdesk-api:v2

sudo docker ps
curl http://localhost/health
