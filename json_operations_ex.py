import os
import json

def print_customers(d_data, data_type, data_col):
    print("\nHere is the list of {}:".format(data_type))
    for item in d_data:
        print(item[data_col])

#set up the working directory, file_name, fill file path
working_dir = '139896'
file_name = 'customers.json'
my_file = os.path.join('C:\\it_osaiti',working_dir,file_name)

#read from a json file and print to console
customer_open = open(my_file)
customer_data = json.load(customer_open)
print(type(customer_data))
print(type(customer_data[0]))
print(customer_data)
input("\npress enter to continue...\n")

print_customers(customer_data,'customers','customer_name')
input("\npress enter to exit...\n")