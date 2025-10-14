Secure File Portal

A secure file upload and download portal built with Python Flask and AES encryption, designed for safe file handling and storage.

Features

AES-CBC encryption for all uploaded files

Random IV per file for enhanced security

Admin login with bcrypt-hashed password

Multiple file upload with real-time progress bar

Per-user folder storage to isolate files

Download files with automatic decryption

Clean and user-friendly interface

Installation

Clone the repository:

git clone <your-repo-url>
cd secure-file-portal


Create a virtual environment and activate:

python -m venv venv
venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Copy .env.example to .env and update:

AES_KEY=Your16CharKeyHere
ADMIN_USER=admin
ADMIN_PASS=Admin123

Usage
python app.py


Open your browser at:

http://127.0.0.1:5000/


Login with your admin credentials

Upload files securely

Download decrypted files

Security Overview

Encryption: AES-CBC, 16-byte key, unique random IV per file

Passwords: Hashed with bcrypt

File Handling: Temporary files deleted after use, per-user folders

Key Management: Stored in .env, not hardcoded

See SecurityOverview.md for full details.

Dependencies

Flask

PyCryptodome

python-dotenv

bcrypt
