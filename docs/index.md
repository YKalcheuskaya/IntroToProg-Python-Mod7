# Assignment07 Module

In this module I've learned how to work with [binary files](https://docs.python.org/3/library/pickle.html) and [exception handling](https://docs.python.org/3/tutorial/errors.html).

## Saving data to a binary file

Here is a code snippet to save a list with a single `Dictionary` object to a binary file:
```
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
```

This code also has a general exception handling block to process cases when writing to the file correctly fails for whatever reason (e.g., there are no permissions to write the file or not enough space on the device).

## Reading from the binary file

To read the values from the binary file the following function is created:
```
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
```

It handles a generic error if the reading was not successful, but also has a specific block for `FileNotFoundError` error type.

## Presentation Block

Here is the code that demonstrates how to use the functions:
```
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
```

Example of the script execution from the terminal is shown below:
