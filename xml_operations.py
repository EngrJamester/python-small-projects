import os
import xml.etree.ElementTree as et

#set up the working directory, file_name, full file path
working_dir = '139892'
file_name = 'customer.xml'
my_file = os.path.join('C:\\it_osaiti',working_dir,file_name)

#read from an xml file and print to console
tree = et.parse(my_file)
root = tree.getroot()
print("\nthe root tag is:")
print(root.tag)
input("\npress enter to continue...\n")

print("\nlist the tag and attrib for children nodes:")
for child in root:
    print(child.tag, child.attrib)
input("\npress enter to continue...\n")

print("\n\nlist each customer, along with their country:")\
for customer in root.findall('customer'):
    country = customer.find('country').text
    name = customer.get('name')
    print(name + ': ', country)
input("\npress enter to exit...\n")