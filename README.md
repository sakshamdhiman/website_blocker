# website_blocker
This program blocks the browser from accessing sites like facebook, youtube, instagram by redirecting the URL to 127.0.0.1 with the help of "hosts.txt" file.
## Running the program - 
- Replace "ABSOLUTE_FILE_ADDRESS" with address of this file on your PC.  
- Execute this file in cmd as an administrator.This file needs to be run as an administrator since appending "hosts.txt" need admin access.  
- Open the browser check facebook.com,youtube.com, these should be blocked.  
- Alternatively, "Task scheduler" can be used to run this program at system startup.   
  - Open Task scheduler from the start menu. Create new task.  
  - Check "Run with highest priviledges"
  - Go to actions tab, create new action.  
  - Program/script = "ADDRESS OF pythonw.exe". pythonw.exe is automatically downloaded with installation of python and is in the installation folder of python.
  - Additional Arguments = "C:\Users\dell_laptop\Desktop\New folder\Web_Blocker.pyw" => Absolute path of this file. Make sure to keep this file's extension as ".pyw".
  - Go to Triggers tab. Create a new trigger and set it to "At startup".
