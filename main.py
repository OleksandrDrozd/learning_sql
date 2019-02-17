import db_functions as db


list_of_contacts = [('Khadijah', 'Hinesley', 'Facebook'),
                    ('Marcene', 'Babiarz', 'Google'),
                    ('Janyce', 'Wilcoxson', 'Amazon'),
                    ('Natisha', 'Shockley', 'Microsoft'),
                    ('Annmarie', 'Fester', 'Ebay')]

db.add_multiple_records_to_contact_details(list_of_contacts)


new_list = list(range(46, 51))
print(new_list)

db.delete_multiple_records_from_contact_details(new_list)


print(db.select_all_contacts())
