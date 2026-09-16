\# Analysis Results



\## Data Collection



The Cowrie honeypot was deployed on an AWS EC2 Ubuntu server and

allowed to collect unsolicited SSH activity during the project

data-collection period.



The analysis was performed on Cowrie JSON logs using Python.



\## Summary



| Metric | Result |

|---|---:|

| SSH connection sessions | 28,897 |

| Unique external source IPs | 43 |

| Successful-login events | 28,830 |

| Failed-login events | 1 |



> Note: Cowrie `login.success` events represent authentication accepted

> by the honeypot's emulated environment. They do not demonstrate

> compromise of the underlying EC2 host.



\## Observed Activity



\### Source IP Activity



The honeypot received connections from multiple external source IPs.

A single source address generated the majority of the recorded

connections.



Source IP addresses are not included in this public repository to

avoid publishing collected network data.



\### Authentication Activity



The logs contained repeated authentication attempts using commonly

targeted usernames.



Authentication data was analyzed locally but raw passwords are not

included in this repository.



\### SSH Client Information



Multiple SSH client implementations were observed in the Cowrie logs,

including Go-based and Paramiko-based SSH clients.



The client information was used to identify recurring connection

patterns.



\### Command Activity



Observed commands included:



\- `uname`

\- `whoami`

\- `pwd`

\- `ls`



Highly repetitive command patterns were also observed.



Commands such as `uname` can provide system information such as the

operating-system and kernel details available in the emulated

environment.



\## Automated Activity



The high frequency of repeated connections, authentication events,

client patterns, and commands suggests that a significant portion of

the observed activity was automated or scripted.



The project does not attempt to identify a specific attacker,

malware family, or tool based only on these observations.



\## GeoIP Visualization



Source IP addresses were processed using GeoIP information and

visualized with Folium.



The visualization provides an approximate geographic location

associated with an IP address. It does not identify the physical

location or identity of an attacker.



The generated interactive map is not included in the public repository

because it contains collected source IP information.



\## Key Learnings



Through this analysis, the project provided practical experience with:



\- AWS EC2 deployment

\- Ubuntu Linux administration

\- SSH and networking

\- Cowrie honeypot operation

\- JSON log processing

\- Python data analysis

\- SSH client and session analysis

\- GeoIP visualization

\- Security monitoring



\## Limitations



\- The dataset represents one honeypot deployment and one collection

&#x20; period.

\- Results should not be treated as representative of all Internet SSH

&#x20; activity.

\- An IP address does not necessarily represent an individual attacker.

\- GeoIP results are approximate.

\- Cowrie provides an emulated environment rather than a real production

&#x20; SSH server.

\- Honeypot authentication events should not be interpreted as confirmed

&#x20; compromise of the EC2 host.

