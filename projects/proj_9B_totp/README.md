# Project 9B- TOTP 2FA Demo (Flask)

## What this is
A demo login flow protected by Time-based One-Time Passwords (TOTP) compatible with Google Authenticator/1Password/Authy.

## How to run
'''bash
python app.py
# open http://<server-ip>:5051
# 1) login with any user/pass
# 2) scan the QR code in your authenticator app
# 3) enter the 6-digitcode to enroll
# 4) then enter another 6-digit code to reach /home
