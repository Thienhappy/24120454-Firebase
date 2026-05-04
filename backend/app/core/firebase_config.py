import os
import json
import pyrebase
import firebase_admin
import streamlit as st

from firebase_admin import credentials, firestore

def get_pyrebase_auth():
    # Streamlit secrets sometimes has issues with keys, ensure explicit dict and casing
    firebase_cfg = {
        "apiKey": st.secrets["firebase_client"]["apiKey"],
        "authDomain": st.secrets["firebase_client"]["authDomain"],
        "projectId": st.secrets["firebase_client"]["projectId"],
        "storageBucket": st.secrets["firebase_client"]["storageBucket"],
        "messagingSenderId": st.secrets["firebase_client"]["messagingSenderId"],
        "appId": st.secrets["firebase_client"]["appId"],
        "databaseURL": st.secrets["firebase_client"]["databaseURL"]
    }
    firebase_app = pyrebase.initialize_app(firebase_cfg)
    return firebase_app.auth()

def init_firebase_admin():
    if not firebase_admin._apps:
        cred_dict = dict(st.secrets["firebase_admin"])
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)

def get_firestore():
    init_firebase_admin()
    return firestore.client()