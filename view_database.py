import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('C:/PROJECTS/Quiz App/quizapp-7bc35-firebase-adminsdk-4denh-cb7f1c9dab.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def view_collection(collection_name):
    try:
        collection_ref = db.collection(collection_name)
        docs = collection_ref.stream()
        
        for doc in docs:
            print(f'Document ID: {doc.id}')
            print(f'Document Data: {doc.to_dict()}')
            print('---')
    
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    view_collection('user_responses')
