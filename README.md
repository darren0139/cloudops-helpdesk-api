# CloudOps Helpdesk API

A beginner AWS Cloud Engineer practice project.

## What this project teaches

- FastAPI backend basics
- Docker image and container
- EC2 deployment
- Security groups
- CloudWatch metrics
- Cost-aware cleanup
- Basic AI-style ticket classification without paid API calls

## Local setup

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### WSL / Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000/docs
http://localhost:8000/health
```

## Run with Docker

```bash
docker build -t cloudops-helpdesk-api:v1 .
docker run -d --name helpdesk-api -p 8000:8000 cloudops-helpdesk-api:v1
docker ps
```

Open:

```text
http://localhost:8000/docs
```

Stop:

```bash
docker stop helpdesk-api
docker rm helpdesk-api
```

## Example API calls

Create a ticket:

```bash
curl -X POST http://localhost:8000/tickets/ \
  -H "Content-Type: application/json" \
  -d '{"title":"VPN cannot connect","description":"User cannot connect to VPN from home","category":"network","priority":"high"}'
```

List tickets:

```bash
curl http://localhost:8000/tickets/
```

Classify a ticket:

```bash
curl -X POST http://localhost:8000/tickets/classify \
  -H "Content-Type: application/json" \
  -d '{"title":"AWS EC2 down","description":"The web server on EC2 is not responding"}'
```

## AWS deployment goal

Deploy this Docker container on EC2 and expose it through port 80.

See:

```text
docs/aws-steps.md
scripts/ec2_user_data_install_docker.sh
scripts/ec2_run_app_commands.sh
```

## Cost warning

Terminate EC2 and remove unused AWS resources after testing.


# v2: S3 Ticket Attachments

Goal:

Add file uploads to your existing FastAPI Helpdesk API. Ticket text stays in SQLite.
Uploaded files/screenshots go to a private S3 bucket.

Architecture:

```text
Browser -> EC2 Docker FastAPI
              |-> SQLite: ticket records
              |-> S3: uploaded files
```

AWS setup:

1. Create S3 bucket, e.g. `cloudops-helpdesk-uploads-<your-name>`.
2. Keep Block Public Access ON.
3. Create IAM role for EC2.
4. Attach the policy in `iam_policy_s3_uploads.json` after replacing the bucket name.
5. Attach the IAM role to your EC2 instance.
6. Add the Python files from this folder to your project.
7. Update requirements.txt.
8. Update app/main.py to include attachments router.
9. Rebuild Docker image and run with S3 environment variables.
