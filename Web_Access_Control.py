#This programme Controls Web Access to help maximize work hours
#Written by Onuchukwu Marvellous
#written on December 12th, 2018.
import time
from datetime import datetime as dt
#Then we can do dt as datetime
#For a user on a windows OS we allow Read and Write to the file name host
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
#Redirect all web access to our localhost server
redirect ="127.0.0.1"
#List the sites that we need to block web access and will be redirected to host server
sites_to_block= ["www.facebook.com", "facebook.com", "web.whatsapp.com", "www.web.whatsapp.com", "gmail.com", "www.gmail.com", "www.yahoomail.com", "yahoomail.com", "Naijagist.com", "www.Naijagist.com", "Nairaland.com", "www.Nairaland.com", "www.Instagram.com", "instagram.com", "Twitter.com", "www.Twitter.com", "Youtube.com", "www.Youtube.com", "iroko.com", "www.iroko.com"]
#Time frame to block the listed sites
print(dt.now())
#Now the conditional statement for running programme
while True:
    #We must set the time frame in which the program should execute the block and also allow access
    #Using the 24HRS datetime format (Y/M/D:H/M/S/MS)
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("It's Working Hours")
#We allow the read and write priviledge to the host file using the r+
        with open(hosts_path,"r+") as file:
#Then load the entire file to allow write priviledge to the host
            content= file.read()
            for site in sites_to_block:
                if site in content:
                    pass
                else:
                    file.write(redirect+" " +site+ "\n")
#We create a script that would allow web access to the sites after the set time and remove them from the host path list
    else:
        with open(hosts_path, "r+") as file:
             content=file.readlines()
             file.seek(0)
             for line in content:
                 if not any(site in line for site in sites_to_block):
                     file.write(line)
#We initailize the truncate module to delete all things under the specified section
             file.truncate()
        print("Access Granted!!!")
    time.sleep(10)
        
#END