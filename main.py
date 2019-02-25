import db_functions as db

import config as c


list_of_contacts = [('Khadijah', 'Hinesley', 'Facebook'),
                    ('Marcene', 'Babiarz', 'Google'),
                    ('Janyce', 'Wilcoxson', 'Amazon'),
                    ('Natisha', 'Shockley', 'Microsoft'),
                    ('Annmarie', 'Fester', 'Ebay')]

# db.add_multiple_records_to_contact_details(list_of_contacts)


# new_list = list(range(66, 71))
# print(new_list)

# db.delete_multiple_records_from_contact_details(new_list)

# db.truncate_table(c.mysql_table_contact_details)


# print(db.select_all(c.mysql_table_contact_details))

print(type(list_of_contacts[0]))
