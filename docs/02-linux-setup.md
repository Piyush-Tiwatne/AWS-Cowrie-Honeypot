# Linux Setup

## 1. Objective

After deploying the AWS EC2 instance, the Ubuntu server was prepared to run the Cowrie SSH honeypot in an isolated and controlled environment.

The setup included system updates, creation of a dedicated non-root user, Python environment configuration, and preparation of the Cowrie installation directory.

---

## 2. System Update

The Ubuntu package lists were updated and available system packages were upgraded before installing the required software.

```bash
sudo apt update
sudo apt upgrade -y
```

Keeping the system updated helped ensure that the server had the latest available package updates before configuring the honeypot.

---

## 3. Dedicated Cowrie User

A separate Linux user was created specifically for running Cowrie.

```bash
sudo adduser cowrie
```

Cowrie was operated using this account instead of the root account.

### Why Use a Separate User?

Running the honeypot under a dedicated non-root user follows the **principle of least privilege**.

The Cowrie process therefore does not require full administrative privileges to perform its normal operations. If the honeypot process encounters a security issue, restricting its permissions can reduce the potential impact on the underlying system.

---

## 4. Switch to the Cowrie User

After creating the account, the session was switched to the dedicated Cowrie user:

```bash
su - cowrie
```

The Cowrie user was then used for the honeypot installation and operation.

---

## 5. Python Virtual Environment

A Python virtual environment was created for the Cowrie installation.

```bash
python3 -m venv cowrie-env
source cowrie-env/bin/activate
```

After activation, the terminal displayed the virtual environment name:

```text
(cowrie-env)
```

The virtual environment isolates project-specific Python packages from the system Python environment.

This helps prevent dependency conflicts between Cowrie and other Python software installed on the server.

---

## 6. Python and Package Setup

The Python package manager was upgraded inside the virtual environment:

```bash
python -m pip install --upgrade pip
```

Cowrie was then installed according to its project requirements.

All Cowrie-related Python packages were kept within the project's virtual environment.

---

## 7. Directory Structure

The main Cowrie installation directory was located under the dedicated user's home directory:

```text
/home/cowrie/cowrie/
```

Cowrie's log files were stored under:

```text
/home/cowrie/cowrie/var/log/cowrie/
```

The directory structure provided a dedicated location for the honeypot application and its collected logs.

---

## 8. Setup Overview

The Linux environment was configured with the following components:

```text
Ubuntu EC2 Server
│
├── cowrie user
│   └── Non-root account
│
├── cowrie-env
│   └── Python virtual environment
│
└── /home/cowrie/cowrie/
    └── Cowrie installation
        └── var/log/cowrie/
            └── Honeypot logs
```

---

## 9. Result

The Ubuntu server was successfully prepared for Cowrie deployment with:

* A dedicated non-root `cowrie` user
* Updated Ubuntu packages
* A Python virtual environment
* Required Python tooling
* A dedicated Cowrie installation directory
* A separate location for Cowrie logs
* A controlled environment for running the honeypot

The server was then ready for **Cowrie installation and configuration**.
