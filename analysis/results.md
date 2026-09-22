# Cowrie SSH Honeypot Analysis Results

## 1. Collection Summary

The Cowrie JSON logs were analyzed using a Python script. The analysis covered 10 log files and excluded three known project-owner test IP addresses.

| Metric | Result |
|---|---:|
| Log files analyzed | 10 |
| Total connections | 28,905 |
| Connections after filtering | 28,902 |
| Unique source IPs | 47 |
| Successful login events | 28,831 |
| Failed login events | 1 |
| Malformed JSON lines | 0 |

> Cowrie login-success events represent authentication accepted by the honeypot emulation. They do not indicate successful compromise of the AWS EC2 host.

---

## 2. Top Source IPs

The highest-volume source generated 28,799 connection events.

| Source IP | Connections |
|---|---:|
| 8.213.218.35 | 28,799 |
| 138.68.63.15 | 30 |
| 44.250.212.125 | 8 |
| 47.74.213.140 | 3 |
| 8.219.140.39 | 3 |
| 101.200.184.113 | 3 |
| 165.232.148.53 | 2 |
| 20.40.254.159 | 2 |
| 47.80.21.54 | 2 |
| 20.118.236.47 | 2 |

The results show that most observed connection activity came from a single highly repetitive source.

---

## 3. Username Analysis

The most frequently attempted username was `root`.

| Username | Attempts |
|---|---:|
| root | 28,801 |
| admin | 6 |
| elastic | 3 |
| apache | 2 |
| app | 2 |
| centos | 2 |
| docker | 2 |
| elsearch | 2 |
| es | 2 |
| appuser | 1 |

The dominance of `root` indicates repeated attempts to access the SSH service using a commonly targeted administrative account.

---

## 4. Command Analysis

The most frequently observed command was:

```text
echo -e "\x6F\x6B"

with 28,797 occurrences.

Command	Count
echo -e "\x6F\x6B"	28,797
/bin/./uname -s -v -n -r -m	29
echo 1 > /dev/null && cat /bin/echo	1

The highly repetitive command pattern indicates automated or scripted activity.

The repeated uname command represents system-information discovery within the emulated environment.

5. Observed Client and Protocol Strings

Cowrie recorded several client and protocol identification strings.

Client / Protocol String	Count
SSH-2.0-Go	28,837
SSH-2.0-paramiko_3.4.1	8
GET / HTTP/1.1	6
MGLNDD_13.204.62.18_2222	6
SSH-2.0-libssh_0.7.4	6
SSH-2.0-russh_0.51.1	4
GET /favicon.ico HTTP/1.1	2
SSH-2.0-perlssh	2
SSH-2.0-libssh2_1.11.1	1

The SSH-2.0-Go client string was the dominant observed client identifier.

These strings identify client-reported protocol information; they do not independently identify a specific attacker.

6. HASSH Analysis

HASSH fingerprints were used to group SSH connections according to their SSH handshake characteristics.

HASSH Fingerprint	Count
01ca35584ad5a1b66cf6a9846b5b2821	28,798
16443846184eafde36765c9bab2f4397	29
87e3d9ffee0540b0390f8a5b9c343c08	8
bc3aee897af7d3feb9fc37b89c7d15c9	7
e37f354a101aff5871ba233aa82b84ec	6
1b8acd46a07d2dc9854db9ec4044c45c	4
e54ef3ec27fe1fea7ab64d3fa05359fd	2
3c0eaacec19ba322a90a5541dac09a06	2
Other fingerprints	2

The dominant fingerprint appeared in 28,798 connections, showing a highly repetitive SSH connection pattern.

HASSH grouping can indicate similar SSH client behavior, but it should not be treated as proof that all connections came from the same attacker.

7. Activity by Date

Connection activity was distributed across the following dates:

Date	Connections
2026-09-01	36
2026-09-02	28,809
2026-09-03	25
2026-09-04	13
2026-09-05	7
2026-09-06	5
2026-09-07	1
2026-09-16	3
2026-09-17	1
2026-09-22	2

The highest observed connection activity occurred on 2026-09-02.

8. Key Findings
The honeypot recorded 28,905 SSH connection events.
After removing three known project-owner test IPs, 28,902 external connection events remained.
47 unique source IPs were observed.
One source generated 28,799 connections, representing the majority of observed activity.
The username root was the most frequently attempted username.
The command echo -e "\x6F\x6B" was observed 28,797 times, indicating highly repetitive automated activity.
SSH-2.0-Go was the most frequently observed client string.
The dominant HASSH fingerprint appeared in 28,798 connections.
The results demonstrate how a honeypot can capture and analyze repeated SSH activity without exposing the production system.
9. Analysis Limitations

The analysis has several limitations:

A source IP address does not necessarily represent a unique attacker.
GeoIP information is approximate and should not be treated as an exact physical location.
Client strings and HASSH fingerprints describe observed connection characteristics but do not independently identify an attacker.
Cowrie operates as an emulated environment; successful honeypot authentication does not mean the AWS EC2 host was compromised.
The collected commands provide behavioral evidence but are not sufficient by themselves to identify a specific malware family or threat actor.
The analysis excludes the project's known manual testing IP addresses to reduce contamination of the external activity results.
10. Conclusion

The analysis demonstrates the use of Cowrie and Python to collect and investigate SSH activity against a public-facing honeypot.

The collected data was analyzed across connection sources, usernames, commands, client strings, HASSH fingerprints, and activity over time. The results showed highly repetitive SSH activity, particularly from automated connection patterns.

The project demonstrates a practical workflow:

AWS EC2
   ↓
Ubuntu Linux
   ↓
Cowrie SSH Honeypot
   ↓
JSON Security Logs
   ↓
Python Log Analysis
   ↓
Security Findings
