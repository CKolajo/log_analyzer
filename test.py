logfile = "/root/apache_logs.txt" #adjust this path

with open(logfile, "r") as f:
 for i, line in enumerate(f):
  if i < 5:
   print(line.strip())
