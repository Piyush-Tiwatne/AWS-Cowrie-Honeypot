# Cowrie Installation

## 1. Overview

Cowrie is an open-source SSH and Telnet honeypot designed to monitor and log brute-force authentication attempts and shell interactions within an emulated environment.

In this project, Cowrie was installed on an Ubuntu Linux server running on AWS EC2.

---

## 2. Activate the Python Virtual Environment

The Python virtual environment created during the Linux setup was activated using:

```bash
source ~/cowrie-env/bin/activate
```

After activation, the terminal displayed:

```text
(cowrie-env)
```

The virtual environment was used to keep Cowrie's Python dependencies separated from the system Python installation.

---

## 3. Install Cowrie

The Cowrie source code was downloaded into the dedicated `cowrie` user's home directory.

The Cowrie project directory was:

```text
~/cowrie
```

The installation was performed using:

```bash
cd ~/cowrie
python -m pip install -e .
```

The `-e` option installs the project in editable mode, allowing the installed package to reference the source directory directly.

---

## 4. Dependency Issue

During the initial setup, installing Cowrie's development dependencies resulted in a build issue involving the `pytype` package.

The development dependencies were not required for running the honeypot itself.

Therefore, the base Cowrie package was installed using:

```bash
python -m pip install -e .
```

This installation completed successfully and provided the packages required to operate the honeypot.

---

## 5. Verify Cowrie Installation

After installation, the Cowrie command-line interface was tested using:

```bash
cowrie --help
```

The available commands included:

```text
init
start
stop
force-stop
restart
status
shell
bash
sh
```

The installed version was verified using:

```bash
cowrie --version
```

The project used:

```text
Cowrie 3.0.13
```

---

## 6. Installation Details

The final Cowrie environment consisted of:

| Component                  | Location / Configuration |
| -------------------------- | ------------------------ |
| Linux user                 | `cowrie`                 |
| Python virtual environment | `~/cowrie-env`           |
| Cowrie installation        | `~/cowrie`               |
| Cowrie version             | `3.0.13`                 |

Cowrie was operated using the dedicated non-root `cowrie` Linux user.

The Python virtual environment kept Cowrie's project-specific dependencies separate from the system Python environment.

---

## 7. Installation Verification

The installation was considered successful after confirming that:

* The Python virtual environment could be activated.
* The Cowrie package was installed successfully.
* The `cowrie` command was available.
* Cowrie CLI commands were accessible.
* The installed version was confirmed as **3.0.13**.

---

## 8. Result

Cowrie was successfully installed on the Ubuntu EC2 server and verified using its command-line interface.

The honeypot environment was ready for the next stage: **Cowrie configuration and SSH honeypot deployment**.
