import time
from datetime import datetime as dt
import os

hosts_temp = r"ABSOLUTE_LOCATION_OF_THIS_FILE"
hosts_path = r"C:\\Windows\\System32\\drivers\\etc\\hosts" # address of host file
redirect = "127.0.0.1"#redirect IP address
website_list = ["www.facebook.com","facebook.com","instagram.com","www.instagram.com","youtube.com","www.youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,12) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        print("Working hours...")
        with open(hosts_path,'r+') as host_file:
            content_work = host_file.read()
            for website in website_list:
                if website in content_work:
                    pass
                else:
                    host_file.write(redirect+" "+website+"\n")
        
    else:
        print("Fun hours...")
        with open(hosts_path,'r+') as host_file:    
            content_fun = host_file.readlines()
            host_file.seek(0)
            for line in content_fun:
                if not any(website in line for website in website_list):
                    host_file.write(line)
                else:
                    host_file.truncate()

    time.sleep(300)
    #You can execute this file from cmd as an administrator
    #This file needs to be run as an administrator since "hosts.txt" need admin access
    #Task scheduler can be used to run this program at system startup 
    ##Giving it maximum priviledges for admin access
    ##With action setting as follows - 
    ###Program/script = "C:\Users\saksh\AppData\Local\Programs\Python\Python38\pythonw.exe"
    ###Additional Arguments = "C:\Users\saksh\Desktop\New folder\data science\Python 10 Desktop\App 3 Website Blocker\Web_Blocker.pyw"
    ##With trigger remaining "At system startup"
