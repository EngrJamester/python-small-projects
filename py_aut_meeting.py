#connect to outlook
import win32com.client as client
from datetime import date

outlook = client.Dispatch("outlook.application")

#create a new calendar items
#with the index 1 you can create an appointment
call_item = outlook.CreateItem(1)
#lets manipulate some base properties
call_item.subject = "WFH Jamester"
call_item.body = """Task For Today
 •	Completion of KT Videos 
 •	Completion of Roll-in Checklist
"""
# call_item.location = "test_location"
#the starting date and time has a specific formatting
#the hour mode is 12
call_item.Start = f"{date.today()} 2:00:00 PM"
# the duration is always given in minutes
call_item.duration = 600 #1.5 hours
# you can add an attachment with
# call_item.attachment.add("<path>")
# you can give the item more priority with
# call_item.importance = 2
#if you want to invite some people you need to change the status
#it allows having a meeting instead of an appointment
call_item.MeetingStatus = 1
#finally let's add some recipients
# required = call_item.Recipients.add("Exelon.IT.SPP.CSS.Offshore@accenture.com")
required = call_item.Recipients.add("jamester.c.go@accenture.com")
required.Type = 1
optional = call_item.Recipients.add("jamester.c.go@accenture.com")
optional.Type = 2
#with the display method you can see the results of you work
#call_item.display()
call_item.Send()

