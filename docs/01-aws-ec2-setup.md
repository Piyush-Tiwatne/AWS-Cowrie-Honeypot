\# AWS EC2 Setup



\## Objective



The first step of the project was to deploy an Ubuntu Linux server on

AWS EC2 that would host the Cowrie SSH honeypot.



\## EC2 Configuration



The project used:



\- AWS EC2

\- Ubuntu Linux

\- AWS Security Groups

\- SSH

\- EC2 key pair authentication



The EC2 instance was deployed in the AWS Mumbai region.



\## Security Group Configuration



The EC2 Security Group was configured to control inbound network

traffic to the instance.



The main rules were:



| Protocol | Port | Purpose |



| TCP | 22 | Administrative SSH access |

| TCP | 2222 | Cowrie SSH honeypot |



Port 22 was used for administrative access to the Ubuntu server.



Port 2222 was used by Cowrie to receive SSH connections for the

honeypot.



\## Why Use Separate Ports?



The actual administrative SSH service and the Cowrie honeypot were

kept separate.



\- Port 22 → real SSH access to administer the server

\- Port 2222 → Cowrie honeypot



This separation made it possible to administer the server while

monitoring activity directed at the honeypot.



\## SSH Access



The EC2 instance was accessed using the AWS EC2 key pair.



Example:



ssh -i <key-file>.pem ubuntu@<EC2-PUBLIC-IP>



\## Security Considerations



The EC2 instance was used specifically for the honeypot project.



The following practices were used:



Separate administrative SSH access from the honeypot service.

Run Cowrie under a dedicated non-root Linux user.

Keep private SSH keys outside the repository.

Use AWS Security Group rules to control network access.

Monitor the instance and collected logs during the project.

Result



An Ubuntu EC2 server was successfully deployed and prepared to host

the Cowrie SSH honeypot.

