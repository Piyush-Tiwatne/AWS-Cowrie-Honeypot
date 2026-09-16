# Challenges and Lessons Learned

## 1. Overview

Several practical challenges were encountered during the deployment, configuration, testing, and analysis of the Cowrie SSH honeypot.

Resolving these issues provided hands-on experience with cloud infrastructure, Linux administration, networking, Python development, log analysis, and security monitoring.

---

## 2. Challenges Encountered

### 2.1 Cowrie Dependency Installation

During the initial Cowrie installation, the development dependencies caused a build problem involving the `pytype` package.

The development dependencies were not required to operate the honeypot, so the base Cowrie package was installed instead.

This allowed Cowrie to be installed and operated successfully.

**Lesson learned:**
Not every development dependency is required for production or runtime operation. Understanding which dependencies are actually necessary can simplify deployment and troubleshooting.

---

### 2.2 SSH and Honeypot Port Separation

The EC2 server required SSH access for administration while Cowrie needed a separate port for honeypot activity.

The following port separation was used:

```text id="5j8s2p"
Port 22
   ↓
EC2 Administrative SSH


Port 2222
   ↓
Cowrie SSH Honeypot
```

This allowed the server to be administered through the normal SSH service while Cowrie independently handled honeypot connections.

**Lesson learned:**
Separating administrative services from monitored or exposed services helps maintain clear boundaries between system administration and honeypot activity.

---

### 2.3 AWS Security Group Configuration

The AWS Security Group had to allow TCP traffic on port `2222` so that external SSH connections could reach the honeypot.

Administrative SSH access on port `22` was restricted to the administrator's current public IP address.

Correctly configuring these rules was necessary for both server administration and honeypot accessibility.

**Lesson learned:**
Cloud firewall rules directly affect network connectivity, and incorrect inbound rules can prevent legitimate administrative access or prevent the honeypot from receiving external traffic.

---

### 2.4 SSH Connection Troubleshooting

During testing, an SSH connection initially timed out because the Security Group contained an outdated source IP address.

The SSH rule was updated to the administrator's current public IP address, after which the connection worked correctly.

**Lesson learned:**
When using IP-based cloud firewall rules, a change in the client's public IP address can cause previously working SSH connections to fail.

A connection timeout should therefore be investigated across multiple layers, including:

```text id="0tq3av"
Client
  ↓
Internet / Network
  ↓
AWS Security Group
  ↓
EC2 Instance
  ↓
SSH Service
```

---

### 2.5 Log Analysis Error

The first version of the Python analysis script counted all Cowrie events when calculating the total number of connections.

This produced an incorrect connection count because a single SSH session can generate multiple Cowrie events.

The analysis was corrected to count only:

```text id="4m8w1n"
cowrie.session.connect
```

This produced the intended count of SSH connection sessions.

**Lesson learned:**
Log analysis requires a clear understanding of the meaning of each event type. Multiple log events may belong to a single session, so metrics must be defined before they are calculated.

---

### 2.6 GeoIP API Handling

The GeoIP visualization required external IP geolocation requests.

The analysis script was designed to handle potential request failures by:

* Using request timeouts
* Checking HTTP responses
* Handling unsuccessful lookups
* Handling network errors
* Adding a delay between requests

These measures reduced the risk of the analysis process stopping because of a single unsuccessful GeoIP request.

**Lesson learned:**
External services can fail or become unavailable, so scripts that depend on APIs should handle network and response errors gracefully.

---

### 2.7 Data Privacy

The collected honeypot logs contained potentially sensitive information, including source IP addresses and authentication-related data.

To reduce unnecessary exposure, the following information was kept out of the public repository:

* Raw Cowrie logs
* Passwords
* Private SSH keys
* Source IP addresses
* Generated GeoIP maps containing collected IP information

The public repository contains the analysis methodology and sanitized results rather than the raw collected data.

**Lesson learned:**
Security monitoring projects can themselves collect sensitive information. Protecting the collected data is therefore an important part of the project.

---

### 2.8 Interpretation of Honeypot Data

Another challenge was correctly interpreting what the collected events represented.

Cowrie operates within an emulated SSH environment. Therefore, an authentication accepted by Cowrie does not demonstrate that the underlying EC2 host was compromised.

Similarly, a source IP address represents a network endpoint and cannot automatically be treated as an individual attacker.

**Lesson learned:**
Security telemetry must be interpreted within its technical context. Observed activity should be distinguished from conclusions that the available data cannot directly support.

---

# 3. Lessons Learned

The project provided practical experience in the following areas:

### Cloud Infrastructure

* AWS EC2 deployment
* AWS Security Group configuration
* Cloud-based SSH access
* Troubleshooting cloud connectivity

### Linux Administration

* Ubuntu server administration
* Linux user management
* Non-root service operation
* Python virtual environments
* Service and port verification

### Networking and Security

* SSH configuration
* TCP ports
* IP-based firewall rules
* Network connection troubleshooting
* Honeypot deployment
* Security monitoring

### Python and Data Analysis

* Python scripting
* JSON log processing
* Event-based analysis
* Session counting
* SSH client analysis
* Command analysis
* HASSH fingerprint analysis
* API error handling
* GeoIP visualization

### Security and Data Handling

* Least-privilege operation
* Separation of administrative and honeypot services
* Protection of collected network data
* Sanitization of public project data
* Careful interpretation of security telemetry

---

# 4. Overall Learning

The project demonstrated that deploying a security monitoring system involves more than simply installing a honeypot.

The work required understanding the interaction between:

```text id="7k2c9f"
AWS EC2
   ↓
Security Groups
   ↓
Ubuntu Linux
   ↓
SSH
   ↓
Cowrie
   ↓
JSON Logs
   ↓
Python Analysis
   ↓
Security Findings
```

Troubleshooting the deployment and validating the collected data helped develop practical experience in building, operating, and analyzing a cloud-based cybersecurity monitoring environment.
