# Logic-Bomb-Python
This is my understanding of a logic bomb, built using python.


This repo is for educational purpose only. I am not responsible for any damage this may cause on your system.

This will destroy your system, please run this in a VM. Use it at your own risk

This isn't a traditional logic bomb, this code will create various triggers and pyalods and store them in the system.
These triggers and payloads will act as the actual logic bomb.

Currently, there are three types of triggers (stored in modules/triggers.py)- 
1. Execute on after a certain time (Working for linux and windows)
2. Execute on after a certain date (Working for linux)
2. Execute on a certain key press (Working for linux)

List of payloads (stored in modules/payloads.py)- 
1. Fork Bomb
2. System shutdown
3. Bulk file creation

Flow - Select a payload -> select a trigger type -> choose whether to make persistent or not.
Code will create multiple files depending on the OS and then create a cleanup.sh file which can be used to remove all created files.
