# Cowrie Configuration

## 1. Overview

After installing Cowrie, the honeypot was configured to provide an emulated SSH service on port `2222`.

Port `22` was kept available for normal administrative SSH access to the AWS EC2 Ubuntu server.

This separation allowed the server to be administered normally while Cowrie monitored SSH activity directed toward the honeypot.

---

## 2. Cowrie Configuration File

The main Cowrie configuration file used in the project was:

```text
~/cowrie/etc/cowrie.cfg
```

The configuration file was edited using:

```bash
nano ~/cowrie/etc/cowrie.cfg
```

The required hostname and SSH listener settings were configured in this file.

---

## 3. Configure the Honeypot Hostname

The emulated honeypot hostname was configured as:

```ini
hostname = web-server-01
```

This makes the emulated system appear as a server named `web-server-01` to SSH clients interacting with the honeypot.

The hostname helps make the emulated environment appear more like a normal server during SSH sessions.

---

## 4. Configure the SSH Listener

Cowrie was configured to listen for SSH connections on port `2222`:

```ini
listen_endpoints = tcp:2222:interface=0.0.0.0
```

The configuration specifies:

| Setting   | Value     | Purpose                                |
| --------- | --------- | -------------------------------------- |
| Protocol  | TCP       | Transport protocol used by SSH         |
| Port      | `2222`    | Port used by the Cowrie honeypot       |
| Interface | `0.0.0.0` | Listen on available network interfaces |

Using `0.0.0.0` allows Cowrie to accept connections arriving at the EC2 instance on port `2222`, subject to the AWS Security Group and other network controls.

---

## 5. Port Separation

The EC2 instance used separate ports for administration and honeypot activity:

```text
Port 22
   ↓
Normal SSH Service
   ↓
EC2 Server Administration


Port 2222
   ↓
Cowrie SSH Honeypot
   ↓
Capture and Monitor SSH Activity
```

This separation allowed administrative SSH access to remain available while exposing the Cowrie service separately for monitoring unsolicited SSH activity.

---

## 6. AWS Security Group Configuration

The EC2 Security Group was configured with the following inbound rules:

| Protocol | Port | Access / Purpose          |
| -------- | ---: | ------------------------- |
| TCP      |   22 | Administrative SSH access |
| TCP      | 2222 | Cowrie SSH honeypot       |

Administrative SSH access on port `22` was restricted to the administrator's current public IP address.

Port `2222` was exposed for the Cowrie honeypot so that unsolicited SSH connections could reach the emulated service.

---

## 7. Start Cowrie

After completing the configuration, Cowrie was started using:

```bash
cowrie start
```

The running status was then checked using:

```bash
cowrie status
```

A running status confirmed that the Cowrie process had started successfully.

---

## 8. Verify the Listening Port

The Linux `ss` command was used to verify that Cowrie was listening on port `2222`:

```bash
ss -lnt | grep 2222
```

A listening entry for port `2222` confirmed that the Cowrie service was bound to the configured port and ready to accept incoming TCP connections.

---

## 9. Configuration Summary

The final network configuration was:

| Component           | Configuration             |
| ------------------- | ------------------------- |
| Administrative SSH  | Port `22`                 |
| Cowrie SSH honeypot | Port `2222`               |
| Cowrie hostname     | `web-server-01`           |
| Cowrie listener     | `0.0.0.0:2222`            |
| Configuration file  | `~/cowrie/etc/cowrie.cfg` |

---

## 10. Result

Cowrie was successfully configured to provide an emulated SSH service on port `2222`.

Port `22` remained available for administrative SSH access to the Ubuntu EC2 instance, while port `2222` was dedicated to the Cowrie honeypot.

The listening-port verification confirmed that Cowrie was ready to receive SSH connections and begin collecting honeypot activity.
