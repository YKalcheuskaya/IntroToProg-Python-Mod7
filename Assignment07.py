# ------------------------------------------------- #
# Title: Assignment07
# Description: A simple example of storing data in a binary file with exceptions handling
# ChangeLog: (Who, When, What)
# YKalch,3.5.2022,Created the script using the provided template
# YKalch,3.5.2022,Complete the code to save & read customer's data to a binary file
# ------------------------------------------------- #

import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
str_file_name = 'AppData.dat'
lst_customer = []


# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    """ Save customer data to the binary file

    :param file_name: (string) with name of file:
    :param list_of_data: (list) customer list:
    :return: (boolean) if the data was saved successfully or not
    """

    # Adding exception handling for scenario when the file does not exist
    try:
        # Creating/opening the file in write binary mode
        file = open(file_name, "wb")

        # Writing the data from the file
        pickle.dump(list_of_data, file)

        # The file has been saved successfully
        return True
    except Exception as ex:
        print("Failed to read the customers data from the file!")
        print(ex)
        print(type(ex))
        print(ex.__doc__)
        print(ex.__str__())

    # Failed to save the file
    return False


def read_data_from_file(file_name):
    """ Reads data from a file into a list

    :param file_name: (string) with name of file:
    :return: (list) of customers
    """

    # Adding exception handling for scenario when the file does not exist
    try:
        # Opening the file in read binary mode
        file = open(file_name, "rb")

        # Reading the data from the file
        list_customers = pickle.load(file)
    except FileNotFoundError:
        print(file_name + " does not exist!")
    except Exception as ex:
        print("Failed to read the customers data from the file!")
        print(ex)
        print(type(ex))
        print(ex.__doc__)
        print(ex.__str__())

    return list_customers


# Presentation ------------------------------------ #
str_user_id = str(input("Enter user ID: "))
str_user_name = str(input("Enter user name: "))

row = {"ID": str(str_user_id).strip(), "Name": str(str_user_name).strip()}
lst_customer.append(row)

print("Saving customer's data to '{}' file...".format(str_file_name))
bool_result = save_data_to_file(str_file_name, lst_customer)

print("Result of the save operation: {}".format(bool_result))

try:
    print("Reading the customer's data to a new list object...")
    fresh_lst_customer = read_data_from_file(str_file_name)

    print("Read values: ID = {}, name = {}".format(fresh_lst_customer[0]['ID'], fresh_lst_customer[0]['Name']))
except:
    print("Failed to read customer's data!")
