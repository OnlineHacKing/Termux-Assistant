import time
import datetime
import os
import subprocess



os.system('screenfetch')
print('\033[1m' + '\033[91m'+'     ///   CREATED BY TECHNICAL B9T   ///')
def wish():
  h=int(datetime.datetime.now().hour)
  if h<12:
     subprocess.call(["termux-tts-speak","Good morning sir","how may i help you"])
  else:
     if h>=12 and h<17:
       subprocess.call(["termux-tts-speak","good afternoon sir","how may i help you"])
     elif h>=17 and h<20:
       subprocess.call(["termux-tts-speak","good evening sir,how may i help you"])
     else:
       subprocess.call(["termux-tts-speak","welcome sir how may i help you"])
wish()
os.system("python main.py")