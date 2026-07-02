#!/bin/bash
# EC2 user-data starter script for Amazon Linux.
# Use this when launching EC2 if you want Docker installed automatically.
# Still check logs after boot: /var/log/cloud-init-output.log

dnf update -y
dnf install -y docker git
systemctl enable docker
systemctl start docker
usermod -aG docker ec2-user

# Optional simple test container:
# docker run -d --name test-nginx -p 80:80 nginx
