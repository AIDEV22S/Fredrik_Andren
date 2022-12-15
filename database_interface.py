import sqlite3


def insert_contact(firstname, lastname, address, postnumber, postaddress):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("INSERT INTO CONTACT_INFORMATION (FIRSTNAME,LASTNAME, ADDRESS, POSTNUMBER, POSTADDRESS) \
VALUES (?,?,?,?,?)", (firstname, lastname, address, postnumber, postaddress))
    conn.commit()
    conn.close()


def delete_contact_by_name(name):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("DELETE from CONTACT_INFORMATION where name = ?", (name,))
    conn.close()


def edit_address_by_name(name, address):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("UPDATE CONTACT_INFORMATION set ADDRESS = ? where NAME = ?", (name, address))
    conn.commit()
    conn.close()


def edit_phone_number_by_name(name, phone_number):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("UPDATE CONTACT_INFORMATION set ADDRESS = ? where NAME = ?", (name, phone_number))
    conn.close()


def retrieve_contacts():
    results = []
    conn = sqlite3.connect('contact_information.db')
    cursor = conn.execute("SELECT memberid, firstname, lastname, address, postnumber, postaddress from CONTACT_INFORMATION")
    # Contact records are tuples and need to be converted into an array
    for row in cursor:
        results.append(list(row))
    return results