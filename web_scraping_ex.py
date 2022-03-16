
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