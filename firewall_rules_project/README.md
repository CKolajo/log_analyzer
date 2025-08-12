# FIrewall Rules Project

This project involes configuring and testing basic firewall rules using UFW (Uncomplicated Firewall) on Ubuntu. The goal is to understand how firewalls control incoming and outgoing network traffic, and how to apply rules safely in a real-world environment.

## Objectives:
 - Enable and confige UFW
- Allow specific ports (e.g., SSH, HTTP)
- Deny all other incoming connections
- Test the rules using 'curl', ping', and 'nmap'

## What I configured
- Enabled UFW with safe defaults (deny incoming, allow outgoing)
- Allowed SSH, HTTP, HTTPS
- Restricted SSH to my public IP only
- Enabled logging (low)
- Installed and configured Fail2ban (sshd jail)
- Linked Fail2ban - UFW and added custom ban.unban logging to /var/log/fail2ban-custom.log

## Test commands I used
sudo ufw status numbered
sudo tail -f /var/log/ufw.log
sudo fail2ban-client status sshd
sudo fail2ban-client set sshd banip <TEST_IP>
cat /var/log/fail2ban-custom.log
