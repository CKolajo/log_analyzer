import re
from collections import defaultdict

# Log file path
logfile = "/root/apache_logs.txt"

#Patterns for SQL injection
sql_injection_patterns = [
	r"' OR '1'='1",
	r"UNION SELECT",
	r"--"
	r"sleep\(",
	r "drop table",
	r " OR 1=1"
]

suspicious_ips = defaultdict(list)

with open(logfile,"r") as f:
  for line in f:
   for pattern in sql_injection_patterns:
    if re.search(pattern, line, re.IGNORECASE):
     ip = line.split(" ")[0]
     suspicious_ips[ip].append(line.strip())

if suspicious_ips:
  print("Suspicious IPs detected:")
  for ip, entries in suspicious_ips.items():
   print(f"\nIP: {ip}")
   for entry in entries:
     print(f" {entry}")

else:
  print("No suspicious SQL injection patterns found.")
