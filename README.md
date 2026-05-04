# MSSV: 24120454
# Họ và tên: Huỳnh Trần Phước Thiện
# Project: Firebase & AI Note-Taking App

A comprehensive note-taking application built with **FastAPI** (Backend) and **Streamlit** (Frontend), featuring **Firebase Authentication**, **Firestore** database integration, and AI capabilities powered by **AI Services**.

## 🚀 Features

* **User Authentication**: Secure login and signup system powered by Firebase Auth.
* **Note Management (CRUD)**: Create, read, update, and delete notes stored in Firebase Firestore.
* **AI Integration**: Enhance your notes with AI Services.
* **Two-Tier Architecture**: Clean separation of concerns with a FastAPI backend and a Streamlit frontend.
* **RESTful API**: Comprehensive API endpoints for authentication and note management.

## 🧰 Tech Stack

**Backend:**
* Python 3.x
* FastAPI
* Firebase Admin SDK (Auth & Firestore)
* AI Services (e.g., Google GenAI)

**Frontend:**
* Streamlit
* Requests (API Client)

## 📁 Project Structure

```
├── backend/
│   └── app/
│       ├── core/          # Firebase and App Configurations
│       ├── dependencies/  # FastAPI Dependencies (e.g., Auth)
│       ├── routers/       # API Routes (Auth, Notes)
│       ├── schemas/       # Pydantic Models for Data Validation
│       ├── services/      # Business Logic (Firestore, AI Services)
│       └── main.py        # FastAPI Application Entry Point
├── frontend/
│   ├── app.py             # Streamlit Application
│   └── api_client.py      # HTTP Client to communicate with Backend
├── requirements.txt       # Project Dependencies
└── README.md              # Project Documentation
```

## ⚙️ Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/Thienhappy/24120454-Firebase.git
cd <your-repo-directory>
```

2. **Set up a Virtual Environment (Recommended):**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
pip install fastapi 
pip install uvicorn 
pip install pydantic[email]

```

4. **Firebase Setup (Console):**
* Create a Firebase project in the [Firebase Console](https://console.firebase.google.com/).
* Enable Authentication (e.g., Email/Password, Google).
* Enable Firestore Database and Realtime Database.


5. **Credentials & Secrets Setup:**
* **Environment Variables:** 
    Rename `.env.example` to `.env` and fill in your Gemini API key before running the application.

* **Firebase Admin SDK Setup (Backend):**
    1. Go to your [Firebase Console](https://console.firebase.google.com/) > **Project settings** > **Service accounts**.
    2. Click **Generate new private key** to download the `.json` file.
    3. **Note:** You only need this file to copy its content. You can delete it after completing the Streamlit setup below.

* **Google OAuth 2.0 Setup (For Google Login):**
    1. Go to the [Google Cloud Console](https://console.cloud.google.com/) and select the project that was automatically created when you made your Firebase project.
    2. Navigate to **APIs & Services** > **Credentials**.
    3. Click **+ CREATE CREDENTIALS** and select **OAuth client ID**.
    4. Choose **Web application** as the Application type.
    5. Under **Authorized redirect URIs**, add exactly this URL: `http://localhost:8000/auth/google/callback`
    6. Click **Create**. A popup will appear containing your **Client ID** and **Client Secret**. Keep this tab open for the next step.

* **Streamlit Secrets Setup (Frontend):**
    1. Create a `.streamlit` directory and a `secrets.toml` file in the root of your project:
       ```bash
       mkdir .streamlit
       touch .streamlit/secrets.toml
       ```
    2. Add the following content to `secrets.toml` and fill in the necessary Firebase and Google Login credentials:
       ```toml
       [firebase_client]
            # You can find this in Firebase Console > Project settings > General > Your apps > Web app configuration
            # apiKey = "..."
            # authDomain = "..."
            # databaseURL = "..."
            # projectId = "..."
            # storageBucket = "..."
            # messagingSenderId = "..."
            # appId = "..."

       [firebase_admin]
            # Extract the values from your downloaded Service Account .json file
            # type = "service_account"
            # project_id = "your-project-id"
            # private_key_id = "..."
            # private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
            # client_email = "..."
            # client_id = "..."
            # auth_uri = "https://..."
            # token_uri = "https://..."
            # auth_provider_x509_cert_url = "https://..."
            # client_x509_cert_url = "..."

       [google-login]
            # Fill in the Google OAuth 2.0 credentials you obtained from the Google Cloud Console
            # google-url = "http://localhost:8000/auth/google/start"
            # google_client_id = "..." 
            # google_client_secret = "..."
            # google_redirect_uri = "http://localhost:8000/auth/google/callback"
            # firebase_web_api_key = "..."
            # frontend_url = "http://localhost:8501"
            # cookie_secure = false
       ```
* **⚠️ IMPORTANT SECURITY NOTE:** Never commit your `.env`, `firebase-credentials.json`, or `.streamlit/secrets.toml` files to version control. Make sure all of them are added to your `.gitignore` file to protect your sensitive credentials.


## ▶️ Running the Application

**1. Start the FastAPI Backend:**
```bash
uvicorn backend.app.main:app --reload --port 8000
```
The API will be available at `http://localhost:8000`. You can view the API documentation at `http://localhost:8000/docs`.

**2. Start the Streamlit Frontend:**
Open a new terminal, activate your virtual environment, and run:
```bash
streamlit run frontend/app.py
```
The Streamlit interface will open in your browser, typically at `http://localhost:8501`.

## 🎥 Video Demo
https://drive.google.com/drive/folders/1eRINZEdt83eh2dPKnlfVW6dogOqpI8nW?usp=drive_link




