\# Linux Setup



\## Objective



After creating the AWS EC2 instance, the Ubuntu server was prepared

to run Cowrie in an isolated and controlled manner.



\## System Update



The Ubuntu package lists were updated before installing the required

software.



sudo apt update

sudo apt upgrade -y





\##Dedicated Cowrie User



\#A separate Linux user was created for running Cowrie.



sudo adduser cowrie



The Cowrie honeypot was operated using this account instead of the

root account.



Why Use a Separate User?



Running the honeypot under a dedicated non-root user follows the

principle of least privilege.



If the honeypot process encounters a security issue, limiting its

permissions can reduce the potential impact on the underlying system.



\##Switch to the Cowrie User

su - cowrie



The Cowrie user was then used for the honeypot installation and

operation.



\##Python Virtual Environment



A Python virtual environment was created for the Cowrie installation.



python3 -m venv cowrie-env

source cowrie-env/bin/activate



The virtual environment keeps project-specific Python packages

separate from the system Python environment.



After activation, the terminal displayed:



(cowrie-env)

Python and Package Installation



Required Python packages were installed inside the virtual environment.



Example:



python -m pip install --upgrade pip



Cowrie was then installed according to its project requirements.



Directory Structure



The main Cowrie directory was located under the dedicated user's

home directory:



/home/cowrie/cowrie/



Cowrie logs were stored under:



/home/cowrie/cowrie/var/log/cowrie/

Result



The Ubuntu server was prepared with:



A dedicated non-root cowrie user

A Python virtual environment

Required Python tooling

A separate directory for the Cowrie installation

A controlled environment for running the honeypot

