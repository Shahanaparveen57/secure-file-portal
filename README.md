name: Secure File Portal
description: >
  A secure file upload and download portal built with Python Flask and AES encryption, 
  designed for safe file handling and storage.

features:
  - AES-CBC encryption for all uploaded files
  - Random IV per file for enhanced security
  - Admin login with bcrypt-hashed password
  - Multiple file upload with real-time progress bar
  - Per-user folder storage to isolate files
  - Download files with automatic decryption
  - Clean and user-friendly interface

installation:
  - step: Clone repository
    command: git clone <your-repo-url>
  - step: Navigate to folder
    command: cd secure-file-portal
  - step: Create virtual environment
    command: python -m venv venv
  - step: Activate virtual environment
    command: venv\Scripts\activate
  - step: Install dependencies
    command: pip install -r requirements.txt
  - step: Configure environment variables
    instructions: Copy .env.example to .env and update AES_KEY, ADMIN_USER, ADMIN_PASS

usage:
  - step: Run Flask app
    command: python app.py
  - step: Open browser
    url: http://127.0.0.1:5000/
  - step: Login
    credentials:
      username: admin
      password: Admin123
  - step: Upload files securely
  - step: Download decrypted files

security_overview:
  encryption:
    type: AES-CBC
    key_length: 16 bytes
    iv: Random per file
  passwords:
    hashed: bcrypt
  file_handling:
    temp_files_deleted: true
    per_user_folders: true
  key_management:
    location: .env
    hardcoded: false

dependencies:
  - Flask
  - PyCryptodome
  - python-dotenv
  - bcrypt

