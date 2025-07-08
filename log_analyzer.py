import re
from collections import defaultdict

# ===== CONFIGURATION =====

logfile = "/root/apache_logs.txt"

sql_injection_patterns = [
	r"' OR '1'='1",
	r"UNION SELECT",
	r"--",
	r"drop table",
	r"sleep\(",
	r" or 1=1"
]
# Thresholds
BRUTE_FORCE_THRESHOLD = 10
HIGH_TRAFFIC_THRESHOLD = 100
# ===== DATA STRUCTURES =====
suspicious_ips = defaultdict(list)
login_attempts = defaultdict(int)
request_count = defaultdict(int)

# ===== READ THE LOG FILE =====

with open(logfile, "r") as f:
  for line in f:
   ip= line.split(" ")[0]
   request_count[ip] +=1

# Check for SQL injection patterns
for pattern in sql_injection_patterns:
  if re.search(pattern, line,  re.IGNORECASE):
   suspicious_ips[ip].append(f"SQL Injectioin attempt: {line.strip()}")

#Check for brute force patterns
if"Post/login" in line or "GET/login" in line:
  login_attempts[ip] +=1

# ===== ANALYZE RESULTS =====

# Save to report
report = []

report.append("====LOG ANALYSIS REPORT ====\n")

#Suspicious SWL Injection attempts
if suspicious_ips:
  report.append("Suspicious SQL Injection attempts detected:\n")
  for ip, entries in suspicious_ips.items():
    report.append(f"IP: {ip}")
    for entry in entries:
      report.append(f" {entry}")
    report.append(" ")
else:
  report.append("No SQL injection patterns found. \n")

# Brute force detection
report.append("Brute Force Attempts:\n")
for ip, count in login_attempts.items():
  if count > BRUTE_FORCE_THRESHOLD:
    report.append(f" {ip} attempted {count} logins")

if not any(count > BRUTE_FORCE_THRESHOLD for count in login_attempts.values()):
  report.append("NO brute force activity detected.\n")

# High traffic detection
report.append("\nHigh Request Volumn:\n")
for ip, count in request_count.items():
  if count > HIGH_TRAFFIC_THRESHOLD:
   report.append(f" {ip} made {count} request")

if not any(count > HIGH_TRAFFIC_THRESHOLD for count in request_count.values()):
  report.append("NO high traffic IPs detected.\n")

# Save the request
with open("analysis_report.txt", "w") as f:
  for line in report:
   f.write(line + "\n")

print("Analysis complete. See 'analysis_report.txt' for results.")
