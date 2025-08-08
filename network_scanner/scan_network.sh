#!/bin/bash
# Scan the local network for live hosts and open ports
echo "[+] Starting Nmap network scan..."

nmap -sS T4 -p 1-1000 104.225.129.164/24 -oN nmap_scan_results.txt

echo "[+] Nmap sscan complete. Results saved to nmap_scan_results.txt"
