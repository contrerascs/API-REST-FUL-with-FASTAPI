from src.lib.managedb import ManageDb
from fastapi import HTTPException

def delete_contacts(id_contact):
    md = ManageDb()
    contacts = md.read_contacts()

    for index,contact in enumerate(contacts):
        print('hi')
        if contact['id'] == id_contact:
            contacts.pop(index)
            
            md.write_contacts(contacts)

            return {
                'success': True,
                'message': 'Delete contact'
            }
        
    raise HTTPException(status_code=404, detail='Contact not found')