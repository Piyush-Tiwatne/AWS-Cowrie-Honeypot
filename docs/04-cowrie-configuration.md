# Cowrie Configuration

## Overview

After installing Cowrie, the honeypot was configured to listen for
SSH connections on port `2222`.

Port `22` was kept available for normal administrative SSH access to
the EC2 server.

## 1. Cowrie Configuration File

The main Cowrie configuration file used in this project was:


~/cowrie/etc/cowrie.cfg

The configuration was edited using:

nano ~/cowrie/etc/cowrie.cfg

## 2. Configure the Honeypot Hostname

The honeypot hostname was configured as:

hostname = web-server-01

This makes the emulated system appear as a server named
web-server-01 to SSH clients interacting with the honeypot.

## 3. Configure the SSH Listener

Cowrie was configured to listen on port 2222:

listen_endpoints = tcp:2222:interface=0.0.0.0

This means Cowrie accepts TCP connections on port 2222 from
available network interfaces.

## 4. Why Port 2222 Was Used

The EC2 instance used:

Port 22   → Normal administrative SSH access
Port 2222 → Cowrie SSH honeypot

Separating the ports allows the server administrator to access the
EC2 instance normally while exposing a different port for the
honeypot.

## 5. AWS Security Group

The EC2 Security Group was configured to allow:

TCP 22   → SSH administration
TCP 2222 → Cowrie honeypot

SSH administrative access was restricted to the administrator's
current IP address rather than being openly exposed.

## 6. Start Cowrie

After configuration, the honeypot was started using:

cowrie start

The status was checked using:

cowrie status
## 7. Verify the Listening Port

The Linux ss command was used to verify that Cowrie was listening
on port 2222:

ss -lnt | grep 2222

A listening entry for port 2222 confirmed that the honeypot was
ready to accept SSH connections.

Result

Cowrie was successfully configured to provide an emulated SSH
service on port 2222, while port 22 remained available for
administrative SSH access to the Ubuntu EC2 instance.