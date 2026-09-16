# Testing the Cowrie Honeypot

## 1. Overview

After configuring Cowrie, the SSH honeypot was tested from a Windows machine to verify that external SSH connections could reach the honeypot and that Cowrie correctly captured the resulting activity.

The testing process covered service status, network connectivity, shell interaction, and log generation.

---

## 2. Verify Cowrie Status

Before performing the connection test, the Cowrie service was checked on the Ubuntu EC2 server:

```bash id="h6k4c2"
cowrie status
```

The service was expected to show a **running** status.

The configured listening port was also verified using:

```bash id="z9yq0a"
ss -lnt | grep 2222
```

A listening entry for port `2222` confirmed that Cowrie was ready to receive SSH connections.

---

## 3. Connect to the Honeypot from Windows

Windows PowerShell was used to connect to the EC2 public IP address on port `2222`:

```bash id="v8t4xm"
ssh -p 2222 testuser@<EC2-PUBLIC-IP>
```

A test username and password were used during the connection.

No real credentials were used as part of the honeypot testing process.

The connection was directed to port `2222`, ensuring that the test interacted with Cowrie rather than the actual administrative SSH service on port `22`.

---

## 4. Verify the Emulated Shell

After authentication, Cowrie provided an emulated SSH shell.

The following commands were entered to verify that shell interaction was being captured:

```bash id="9wq5pd"
whoami
pwd
ls
uname -a
exit
```

These commands were used only to test the honeypot's ability to receive and record shell interaction.

The commands also represented common basic system-information and environment-discovery activity.

---

## 5. Verify Log Generation

Cowrie stores its JSON event logs in:

```text id="j3x1v8"
~/cowrie/var/log/cowrie/
```

The log directory was checked using:

```bash id="4z6wqs"
ls -lh ~/cowrie/var/log/cowrie/
```

Cowrie records structured events related to different stages of an SSH session, including:

* SSH connections
* Authentication activity
* SSH client information
* Commands entered
* Session information
* Session termination

These structured JSON logs were later used as the input for Python-based analysis.

---

## 6. Example Cowrie Event Types

The following event types were observed during testing:

```text id="2u0d4s"
cowrie.session.connect
cowrie.login.success
cowrie.login.failed
cowrie.command.input
cowrie.client.version
cowrie.client.kex
cowrie.session.closed
```

Each event represents a different activity associated with an SSH session.

For example:

| Event                    | Purpose                                         |
| ------------------------ | ----------------------------------------------- |
| `cowrie.session.connect` | Records an incoming SSH connection              |
| `cowrie.login.success`   | Records authentication accepted by the honeypot |
| `cowrie.login.failed`    | Records a failed authentication attempt         |
| `cowrie.command.input`   | Records a command entered during a session      |
| `cowrie.client.version`  | Records SSH client information                  |
| `cowrie.client.kex`      | Records key-exchange information                |
| `cowrie.session.closed`  | Records the end of an SSH session               |

These events were later processed using Python to perform the project analysis.

---

## 7. Separate Test Traffic from External Activity

The project's own test connection was identified using its source IP address.

When analyzing unsolicited external activity, the project's manually generated test traffic was excluded from the external-source analysis.

This prevented project-generated test activity from being incorrectly interpreted as unsolicited Internet activity.

---

## 8. Testing Workflow

The complete testing process was:

```text
Windows PowerShell
       │
       │ SSH connection
       │ Port 2222
       ▼
AWS EC2 Public IP
       │
       ▼
Cowrie Honeypot
       │
       ├── Authentication Event
       ├── SSH Client Event
       ├── Command Event
       └── Session Event
                │
                ▼
       Cowrie JSON Logs
                │
                ▼
       Python Analysis
```

---

## 9. Result

The testing successfully confirmed that:

* The EC2 instance was reachable on port `2222`.
* Cowrie accepted SSH connections.
* The honeypot provided an emulated SSH shell.
* Shell commands were captured by Cowrie.
* Structured JSON log events were generated.
* SSH session and client information was recorded.
* The collected logs could be used for further Python-based analysis.

The successful test confirmed that the Cowrie honeypot was operational and ready for the project's data-collection phase.
