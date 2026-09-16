# AWS Cowrie Honeypot – SSH Attack Monitoring System

An AWS-based SSH honeypot project using **Cowrie** to capture, analyze, and visualize unsolicited SSH activity in a controlled environment.

## Overview

This project deploys **Cowrie**, an SSH honeypot, on an **AWS EC2 Ubuntu server**.

Cowrie provides an emulated SSH environment that records activity such as:

* SSH connection attempts
* Authentication activity
* SSH client information
* Shell commands
* SSH session information

Python scripts were developed to process the collected Cowrie JSON logs and analyze connection, authentication, client, command, and HASSH fingerprint activity.

GeoIP data was also used to create an approximate geographic visualization of observed source IP addresses.

> **Important:** Cowrie operates in an emulated environment. Authentication events recorded by Cowrie do not demonstrate compromise of the underlying EC2 host.

---

## Architecture

```text
                    Windows Machine
                          │
                          │ SSH
                          ▼
                ┌─────────────────────┐
                │     AWS EC2         │
                │    Ubuntu Linux     │
                └──────────┬──────────┘
                           │
                           │ Port 2222
                           ▼
                ┌─────────────────────┐
                │   Cowrie Honeypot   │
                │   Emulated SSH      │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Cowrie JSON Logs  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │  Python Analysis    │
                └──────────┬──────────┘
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
          Activity Analysis     GeoIP Data
                                     │
                                     ▼
                             Folium Visualization
```

### Network Configuration

```text
Port 22
   ↓
Administrative SSH
   ↓
EC2 Server Management

Port 2222
   ↓
Cowrie SSH Honeypot
   ↓
Unsolicited SSH Activity
```

Administrative SSH access was separated from the honeypot service.

---

## Technologies Used

| Technology   | Purpose                                        |
| ------------ | ---------------------------------------------- |
| AWS EC2      | Cloud server hosting                           |
| Ubuntu Linux | Server operating system                        |
| Cowrie       | SSH honeypot                                   |
| Python       | Log processing and analysis                    |
| JSON         | Structured honeypot logs                       |
| SSH          | Remote administration and honeypot interaction |
| Folium       | Interactive GeoIP visualization                |
| GeoIP        | Approximate source IP geolocation              |

---

## Project Features

* AWS EC2 deployment
* Ubuntu Linux server administration
* Dedicated non-root user for Cowrie
* Python virtual environment
* SSH honeypot on port `2222`
* Authentication activity collection
* SSH client information collection
* Command activity logging
* JSON log processing
* Python-based activity analysis
* Source IP analysis
* HASSH fingerprint analysis
* GeoIP visualization
* Security-focused data sanitization

---

## Data Collection

The Cowrie honeypot was deployed on an AWS EC2 Ubuntu server and allowed to collect unsolicited SSH activity during the project data-collection period.

The collected logs contained structured events related to SSH sessions, authentication, clients, commands, and SSH handshake information.

The logs were analyzed locally using Python.

Raw logs containing collected network data were not published in the repository.

---

## Analysis Results

During the project data-collection period, the honeypot recorded:

| Metric                     |     Result |
| -------------------------- | ---------: |
| SSH connection sessions    | **28,897** |
| Unique external source IPs |     **43** |
| Successful-login events    | **28,830** |
| Failed-login events        |      **1** |

The **43 unique external source IPs** were calculated after excluding project-owner test traffic.

The total connection count includes the project's own test session.

> **Authentication interpretation:** `cowrie.login.success` represents authentication accepted by Cowrie's emulated environment. It does not demonstrate successful compromise of the underlying AWS EC2 host.

---

## Observed Activity

The collected logs showed several recurring activity patterns:

* Repeated SSH connections
* Repeated authentication events
* Multiple SSH client implementations
* Repeated command sequences
* Basic system-information discovery commands
* Recurring SSH handshake characteristics

Example commands observed included:

```text
uname
whoami
pwd
ls
```

The frequency and repetition of these patterns suggest that a significant portion of the observed activity was automated or scripted.

The project does not attempt to identify a specific attacker, malware family, or tool based solely on these observations.

---

## HASSH Analysis

Cowrie SSH handshake information was analyzed to identify recurring HASSH fingerprints.

HASSH fingerprints can help group connections that exhibit similar SSH handshake characteristics.

They were used in this project as an additional method for identifying recurring connection patterns.

> A HASSH fingerprint does not independently identify a specific attacker.

---

## GeoIP Visualization

Source IP addresses were processed using GeoIP information and visualized using **Folium**.

The visualization provides an approximate geographic representation of the observed source addresses.

> GeoIP information does not establish the physical location or identity of an attacker.

The generated interactive map is not included in the public repository because it contains collected source IP information.

---

## Data Privacy

Because honeypots collect information about external systems, the project was designed to avoid publishing sensitive collected data.

The following were excluded from the public repository:

* Raw Cowrie logs
* Source IP addresses
* Raw passwords
* Private SSH keys
* GeoIP maps containing collected IP information

The repository contains sanitized results, analysis methodology, and project documentation.

---

## Repository Structure

```text
aws-cowrie-honeypot/
│
├── README.md
│
├── docs/
│   ├── 01-aws-ec2-setup.md
│   ├── 02-linux-setup.md
│   ├── 03-cowrie-installation.md
│   ├── 04-cowrie-configuration.md
│   ├── 05-testing.md
│   ├── 06-log-analysis.md
│   └── 07-challenges.md
│
├── scripts/
│   ├── analyze_cowrie.py
│   └── cowrie_map.py
│
├── screenshots/
│
├── analysis/
│   └── results.md
│
└── .gitignore
```

---

## Documentation

Detailed project documentation is organized into separate sections:

| Document                     | Description                                         |
| ---------------------------- | --------------------------------------------------- |
| `01-aws-ec2-setup.md`        | AWS EC2 deployment and Security Group configuration |
| `02-linux-setup.md`          | Ubuntu preparation and dedicated Cowrie user        |
| `03-cowrie-installation.md`  | Cowrie installation and dependency handling         |
| `04-cowrie-configuration.md` | Hostname, SSH listener, and port configuration      |
| `05-testing.md`              | Honeypot connectivity and log-generation testing    |
| `06-log-analysis.md`         | Python-based Cowrie log analysis                    |
| `07-challenges.md`           | Deployment challenges and lessons learned           |
| `analysis/results.md`        | Sanitized analysis results                          |

---

## Challenges and Lessons Learned

The project involved several practical troubleshooting challenges, including:

* Cowrie dependency installation issues
* AWS Security Group configuration
* SSH connection timeouts
* Separation of administrative and honeypot ports
* Correct interpretation of Cowrie event types
* Avoiding double-counting during log analysis
* Handling GeoIP API failures
* Protecting collected network data

These challenges provided hands-on experience with AWS, Linux, SSH, networking, Python, log analysis, and security monitoring.

---

## Limitations

The results should be interpreted within the limitations of the project:

* The dataset represents one honeypot deployment and collection period.
* The results are not representative of all Internet SSH activity.
* An IP address does not necessarily represent an individual attacker.
* GeoIP locations are approximate.
* Cowrie provides an emulated environment rather than a production SSH server.
* Honeypot authentication events do not demonstrate compromise of the underlying EC2 host.
* Observed activity alone is insufficient to conclusively identify a specific attacker, malware family, or tool.

---

## Key Learning Outcomes

This project provided practical experience with:

* **AWS EC2 deployment**
* **Ubuntu Linux administration**
* **SSH and networking**
* **AWS Security Groups**
* **Honeypot deployment**
* **Python scripting**
* **JSON log analysis**
* **SSH client and session analysis**
* **HASSH fingerprint analysis**
* **GeoIP visualization**
* **Security monitoring**
* **Data privacy and sanitization**
* **Cloud troubleshooting**

---

## Conclusion

The project successfully deployed a Cowrie SSH honeypot on an AWS EC2 Ubuntu server and collected unsolicited SSH activity.

Python was then used to process the resulting JSON logs and analyze connection sessions, authentication activity, SSH clients, commands, and HASSH fingerprints.

The project demonstrates a practical workflow for deploying a cloud-based honeypot, collecting security telemetry, processing structured logs, and interpreting observed SSH activity while considering data privacy and the limitations of honeypot-based analysis.
