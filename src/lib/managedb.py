import pathlib
import json

class ManageDb:
    __address_file__ = "{0}/src/db/dbContacts.json".format(pathlib.Path().absolute())

    def read_contacts(self):
        with open(self.__address_file__, "r") as data:
            return json.loads(data.read())