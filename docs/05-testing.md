 Testing the Cowrie Honeypot

## Overview

After configuring Cowrie, the SSH honeypot was tested from a Windows
machine to verify that external SSH connections were being received
and logged correctly.

## 1. Verify Cowrie Status

On the Ubuntu EC2 server, Cowrie status was checked using:


cowrie status

The service was expected to show as running.

The listening port was also verified:

ss -lnt | grep 2222

## 2. Connect to the Honeypot from Windows

Windows PowerShell was used to connect to the EC2 public IP on port
2222:

ssh -p 2222 testuser@<EC2-PUBLIC-IP>

A fake username and password were used for testing.

No real credentials were used in the honeypot testing process.

## 3. Verify the Honeypot Shell

After connecting, Cowrie provided an emulated SSH shell.

Basic commands were entered to verify that the interaction was being
captured:

whoami
pwd
ls
uname -a
exit

These commands were executed only for testing the honeypot.

## 4. Verify Log Generation

Cowrie stores its JSON event logs in:

~/cowrie/var/log/cowrie/

The log files were checked using:

ls -lh ~/cowrie/var/log/cowrie/

Cowrie records different types of events, including:

SSH connections
Authentication activity
SSH client information
Commands entered
Session information

## 5. Example Event Types

Some of the Cowrie event types observed during testing included:

cowrie.session.connect
cowrie.login.success
cowrie.login.failed
cowrie.command.input
cowrie.client.version
cowrie.client.kex
cowrie.session.closed

These events were later processed using Python for analysis.

## 6. Separating Test Traffic

The project's own test connection was identified using its source IP
address.

When calculating external activity, the project owner's test traffic
was excluded from the external-source analysis.

This prevents manually generated test activity from being interpreted
as unsolicited Internet activity.

Result

The test confirmed that:

The EC2 instance was reachable on port 2222.
Cowrie accepted SSH connections.
The emulated shell responded to commands.
Cowrie generated structured JSON log events.
The collected logs could be used for further analysis.