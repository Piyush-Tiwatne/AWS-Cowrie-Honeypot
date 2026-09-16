# AWS Cowrie Honeypot – SSH Attack Monitoring System

An AWS-based SSH honeypot project using Cowrie to capture and analyze
unsolicited SSH activity in a controlled environment.

## Overview

This project deploys Cowrie, an SSH honeypot, on an AWS EC2 Ubuntu
server. The honeypot emulates an SSH environment and records connection,
authentication, client, and command activity.

Python scripts are used to analyze the collected Cowrie JSON logs and
visualize approximate source locations using GeoIP data.

## Architecture

Windows Machine
       |
       | SSH
       v
AWS EC2 Ubuntu Server
       |
       v
Cowrie SSH Honeypot
       |
       v
Cowrie JSON Logs
       |
       v
Python Log Analysis
       |
       v
GeoIP Visualization

## Technologies Used

- AWS EC2
- Ubuntu Linux
- Cowrie
- Python
- SSH
- JSON
- Folium
- GeoIP

## Project Features

- AWS EC2 deployment
- Dedicated Linux user for Cowrie
- SSH honeypot on port 2222
- Authentication activity collection
- SSH client information collection
- Command activity logging
- JSON log analysis using Python
- Source IP analysis
- HASSH fingerprint analysis
- GeoIP visualization

## Data Collection

The honeypot was deployed on an AWS EC2 Ubuntu server and allowed to
collect unsolicited SSH activity during the project data-collection
period.

The collected Cowrie logs were analyzed locally using Python.

## Analysis Results

During the collection period, the honeypot recorded:

- 28,897 SSH connection sessions
- 43 unique external source IPs after excluding project-owner test traffic
- 28,830 successful-login events
- 1 failed-login event

Cowrie authentication events represent activity accepted by the
honeypot's emulated environment. They do not demonstrate compromise
of the underlying EC2 host.

## Observed Activity

The logs contained:

- Repeated SSH connections
- Repeated authentication activity
- Multiple SSH client implementations
- System-information reconnaissance commands
- Highly repetitive command patterns

The frequency and repetition of these patterns suggest that a
significant portion of the observed activity was automated or scripted.

The project does not attempt to identify a specific attacker, malware
family, or tool based only on these observations.

## GeoIP Visualization

Source IP addresses were processed using GeoIP information and
visualized using Folium.

The geographic locations are approximate and should not be interpreted
as the physical location or identity of an attacker.

The generated map is not included in this repository because it
contains collected source IP information.

## Repository Structure

aws-cowrie-honeypot/
├── README.md
├── docs/
│   ├── 01-aws-ec2-setup.md
│   ├── 02-linux-setup.md
│   ├── 03-cowrie-installation.md
│   ├── 04-cowrie-configuration.md
│   ├── 05-testing.md
│   ├── 06-log-analysis.md
│   └── 07-challenges.md
├── scripts/
│   ├── analyze_cowrie.py
│   └── cowrie_map.py
├── screenshots/
├── analysis/
│   └── results.md
└── .gitignore