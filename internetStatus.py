'''
Author:Rahul Rana
email-3rahul4@gmail.com
Contact in case of any query .
It is fully tested on Ubuntu.

Use Python3

'''

#!/usr/bin/python3
import os
import signal
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import GLib
import _thread
import time

APPINDICATOR_ID = 'myappindicator12'
APPINDICATOR_ID1 = 'myappindicator123'


def update(indicator):
	status= internet()
	change=0
	downChange=0
	while(status==True or status ==False):
		if status==True:
			downChange=0
			
			print ('Internet is Up')
			if change==0:
				change=1
				indicator.set_icon(os.path.abspath('/home/rahulrana95/Documents/arrows.svg'))

			
		else:
			change=0
			print('Internet is down')
			if downChange==0:
				downChange=1
				indicator.set_icon(os.path.abspath('/home/rahulrana95/Documents/live.svg'))
			
		time.sleep(2)
		status= internet()	

def main(pic):
    print  ('up running')
   
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath(pic), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    
    if __name__ == "__main__":
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        
    #GLib.timeout_add_seconds(1,1, update(indicator),1)  
    _thread.start_new_thread( update, (indicator, ) ) 
    gtk.main()
    



  

def build_menu():
    menu = gtk.Menu()
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

def quit(source):
    gtk.main_quit()






import socket,time
def internet(host="8.8.8.8", port=53, timeout=3):
	"""
	Host: 8.8.8.8 (google-public-dns-a.google.com)
	OpenPort: 53/tcp
	Service: domain (DNS/TCP)
.	"""
	try:
		socket.setdefaulttimeout(timeout)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
		return True
	except Exception as ex:

		print ('Not Working')
		return False


status= internet()

while(status==True or status ==False):
	if status==True:
		u=1
		d=0
		print ('Internet is Up')
		#quit(downmain())
		#if __name__ == "__main__":
		#	main()
		if __name__ == "__main__":
			main('live.svg')


	else:
		print('Internet is down')
		u=0
		d=1

		#quit(main())
		if __name__ == "__main__":
			main('arrows.svg')
		

	time.sleep(2)
	status= internet()				
