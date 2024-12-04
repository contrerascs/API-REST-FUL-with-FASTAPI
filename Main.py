from fastapi import FastAPI, HTTPException
from src.lib.managedb import ManageDb
from pydantic import BaseModel
from uuid import uuid4 as uuid
#uvicorn Main:app --reload

app = FastAPI()
md = ManageDb()

class ContactModel(BaseModel):
    id: str = str(uuid())
    name: str
    phone: str    

@app.get('/')
def root():
    return {'message': 'Hi, i am FastAPI'}

@app.get('/api/contacts')
def get_all_contacts():
    return md.read_contacts()

@app.get('/api/contacts/{id_contact}')
def get_single_contact(id_contact:str):
    contacts = md.read_contacts()

    for contact in contacts:
        if contact['id'] == id_contact:
            return contact
    raise HTTPException(status_code=404, detail='Contact not found')

@app.post('/api/contacts')
def add_contact(new_contact:ContactModel):
    contacts = md.read_contacts()
    new_contact = new_contact.model_dump()

    contacts.append(new_contact)

    md.write_contacts(contacts)

    return {
        'success': True,
        'message': 'Add new contact'
    }