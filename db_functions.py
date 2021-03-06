import config as c
import list_functions as lf


# Function adds a single record to contact_details table.
def add_a_record_to_contact_details(f_name, l_name, c_name):
    c.mysql_cursor.execute("INSERT INTO contact_details (first_name, last_name, company_name) "
                        "VALUES ('{}', '{}', '{}');"
                           .format(f_name, l_name, c_name))
    c.mysql_database_connection.commit()


# Function adds a list of records to contact_details table.
def add_multiple_records_to_contact_details(list_of_data):
    c.mysql_cursor.executemany("INSERT INTO contact_details (first_name, last_name, company_name) "
                        "VALUES (%s, %s, %s);", list_of_data)
    c.mysql_database_connection.commit()


# Function updates a single record in contact_details table using primary key.
def update_contact_details(f_name, l_name, c_name, p_key):
    c.mysql_cursor.execute("UPDATE contact_details "
                        "SET "
                            "first_name = '{}', "
                            "last_name = '{}' , " 
                            "company_name = '{}' "
                        "WHERE "
                        "primary_key = {};"
                           .format(f_name, l_name, c_name, p_key))
    c.mysql_database_connection.commit()


# Functions Truncates table.
def truncate_table(table_name):
    c.mysql_cursor.execute("TRUNCATE TABLE {};"
                           .format(table_name))
    c.mysql_database_connection.commit()

# Function deletes a single row using a primary key.
def delete_a_record_from_contact_details(p_key):
    c.mysql_cursor.execute("DELETE FROM contact_details "
                        "WHERE "
                             "primary_key = {};"
                           .format(p_key))
    c.mysql_database_connection.commit()


# Function deletes a list of rows using a primary key.
def delete_multiple_records_from_contact_details(list_of_ids):

    # Transform original list into a list of tuples. From [1, 2, 3] to [(1,), (2,), (3,)]
    new_list = lf.create_list_of_tuples(list_of_ids)

    # Run SQL delete query.
    c.mysql_cursor.executemany("DELETE FROM contact_details "
                            "WHERE "
                                "primary_key = %s", new_list)
    c.mysql_database_connection.commit()


# Function returns all data from a given table.
def select_all(table_name):
    c.mysql_cursor.execute("SELECT * FROM {};"
                           .format(table_name))
    my_result = c.mysql_cursor.fetchall()
    return my_result
