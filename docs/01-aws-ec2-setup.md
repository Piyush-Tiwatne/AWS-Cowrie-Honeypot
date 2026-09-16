# AWS EC2 Setup

## 1. Objective

The first step of the project was to deploy an Ubuntu Linux server on AWS EC2 to host the Cowrie SSH honeypot.

The EC2 instance provided the cloud-based environment required to run Cowrie and collect unsolicited SSH activity.

---

## 2. EC2 Configuration

The project used the following AWS and Linux components:

* AWS EC2
* Ubuntu Linux
* AWS Security Groups
* SSH
* EC2 key pair authentication

The EC2 instance was deployed in the **AWS Mumbai Region**.

---

## 3. Security Group Configuration

The EC2 Security Group was configured to control inbound network traffic to the instance.

The primary inbound rules were:

| Protocol | Port | Purpose                   |
| -------- | ---: | ------------------------- |
| TCP      |   22 | Administrative SSH access |
| TCP      | 2222 | Cowrie SSH honeypot       |

**Port 22** was used for administrative SSH access to the Ubuntu server.

**Port 2222** was configured for Cowrie to receive SSH connections directed toward the honeypot.

---

## 4. Port Separation

The administrative SSH service and the Cowrie honeypot were kept on separate ports.

```text
Port 22
   ↓
Real SSH Service
   ↓
Server Administration


Port 2222
   ↓
Cowrie SSH Honeypot
   ↓
Capture and Monitor SSH Activity
```

This separation allowed the server to remain accessible for administration while Cowrie independently monitored SSH activity directed at the honeypot.

---

## 5. SSH Access

The EC2 instance was accessed using the SSH key pair generated for the instance.

The general SSH connection format was:

```bash
ssh -i <key-file>.pem ubuntu@<EC2-PUBLIC-IP>
```

The private key file was kept l
