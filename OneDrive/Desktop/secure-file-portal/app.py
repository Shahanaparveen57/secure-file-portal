from flask import Flask, request, render_template, redirect, url_for, session, send_file
import os, datetime, bcrypt
from crypto_utils import encrypt_file, decrypt_file
from dotenv import load_dotenv

load_dotenv()
ADMIN_USER = os.getenv("ADMIN_USER")
ADMIN_PASS = os.getenv("ADMIN_PASS").encode()  # plain text from env

app = Flask(__name__)
app.secret_key = os.urandom(24)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Hash admin password on startup
hashed_password = bcrypt.hashpw(ADMIN_PASS, bcrypt.gensalt())

def get_unique_filename(filename, user_folder):
    file_path = os.path.join(user_folder, filename)
    if os.path.exists(file_path):
        base, ext = os.path.splitext(filename)
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{base}_{timestamp}{ext}"
    return filename

def get_user_folder(username):
    folder = os.path.join(UPLOAD_FOLDER, username)
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode()
        if username == ADMIN_USER and bcrypt.checkpw(password, hashed_password):
            session['user'] = username
            return redirect(url_for('home'))
        return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    user_folder = get_user_folder(session['user'])
    files = os.listdir(user_folder)
    message = request.args.get('message')
    return render_template('index.html', files=files, message=message)

@app.route('/upload', methods=['POST'])
def upload():
    if 'user' not in session:
        return redirect(url_for('login'))
    user_folder = get_user_folder(session['user'])

    if 'file' not in request.files:
        return redirect(url_for('home', message="No file part"))

    files = request.files.getlist('file')
    if not files or files[0].filename == '':
        return redirect(url_for('home', message="No selected file"))

    uploaded_files = []
    for file in files:
        filename = get_unique_filename(file.filename, user_folder)
        file_path = os.path.join(user_folder, filename)
        file.save(file_path + ".tmp")
        encrypt_file(file_path + ".tmp", file_path)
        os.remove(file_path + ".tmp")
        uploaded_files.append(filename)

    return redirect(url_for('home', message=f"Uploaded successfully: {', '.join(uploaded_files)}"))

@app.route('/download/<filename>')
def download(filename):
    if 'user' not in session:
        return redirect(url_for('login'))
    user_folder = get_user_folder(session['user'])
    file_path = os.path.join(user_folder, filename)
    temp_path = file_path + ".dec"
    decrypt_file(file_path, temp_path)
    return send_file(temp_path, as_attachment=True)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
