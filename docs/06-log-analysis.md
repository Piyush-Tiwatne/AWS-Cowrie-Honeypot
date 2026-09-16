# Cowrie Log Analysis

## Overview

Cowrie stores honeypot activity in structured JSON log files.

Python was used to process these logs and extract information about
SSH connections, source IP addresses, authentication activity, SSH
clients, commands, and HASSH fingerprints.

## 1. Cowrie Log Location

The collected logs were stored on the Ubuntu EC2 server at:


~/cowrie/var/log/cowrie/

The main JSON log files follow the naming pattern:

cowrie.json
cowrie.json.<date>

## 2. Python Analysis Script

The analysis was performed using:

scripts/analyze_cowrie.py

The script reads all Cowrie JSON log files and processes each event.

## 3. Connection Analysis

SSH connection events were identified using:

cowrie.session.connect

The analysis counted:

Total SSH connection sessions
Source IP addresses
Connections by date

Only cowrie.session.connect events were counted when calculating
connection totals.

## 4. Authentication Analysis

Authentication events were identified using:

cowrie.login.success
cowrie.login.failed

The analysis recorded the usernames associated with authentication
events.

Raw passwords were not included in the public repository.

## 5. SSH Client Analysis

Cowrie records the SSH client version presented by connecting clients.

The event:

cowrie.client.version

was used to identify recurring SSH client implementations.

Examples observed in the dataset included Go-based SSH clients and
Paramiko-based clients.

## 6. Command Analysis

Commands entered into the emulated shell were identified using:

cowrie.command.input

Examples observed included:

uname
whoami
pwd
ls

The logs also contained highly repetitive command patterns.

Commands such as uname can provide system information such as the
operating system and kernel details available in the emulated
environment.

## 7. HASSH Analysis

Cowrie records SSH handshake information that can include a HASSH
fingerprint.

The event:

cowrie.client.kex

was used to analyze recurring HASSH fingerprints.

HASSH can help group connections with similar SSH handshake
characteristics. It does not identify an attacker by itself.

## 8. Analysis Results

During the project data-collection period, the analysis produced:

Metric	Result
SSH connection sessions	28,897
Unique external source IPs	43
Successful-login events	28,830
Failed-login events	1

The 43 external source IPs were calculated after excluding the
project owner's test traffic.

The total connection count includes the project's own test session.

## 9. Observed Activity Patterns

A large number of repeated connections, authentication events,
client patterns, and commands were observed.

The repetition and frequency of these events suggest that a
significant portion of the observed activity was automated or
scripted.

A specific attacker, malware family, or tool was not identified based
only on these observations.

## 10. Important Interpretation

Cowrie provides an emulated SSH environment.

Therefore, a cowrie.login.success event means that authentication
was accepted by the honeypot. It does not demonstrate successful
compromise of the underlying AWS EC2 host.

Similarly, an IP address represents a network source address and does
not necessarily represent an individual attacker.

## 11. GeoIP Visualization

The source IP addresses were also processed using GeoIP information.

The visualization was created using:

Python
Folium
IP geolocation data

The resulting map shows approximate geographic locations associated
with source IP addresses.

GeoIP information does not establish the physical location or
identity of an attacker.

The generated map is kept outside the public repository because it
contains collected source IP information.

## 12. Limitations

The analysis has several limitations:

The dataset represents one honeypot deployment and collection
period.
The results are not representative of all Internet SSH activity.
An IP address does not necessarily represent an individual attacker.
GeoIP locations are approximate.
Cowrie uses an emulated environment rather than a production SSH
server.
Honeypot authentication events do not demonstrate compromise of the
underlying EC2 host.