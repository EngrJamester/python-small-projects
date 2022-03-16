
import pip._internal as pip
package_names=['requests','beautifulsoup4'] #packages to install
pip.main(['install'] + package_names + ['--upgrade'] + ['--quiet']) #install line 5 and 6 packages
import requests
import bs4

def print_list(list_data,list_type):
    print("\nhere is the listing of {}:".format(list_type))
    for item in list_data:
        print(item)

#download web page - get response object
resp = requests.get('https://www.qutenberg.org/catalog')

try:
    resp.raise_for_status()
except Exception as exc:
    print('seems there was a problem: %s' % (exc))
print("\nyou should see '200' for status code:")
print(resp.status_code)
input("\npress enter to continue...\n")

#create a beatifulsoup object from the text attribute of the response object
gut_soup = bs4.BeautifulSoup(resp.text,"html.parse")

#pull all css elements named <input> that have a name attribute with any value
elems = gut_soup.selet('input[name]')
print("\nthere are {} elements of type '<input[name]'".format(len(elems)))
print("... annd here they are:")
for item in elems:
    print(item)
input("\npress enter to continue...\n")
print("\ncheck the 'class' of one of the elements:")
print(type(elems[2]))
print("\nexamine the elements attributes:")
for item in elems:
    print(item.attrs)

input("\npress enter to exit....\n")