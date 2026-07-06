#!/bin/bash
set -e

# RDS PostgreSQL values
DB_HOST="REPLACE_WITH_RDS_ENDPOINT"
DB_PORT="5432"
DB_NAME="helpdesk"
DB_USER="postgres"
DB_PASSWORD="REPLACE_WITH_PASSWORD"

# S3 values from v2
S3_BUCKET_NAME="cloudops-helpdesk-uploads-912392206132-us-east-1-an"
AWS_REGION="us-east-1"

sudo docker rm -f helpdesk-api || true

sudo docker build -t cloudops-helpdesk-api:v3 .

sudo docker run -d \
  --name helpdesk-api \
  -p 80:8000 \
  -e DB_HOST="$DB_HOST" \
  -e DB_PORT="$DB_PORT" \
  -e DB_NAME="$DB_NAME" \
  -e DB_USER="$DB_USER" \
  -e DB_PASSWORD="$DB_PASSWORD" \
  -e S3_BUCKET_NAME="$S3_BUCKET_NAME" \
  -e AWS_REGION="$AWS_REGION" \
  cloudops-helpdesk-api:v3

curl http://localhost/health