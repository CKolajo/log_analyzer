#!/bin/bash
echo "[+] Starting Nikto scan..."

# replace with your target IP or domain (use localhost:80 if testing loccally)
TARGET= "http://127.0.0.1"

nikto -h $TARGET -output nikto_scan_results.txt

echo "[+] Nikto scan complete. Results saved to nikto_scan_results.txt"
