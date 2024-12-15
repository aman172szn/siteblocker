import time
from datetime import datetime as dt


ip_local = "172.0.0.0"
blocked_list = ["www.facebook.com","www.instagram.com","facebook.com","instagram.com"]
host_path = "C:\Windows\System32\drivers\etc\hosts"
start_time = "09:00:00"
end_time = "18:00:00"


while True:
  now = dt.now()
  current_time = now.strftime("%H:%M:%S")
  print("current time is",current_time)
  if(start_time <= current_time and current_time <= end_time):
    print("working hours")
    with open(host_path,"r+") as file:
      content =  file.read()
      for website in blocked_list:
        if website in content:
          pass
        else:
          file.write(ip_local+" "+website+"\n")
    time.sleep(10)
  
  else:
    print("non working hour")
    with open(host_path,"r+") as file:
      content =  file.readlines()
      file.seek(0)
      for line in content:
        if not any (website in line for website in blocked_list):
          file.write(line)

      file.truncate() 
    time.sleep(10)
