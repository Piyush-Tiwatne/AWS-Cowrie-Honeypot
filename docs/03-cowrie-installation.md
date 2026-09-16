# Cowrie Installation

## Overview

Cowrie is an open-source SSH and Telnet honeypot designed to log
brute-force attempts and shell interaction performed by attackers.

In this project, Cowrie was installed on an Ubuntu EC2 instance.

## 1. Activate the Python Virtual Environment

The Cowrie environment was activated using:


source ~/cowrie-env/bin/activate

After activation, the terminal displayed:

(cowrie-env)

This keeps Cowrie's Python dependencies separated from the system
Python installation.

##2. Install Cowrie

The Cowrie source code was downloaded into the cowrie user's home
directory.

The project directory was:

~/cowrie

Cowrie was installed using:

cd ~/cowrie
python -m pip install -e .

##3. Dependency Issue

During installation, installing the development dependencies caused
a build issue involving the pytype package.

Since the development dependencies were not required to run the
honeypot, the base Cowrie package was installed instead:

python -m pip install -e .

This allowed Cowrie to run successfully.

##4. Verify Cowrie Installation

The Cowrie command-line interface was checked using:

cowrie --help

The available commands included:

init
start
stop
force-stop
restart
status
shell
bash
sh

The installed Cowrie version was:

cowrie --version

The project used Cowrie version:

3.0.13

##5. Important Installation Details

Cowrie was operated using the dedicated non-root cowrie Linux user.

The Python virtual environment was:

~/cowrie-env

The Cowrie installation directory was:

~/cowrie

This setup helped keep the honeypot environment isolated from the
system Python installation.

Result

Cowrie was successfully installed on the Ubuntu EC2 server and was
ready for configuration and deployment as an SSH honeypot.