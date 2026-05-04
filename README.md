# Firebase & Ollama Note-Taking App

A comprehensive note-taking application built with **FastAPI** (Backend) and **Streamlit** (Frontend), featuring **Firebase Authentication**, **Firestore** database integration, and AI capabilities powered by **Ollama**.

## 🚀 Features

* **User Authentication**: Secure login and signup system powered by Firebase Auth.
* **Note Management (CRUD)**: Create, read, update, and delete notes stored in Firebase Firestore.
* **AI Integration**: Enhance your notes with AI using Ollama.
* **Two-Tier Architecture**: Clean separation of concerns with a FastAPI backend and a Streamlit frontend.
* **RESTful API**: Comprehensive API endpoints for authentication and note management.

## 🧰 Tech Stack

**Backend:**
* Python 3.x
* FastAPI
* Firebase Admin SDK (Auth & Firestore)
* Ollama (AI Services)

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
│       ├── services/      # Business Logic (Firestore, Ollama)
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
pip install fastapi uvicorn pydantic[email]

```

4. **Environment Variables & Firebase Setup:**
* Please rename `.env.example` to `.env` and fill in your Gemini API key before running the application.
* Create a Firebase project in the [Firebase Console](https://console.firebase.google.com/).
* Enable Authentication, Firestore and Realtime Database.
* Download your Firebase Admin SDK service account key (`.json` file) and configure the path in your `backend` configurations.

## ▶️ Running the Application

**1. Start the FastAPI Backend:**
```bash
cd backend
uvicorn backend.app.main:app --reload --port 8000
```
The API will be available at `http://localhost:8000`. You can view the API documentation at `http://localhost:8000/docs`.

**2. Start the Streamlit Frontend:**
Open a new terminal, activate your virtual environment, and run:
```bash
cd frontend
streamlit run frontend/app.py
```
The Streamlit interface will open in your browser, typically at `http://localhost:8501`.

## 🎥 Video Demo




