#python FirebaseUploadOnlyFile demo.txt
import os, json, sys
import firebase_admin
from firebase_admin import credentials, storage

PROJECT_ID = 'app-demo'
IS_EXTERNAL_PLATFORM = True # False if using Cloud Functions
firebase_app = None

def init_firebase():
    global firebase_app
    if firebase_app:
        return firebase_app
    if IS_EXTERNAL_PLATFORM:
        cred = credentials.Certificate('firebase-adminsdk.json')
    else:
        cred = credentials.ApplicationDefault()

    firebase_app = firebase_admin.initialize_app(cred, {
        'storageBucket': f"{PROJECT_ID}.appspot.com"
    })

    return firebase_app

init_firebase()
bucket = storage.bucket()
blob = bucket.blob(sys.argv[1])
blob.upload_from_filename(sys.argv[1])
