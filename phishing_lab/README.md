# Simulated Phishing Campaign Lab

This project is a **safe and ethical simulation** of a phishing campign to understand how credential harvesting attacks work. It is part of a red team learning exercise and not intended for malicious use.

## Disclaimer
This project is for **educational purposes only**. Never deploy or use it outside of a controlled lab environment.

## how IT Works

1. A user visits a fake login page.
2. When they submit credentials:
- The data is logged to 'captured.txt'.
- A timestamp is included.
3. Optionally, the user can be redirected to a real login page (like Google).

# Features Implemented
- Credential capture with timestamp
- Flask app with fake login form
- Captured data saved to a text file

## Optional Enhancements
- Timestamp formatting (Implemented)
- Redirect to a real site
- IP and User-Agent logging

## How to Run
'''bash
python3 phish_app.py
Then open the sit in your browser (usually http://localhost:5000) and test it.

# Security Reminder
This is not a real attack. All actions are done in a private, educational lab.

## Learning Goals
- Understand the structure of phishing campaigns
- Practice web form handling in Flask
- Learn how credentials can be exfiltrated by attackers
