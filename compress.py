import os
import zipfile

#this function will backup an entire folder to a .zip file

def backup_zip(folder):
    folder = os.path.abspath(folder) #use absolute path

    #determine filename to backup to
    ver = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(ver) + '.zip'
        if not os.path.exists(zip_filename):
            break
        ver += 1
    
    #create the zip file
    print("\narchiving %s..." % (zip_filename))
    backup_zip_file = zipfile.ZipFile(zip_filename,'w')

    #walk the folder tree in it's entirety to compress all files in subfolders as well