# Interview Recap

## Project pitch

I built a small CloudOps Helpdesk API to recap AWS cloud engineering basics. I containerised a FastAPI backend with Docker and deployed it on an AWS EC2 instance. I configured security groups for HTTP and SSH, checked CloudWatch metrics, and documented setup and cleanup steps.

## Skills shown

- EC2: cloud virtual machine
- Security groups: cloud firewall rules
- Docker: containerised deployment
- CloudWatch: monitoring and metrics
- IAM/MFA: account security basics
- Budget alerts: cost control
- Documentation: repeatable setup and cleanup

## Common troubleshooting points

- App not reachable: check security group, port mapping, Docker container status, app host binding.
- SSH not working: check key pair, security group source IP, instance state.
- Container exits: check `docker logs`.
- Browser cannot load app: check `curl localhost` inside EC2 first, then public IP.
