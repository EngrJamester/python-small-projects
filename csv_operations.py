import os
import csv

def print_list(list_data,list_type):
    print("\nHere is the listing of {}:".format(list_type))
    for item in list_data:
        print(item)


working_dir = '139890'
file_name = 'customer.csv'
new_file_name = 'new_customer.csv'
my_file = os.path.join('C:\\it_osaiti',working_dir,file_name)
my_new_file = os.path.join('C:\\it_osaiti',working_dir,new_file_name)


customer_file = open(my_file)
customer_reader = csv.reader(customer_file)
customer_data = list(customer_reader)
print("\npassing the reader to list() creates a list of lists:")
print(customer_data)
input("\npress enter to continue...\n")
print_list(customer_data,'customers')
input("\npress enter to continue")
print(customer_data[1][1] + ' email:' + customer_data[1][2])
input("\npress enter to continue...\n")
customer_file.close()

customer_file = open(my_new_file,'w',newline='')
customer_writer = csv.writer(customer_file)
customer_writer.writerow(['customer_id','customer_name','customer_email','prov_state','country'])
customer_writer.writerow(['1','Claudia Sand','claudia.sand@hotmail.com','NY','US'])
print("\nsuccessfully created new customer data file...")
input("\npress enter to exit...\n")