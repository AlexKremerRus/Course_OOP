import random

from dataclasses import dataclass

type_document = ["passport", "driving license", "bioPassport"]

@dataclass
class DocumentDataStorage:
    type= []
    number= []
    organisation= []
    date= []

class Document:
    def __init__(self, type, number, organisation, date):
        self.type = type
        self.number = number
        self.organisation = organisation
        self.date = date

    def __str__(self):
        return f"Type: {self.type} with number: {self.number}; Organisqtion: {self.organisation}; Date: {self.date}"


class SaveDocuments:
    def __init__(self, type, number, organisation, date, storage):
        self.storage = storage
        self.type_index = self.get_index_from_storage(type, self.storage.type)
        self.type_index = self.get_index_from_storage(number, self.storage.number)
        self.type_index = self.get_index_from_storage(organisation, self.storage.organisation)
        self.type_index = self.get_index_from_storage(date, self.storage.date)


    def get_index_from_storage(self, search_valiable, storage_savef_attr):
        if search_valiable in storage_savef_attr:
            return storage_savef_attr.index(search_valiable)
        else:
            storage_savef_attr.append(search_valiable)
            return len(storage_savef_attr) - 1

    def __str__(self) -> str:
        return f"Type: {self.storage.type}; Number: {self.storage.number}; Organisation: {self.storage.organisation}; Date: {self.storage.date}"

if __name__ == "__main__":
    data_storage = DocumentDataStorage()

    documents = [
        Document(type=random.choice(type_document), number = random.randint(100,999), organisation = 'Test', date = '11.11.2222')
        for _ in range(random.randint(1, 10))
    ]
    saving_documents = [
        SaveDocuments(type=random.choice(type_document), number = random.randint(100,999), organisation = 'Test', date = '11.11.2222', storage=data_storage)
        for _ in range(random.randint(1, 10))
    ]

    result = f"Type: {len(data_storage.type)} \n" + \
    f"Number : {len(data_storage.number)} \n" + \
    f"Organisation: {len(data_storage.organisation)} \n"+ \
    f"Date: {data_storage.date}"
    print(result)