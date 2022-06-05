#python GetAllDataFromAPIForUpload.py id
#customize de acordo com a api que irá utilizar
import json, sys, cloudscraper # cloudscraper bypassing cloudflare anti-bot
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

#upload api info
filename = "get_info_from_api/%s.json" % (sys.argv[1])
bucket = storage.bucket()
blob = bucket.blob(filename)
print(filename)
if blob.exists():
    print("Já catalogado")
    print("Publicado:", blob.public_url)
else:
    #get api info
    all_directories = ['/profile', '/info']
    info = {}
    url = "https://site-demo.com/v1/user/%s" % (sys.argv[1])
    for item in all_directories:
        scraper = cloudscraper.create_scraper()
        get_info = url + item
        print(get_info)
        data = scraper.get(get_info, headers={'authorization': 'Bearer abcb0s787d6af7demo86887fds7sfsf'}).json()
        info = {**info, **data['user']}
    file = json.dumps(info, sort_keys = False, indent = 4, ensure_ascii = False)
    blob.upload_from_string(file, content_type='application/json')
    blob.make_public()
    print("Publicado:", blob.public_url)
