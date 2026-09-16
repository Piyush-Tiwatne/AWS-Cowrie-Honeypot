# Challenges and Lessons Learned

## Overview

Several practical challenges were encountered while deploying,
configuring, and analyzing the Cowrie SSH honeypot.

## 1. Cowrie Dependency Installation

During installation, the development dependencies caused a build
problem involving the `pytype` package.

The development dependencies were not required for the honeypot to
operate, so the base Cowrie package was installed instead.

This allowed the honeypot to run successfully.

## 2. SSH and Honeypot Port Separation

The EC2 server required SSH access for administration while Cowrie
needed a separate port for honeypot activity.

The following port separation was used:


Port 22   → EC2 administrative SSH
Port 2222 → Cowrie SSH honeypot

This made it possible to manage the server while exposing the
honeypot separately.

3. AWS Security Group Configuration

The AWS Security Group had to allow TCP traffic on port 2222 for
the honeypot.

Administrative SSH access on port 22 was restricted to the
administrator's current IP address.

This demonstrated the importance of correctly configuring cloud
firewall rules.

4. SSH Connection Troubleshooting

During testing, an SSH connection initially timed out because the
Security Group contained an outdated source IP address.

Updating the SSH rule to the current administrator IP resolved the
issue.

This highlighted that cloud firewall rules can depend on the
client's current public IP address.

5. Log Analysis Error

The first version of the Python analysis counted all Cowrie events
when calculating connection totals.

This produced an incorrect connection count because one session
generates multiple events.

The analysis was corrected to count only:

cowrie.session.connect

This produced the correct number of SSH connection sessions.

6. GeoIP API Handling

The GeoIP visualization required external IP geolocation requests.

The script was designed to:

Use a request timeout
Check HTTP responses
Handle unsuccessful lookups
Handle network errors
Add a delay between requests

This reduced the risk of the analysis script failing because of a
single unsuccessful GeoIP request.

7. Data Privacy

The collected logs contained source IP addresses and authentication
data.

For this reason, raw logs, passwords, private keys, and generated
GeoIP maps containing collected IP information were kept out of the
public repository.

The public repository contains analysis methodology and sanitized
results instead.

8. Interpretation of Honeypot Data

A honeypot records activity inside an emulated environment.

Therefore, authentication accepted by Cowrie cannot be treated as
proof that the underlying EC2 host was compromised.

Similarly, an IP address cannot automatically be treated as an
individual attacker.

These limitations were considered when interpreting the collected
data.

Lessons Learned

This project provided practical experience with:

AWS EC2 deployment
Linux administration
SSH configuration
AWS Security Groups
Honeypot deployment
Python scripting
JSON log analysis
Network activity analysis
GeoIP visualization
Data privacy and security
Troubleshooting cloud-based systems