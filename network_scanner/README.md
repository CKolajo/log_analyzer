#  Network Vulnerability Scanner

##  Project Overview
This project is a basic network vulnerability scanner designed to identify OPEN PORTS< RUNNING SERVICES< AND KNOWN VULNERABILITIES ON A TARGET MACHINE> It uses popular tools such as `nmap` and `nikto` to simulate the early stages of penetration testing (reconnaissance and enumeration).

## Tools Used
- 'nmap': For network scanning, port detection, service/version detection, and vulnerability scripts.
- 'nikto': For web server vulnerability scanning.
- 'bash' / 'python3': For automation and reporting

## Project Structure

network scanner/
scan_network.sh
run_nikto.sh
vulnerability_report.txt
README.md

## How to run

1. Nmap Scan
'''bash
sudo bash scan_network.sh 104.225.129.164
2. Nikto Scan (for web services)
bash run_nikto.sh http://104.225.129.164
3. View Results
cat vulnerability_report.txt

## What I learned
- How to use Nmap for service enumeration and vulnerblilty detection.
- How to run and interpret Nikto results.
- How to write a simple but useful vulnerability report.
- Importance of proper port management and patching web services.

## Future Improvments
- Automate report generation with python.
- Add OS detection and CVE lookups.
- Export results to JSON  or HTML  for better presentation.

## Author
Carrissa Kolajo- Aspiring RED TEAM \ Cybersecuity Analyst-in-Training
