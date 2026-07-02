# AWS Steps to Remember

Memory line:

> Root protects. IAM practises. EC2 runs. Security group opens. Docker deploys. CloudWatch watches. Terminate saves money.

## 0. Safety first

1. Enable MFA for root.
2. Create IAM admin user.
3. Enable MFA for IAM admin user.
4. Create AWS Budget alerts.
5. Use IAM admin for daily practice, not root.

## 1. Launch EC2

1. Go to EC2.
2. Click Launch instance.
3. Name: `cloudops-helpdesk-api`.
4. Choose Amazon Linux or Ubuntu.
5. Choose free/small instance type where available.
6. Create/select key pair.
7. Security group:
   - SSH 22: your IP only.
   - HTTP 80: anywhere for testing.
   - Avoid opening all ports.
8. Optional: paste `scripts/ec2_user_data_install_docker.sh` into User data.
9. Launch.

## 2. Connect

Use EC2 Instance Connect, or SSH from your terminal.

## 3. Deploy app

1. Install Docker if not already installed.
2. Clone your repo.
3. Build Docker image.
4. Run Docker container.
5. Visit `http://<EC2_PUBLIC_IP>/health`.

## 4. Monitor

1. Go to CloudWatch.
2. Check EC2 CPU, network in/out, status checks.
3. Optional: create a CPU alarm.

## 5. Cleanup

1. Stop/remove Docker container.
2. Terminate EC2 instance when done.
3. Check for leftover EBS volumes, Elastic IPs, RDS, load balancers, NAT gateways.
4. Check Billing dashboard/Budgets.
