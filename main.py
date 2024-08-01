
from pprint import pprint
import csv
import re
# читаем адресную книгу в формате CSV в список contacts_list

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
def normalize_names(contacts):
    for contact in contacts:
        full_name = " ".join(contact[:3]).split()
        while len(full_name) < 3:
            full_name.append('')
        contact[:3] = full_name
    return contacts

contacts_list = normalize_names(contacts_list)

def normalize_phone_numbers(contacts):
    phone_pattern = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?\s*[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})(\s*(доб\.)\s*(\d+))?')
    formatted_contacts = []
    for contact in contacts:
        phone = contact[5]
        formatted_phone = phone_pattern.sub(r'+7(\2)\3-\4-\5\6', phone)
        contact[5] = formatted_phone
        formatted_contacts.append(contact)
    return formatted_contacts

contacts_list = normalize_phone_numbers(contacts_list)

def merge_contacts(contacts):
    merged_contacts = {}
    for contact in contacts:
        key = (contact[0], contact[1])  # Ключ - это фамилия и имя
        if key in merged_contacts:
            existing_contact = merged_contacts[key]
            for i in range(len(contact)):
                if not existing_contact[i]:
                    existing_contact[i] = contact[i]
        else:
            merged_contacts[key] = contact
    return list(merged_contacts.values())

contacts_list = merge_contacts(contacts_list)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)