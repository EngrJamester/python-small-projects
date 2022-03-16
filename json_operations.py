import os
import json

def print_customers(d_data, data_type, data_col):
    print("\nHere is the list of {}".format(data_type))
    for item in d_data:
        print(item[data_col])

working_dir = '139891'
file_name = 'customer.json'
my_file = os.path.join('C:\\it_osaiit',working_dir,file_name)

#read from a json file to be displayed in the console
customer_open = open(my_file)
customer_data = json.load(customer_open)
print(customer_data)
input("\npress enter to continue....\n")

print_customers(customer_data,'customers','customer_name')
input("\npress enter to exit...\n")