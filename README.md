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
