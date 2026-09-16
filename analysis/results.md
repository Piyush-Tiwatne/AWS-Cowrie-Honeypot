# Analysis Results

## 1. Data Collection

The Cowrie SSH honeypot was deployed on an AWS EC2 Ubuntu server to collect unsolicited SSH activity during the project data-collection period.

Cowrie recorded authentication attempts, SSH sessions, client information, and commands executed within its emulated environment.

The collected Cowrie JSON logs were analyzed locally using Python.

---

## 2. Analysis Method

The analysis focused on the following aspects of the collected SSH activity:

* Number of SSH connection sessions
* Source IP activity
* Authentication attempts
* SSH client information
* Commands executed by connecting sessions
* Repeated and automated activity patterns
* Approximate geographic distribution of source IP addresses

Raw passwords and source IP addresses were not included in the public repository.

---

## 3. Activity Summary

| Metric                     | Result |
| -------------------------- | -----: |
| SSH connection sessions    | 28,897 |
| Unique external source IPs |     43 |
| Successful-login events    | 28,830 |
| Failed-login events        |      1 |

> **Note:** Cowrie `login.success` events represent authentication accepted by the honeypot's emulated environment. They do not demonstrate compromise of the underlying AWS EC2 host.

---

## 4. Observed Activity

### 4.1 Source IP Activity

The honeypot received SSH connections from multiple external source IP addresses.

The collected data showed that a single source address generated the majority of the recorded connections.

Source IP addresses are not included in this public repository to avoid publishing collected network data.

---

### 4.2 Authentication Activity

The logs contained repeated authentication attempts using commonly targeted usernames.

Authentication activity was analyzed locally to identify repeated login patterns.

Raw passwords collected by the honeypot are not included in the public repository.

---

### 4.3 SSH Client Information

Multiple SSH client implementations were observed in the Cowrie logs, including:

* Go-based SSH clients
* Paramiko-based SSH clients

Client information was analyzed to identify recurring connection and authentication patterns.

---

### 4.4 Command Activity

Several basic system and environment discovery commands were observed, including:

```text
uname
whoami
pwd
ls
```

Highly repetitive command patterns were also observed across multiple sessions.

For example, `uname` can provide information about the operating system and kernel details exposed by the emulated environment.

---

## 5. Automated Activity

The high frequency of repeated connections, authentication events, client patterns, and command sequences suggests that a significant portion of the observed activity was automated or scripted.

The analysis focuses on observable activity within the honeypot and does not attempt to identify a specific attacker, malware family, or tool based solely on these observations.

---

## 6. GeoIP Visualization

The collected source IP addresses were processed using GeoIP information and visualized using Folium.

The visualization provides an approximate geographic location associated with each IP address.

> **Important:** GeoIP information does not identify the physical location or identity of an attacker. IP-based geographic information is approximate and may represent a VPN, proxy, hosting provider, or other intermediary.

The generated interactive map is not included in the public repository because it contains collected source IP information.

---

## 7. Key Findings

The analysis provided practical observations about unsolicited SSH activity received by the honeypot:

* The honeypot recorded **28,897 SSH connection sessions**.
* Activity originated from **43 unique external source IP addresses**.
* Repeated authentication activity was observed.
* Multiple SSH client implementations were identified.
* Basic system-discovery commands such as `uname`, `whoami`, `pwd`, and `ls` were observed.
* Repeated connection and command patterns indicated substantial automated or scripted activity.
* GeoIP visualization provided an approximate geographic view of the observed source addresses.

---

## 8. Key Learnings

The project provided practical experience with:

* AWS EC2 deployment
* Ubuntu Linux administration
* SSH and networking
* Cowrie honeypot deployment and operation
* JSON log processing
* Python-based data analysis
* SSH session and client analysis
* GeoIP visualization using Folium
* Security monitoring and observation

---

## 9. Limitations

The analysis has several limitations:

1. **Limited dataset**
   The dataset represents activity collected by a single honeypot deployment during a specific collection period.

2. **Not representative of all Internet SSH activity**
   The observed activity should not be treated as representative of global or general Internet-wide SSH activity.

3. **IP address attribution**
   An IP address does not necessarily represent an individual attacker. Addresses may belong to shared infrastructure, proxies, VPNs, cloud providers, or compromised systems.

4. **GeoIP accuracy**
   GeoIP information provides an approximate location and should not be interpreted as the physical location of an attacker.

5. **Emulated environment**
   Cowrie provides an emulated SSH environment rather than a real production SSH server.

6. **Authentication interpretation**
   Cowrie authentication events occur within the honeypot's emulated environment and should not be interpreted as confirmed compromise of the underlying AWS EC2 host.

---

## 10. Conclusion

The Cowrie deployment successfully collected and analyzed unsolicited SSH activity against an AWS EC2-hosted honeypot.

The analysis demonstrated how honeypot logs can be used to examine connection patterns, authentication activity, SSH clients, command execution, and approximate source locations.

The project also provided practical experience in combining **AWS, Linux, SSH, Python, log analysis, and security monitoring** into a hands-on cybersecurity monitoring system.
