import os
import datetime

def print_msg(msg):
    print("\nContents from message file:")
    for item in msg:
        print(item)


working_dir = '139889'
file_name = 'message.txt'
my_path = os.path.join('C:\\it_osaiti',working_dir)
my_file = os.path.join('C:\\it_osaiti',working_dir,file_name)
my_files = os.listdir(my_path)
print("\n\n")
for filename in my_files:
    print(filename)


message_file = open(my_file,'r')
print("\n\nContents from message file : {}".format(message_file.readlines()))
input("\npress Enter to continue...\n")
message_file.close()


message_file = open(my_file,'a')
message_file.write("\nFiles backed up: " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
message_file.close()
message_file = open(my_file,'r')
messages = message_file.readlines()

message_file.close()
print_msg(messages)
input("\npress Enter to exit..\n\n")

