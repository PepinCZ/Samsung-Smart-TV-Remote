#!  /usr/bin/python
# -*- coding: utf-8 -*-
#   Title: remote.py
#   Author: Josef Miegl
#   Date: 30SEP2015
#   Info: Pepin's Samsung Smart TV Remote
#   TODO:

import fcntl, socket, struct
import base64
import time, datetime
import netifaces
import random
from Tkinter import *

def getMyMac1(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return '-'.join(['%02x' % ord(char) for char in info[18:24]])

def getMyMac2(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])

myip = netifaces.ifaddresses(netifaces.gateways()['default'][netifaces.AF_INET][1])[netifaces.AF_INET][0]['addr']
mymac = getMyMac1(netifaces.gateways()['default'][netifaces.AF_INET][1])
appstring = "Pepin's Samsung Smart TV Remote"
remotename = "Pepin's Samsung Smart TV Remote"

print("")
print("Starting Pepin's Samsung Smart TV Remote")
print("")
print("Selected network interface:")
print(netifaces.gateways()['default'][netifaces.AF_INET][1])
print("")
print("My ip:")
print(netifaces.ifaddresses(netifaces.gateways()['default'][netifaces.AF_INET][1])[netifaces.AF_INET][0]['addr'])
print("")
print("My mac:")
print(getMyMac2(netifaces.gateways()['default'][netifaces.AF_INET][1]))
print("")

def sendKey(skey, dataSock, appstring):
 messagepart3 = chr(0x00) + chr(0x00) + chr(0x00) + chr(len(
base64.b64encode(skey))) + chr(0x00) + base64.b64encode(skey);
 part3 = chr(0x00) + chr(len(appstring)) + chr(0x00) \
+ appstring + chr(len(messagepart3)) + chr(0x00) + messagepart3
 dataSock.send(part3);

root = Tk()
root.title("Pepin's Samsung Smart TV Remote")
root.geometry("391x595") #391

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipencoded = base64.b64encode(myip)
macencoded = base64.b64encode(mymac)

messagepart1 = chr(0x64) + chr(0x00) + chr(len(ipencoded)) \
+ chr(0x00) + ipencoded + chr(len(macencoded)) + chr(0x00) \
+ macencoded + chr(len(base64.b64encode(remotename))) + chr(0x00) \
+ base64.b64encode(remotename)
part1 = chr(0x00) + chr(len(appstring)) + chr(0x00) + appstring \
+ chr(len(messagepart1)) + chr(0x00) + messagepart1
messagepart2 = chr(0xc8) + chr(0x00)
part2 = chr(0x00) + chr(len(appstring)) + chr(0x00) + appstring \
+ chr(len(messagepart2)) + chr(0x00) + messagepart2

class Application():
	"""Pepin's Samsung Smart TV Remote"""

	def __init__(self, master):

		self.master = master
		self.create_widgets()

	def connection(self):

                sock.connect((self.entry_tvip.get(), 55000))
		sock.send(part1)
		sock.send(part2)
                sock.settimeout(1)

		self.tvappstring = app.entry_tvappstring.get()
		#self.master.after(500, self.connection_status)


	def connection_status(self):

	 	if sock.recv(64) == "":

                        print("Status: Disconnected")
                        self.label_connection_status['text'] = 'Status: Disconnected'
                        self.label_connection_status['fg'] = 'red'
                else:

			print("Status: Connected")
			self.label_connection_status['text'] = 'Status: Connected'
                        self.label_connection_status['fg'] = 'green'
        
		self.master.after(random.randint(4000, 10000), self.connection_status)

	def create_widgets(self):

		btn_key_poweroff = Button(self.master, text = "Power", bg="red", width=4, height=2, command = lambda: sendKey("KEY_POWEROFF", sock, self.tvappstring)) 
        	btn_key_poweroff.grid(row=0, column=0)

		btn_key_source = Button(self.master, text = "Source", width=4, height=2, command = lambda: sendKey("KEY_SOURCE", sock, self.tvappstring)) 
        	btn_key_source.grid(row=0, column=2)

		btn_key_hdmi = Button(self.master, text = "HDMI", width=4, height=2, command = lambda: sendKey("KEY_HDMI", sock, self.tvappstring)) 
        	btn_key_hdmi.grid(row=0, column=1)

		btn_key_1 = Button(self.master, text = "1", width=4, height=2, command = lambda: sendKey("KEY_1", sock, self.tvappstring)) 
        	btn_key_1.grid(row=1, column=0)

		btn_key_2 = Button(self.master, text = "2", width=4, height=2, command = lambda: sendKey("KEY_2", sock, self.tvappstring))
        	btn_key_2.grid(row=1, column=1)

		btn_key_3 = Button(self.master, text = "3", width=4, height=2, command = lambda: sendKey("KEY_3", sock, self.tvappstring)) 
        	btn_key_3.grid(row=1, column=2)

		btn_key_4 = Button(self.master, text = "4", width=4, height=2, command = lambda: sendKey("KEY_4", sock, self.tvappstring)) 
        	btn_key_4.grid(row=2, column=0)

		btn_key_5 = Button(self.master, text = "5", width=4, height=2, command = lambda: sendKey("KEY_5", sock, self.tvappstring)) 
        	btn_key_5.grid(row=2, column=1)

		btn_key_6 = Button(self.master, text = "6", width=4, height=2, command = lambda: sendKey("KEY_6", sock, self.tvappstring)) 
        	btn_key_6.grid(row=2, column=2)

		btn_key_7 = Button(self.master, text = "7", width=4, height=2, command = lambda: sendKey("KEY_7", sock, self.tvappstring)) 
        	btn_key_7.grid(row=3, column=0)

		btn_key_8 = Button(self.master, text = "8", width=4, height=2, command = lambda: sendKey("KEY_8", sock, self.tvappstring)) 
        	btn_key_8.grid(row=3, column=1)

		btn_key_9 = Button(self.master, text = "9", width=4, height=2, command = lambda: sendKey("KEY_9", sock, self.tvappstring)) 
        	btn_key_9.grid(row=3, column=2)

		btn_key_ttx_mix = Button(self.master, text = "TTX/MIX", width=4, height=2, command = lambda: sendKey("KEY_TTX_MIX", sock, self.tvappstring)) 
        	btn_key_ttx_mix.grid(row=4, column=0)


		btn_key_0 = Button(self.master, text = "0", width=4, height=2, command = lambda: sendKey("KEY_0", sock, self.tvappstring)) 
        	btn_key_0.grid(row=4, column=1)

		btn_key_prech = Button(self.master, text = "PRE-CH", width=4, height=2, command = lambda: sendKey("KEY_PRECH", sock, self.tvappstring)) 
        	btn_key_prech.grid(row=4, column=2)

		btn_key_volup = Button(self.master, text = "+", bg="blue", width=4, height=2, command = lambda: sendKey("KEY_VOLUP", sock, self.tvappstring)) 
        	btn_key_volup.grid(row=5, column=0)

		btn_key_mute = Button(self.master, text = "MUTE", width=2, height=2, command = lambda: sendKey("KEY_MUTE", sock, self.tvappstring)) 
        	btn_key_mute.grid(row=5, column=1)

		btn_key_chup = Button(self.master, text = "↑", bg="blue", width=4, height=2, command = lambda: sendKey("KEY_CHUP", sock, self.tvappstring)) 
        	btn_key_chup.grid(row=5, column=2)

		btn_key_voldown = Button(self.master, text = "-", bg="blue", width=4, height=2, command = lambda: sendKey("KEY_VOLDOWN", sock, self.tvappstring)) 
        	btn_key_voldown.grid(row=6, column=0)

		btn_key_ch_list = Button(self.master, text = "CHLIST", width=2, height=2, command = lambda: sendKey("KEY_CH_LIST", sock, self.tvappstring)) 
        	btn_key_ch_list.grid(row=6, column=1)

		btn_key_chdown = Button(self.master, text = "↓", bg="blue", width=4, height=2, command = lambda: sendKey("KEY_CHDOWN", sock, self.tvappstring)) 
        	btn_key_chdown.grid(row=6, column=2)

		btn_key_menu = Button(self.master, text = "MENU", width=4, height=2, command = lambda: sendKey("KEY_MENU", sock, self.tvappstring)) 
        	btn_key_menu.grid(row=7, column=0)

		btn_key_contents = Button(self.master, text = "HUB", bg="orange", width=3, height=2, command = lambda: sendKey("KEY_CONTENTS", sock, self.tvappstring)) 
        	btn_key_contents.grid(row=7, column=1, pady=5)

		btn_key_guide = Button(self.master, text = "GUIDE", width=4, height=2, command = lambda: sendKey("KEY_GUIDE", sock, self.tvappstring)) 
        	btn_key_guide.grid(row=7, column=2)

		btn_key_tools = Button(self.master, text = "TOOLS", width=4, height=2, command = lambda: sendKey("KEY_TOOLS", sock, self.tvappstring)) 
        	btn_key_tools.grid(row=8, column=0)

		btn_key_up = Button(self.master, text = "▲", width=1, height=2, command = lambda: sendKey("KEY_UP", sock, self.tvappstring)) 
        	btn_key_up.grid(row=8, column=1)

		btn_key_info = Button(self.master, text = "INFO", width=4, height=2, command = lambda: sendKey("KEY_INFO", sock, self.tvappstring)) 
        	btn_key_info.grid(row=8, column=2)

		btn_key_left = Button(self.master, text = "◄", width=2, height=1, command = lambda: sendKey("KEY_LEFT", sock, self.tvappstring)) 
        	btn_key_left.grid(row=9, column=0)

		btn_key_enter = Button(self.master, text = "ENTER", width=2, height=1, command = lambda: sendKey("KEY_ENTER", sock, self.tvappstring)) 
        	btn_key_enter.grid(row=9, column=1, pady=10)

		btn_key_right = Button(self.master, text = "►", width=2, height=1, command = lambda: sendKey("KEY_RIGHT", sock, self.tvappstring)) 
        	btn_key_right.grid(row=9, column=2)

		btn_key_return = Button(self.master, text = "RETURN", width=4, height=2, command = lambda: sendKey("KEY_RETURN", sock, self.tvappstring)) 
        	btn_key_return.grid(row=10, column=0)

		btn_key_down = Button(self.master, text = "▼", width=1, height=2, command = lambda: sendKey("KEY_DOWN", sock, self.tvappstring)) 
        	btn_key_down.grid(row=10, column=1, pady=(0,5))

		btn_key_exit = Button(self.master, text = "EXIT", width=4, height=2, command = lambda: sendKey("KEY_EXIT", sock, self.tvappstring)) 
        	btn_key_exit.grid(row=10, column=2)

		btn_key_custom1 = Button(self.master, text = "Social TV", width=4, height=1, command = lambda: sendKey("KEY_TURBO", sock, self.tvappstring)) 
        	btn_key_custom1.grid(row=11, column=0)

		btn_key_custom2 = Button(self.master, text = "TV", width=4, height=1, command = lambda: sendKey("KEY_TV", sock, self.tvappstring)) 
        	btn_key_custom2.grid(row=11, column=1)

		btn_key_pannel_chdown = Button(self.master, text = "3D", width=4, height=1, command = lambda: sendKey("KEY_PANNEL_CHDOWN", sock, self.tvappstring)) 
        	btn_key_pannel_chdown.grid(row=11, column=2)

		btn_key_pmode = Button(self.master, text = "P.MODE", width=4, height=1, command = lambda: sendKey("KEY_PMODE", sock, self.tvappstring)) 
        	btn_key_pmode.grid(row=12, column=0)

		btn_key_picture_size = Button(self.master, text = "P.SIZE", width=4, height=1, command = lambda: sendKey("KEY_PICTURE_SIZE", sock, self.tvappstring)) 
        	btn_key_picture_size.grid(row=12, column=1)

		btn_key_caption = Button(self.master, text = "AD/SUB", width=4, height=1, command = lambda: sendKey("KEY_CAPTION", sock, self.tvappstring)) 
        	btn_key_caption.grid(row=12, column=2)

		btn_key_rewind = Button(self.master, text = "↞", width=4, height=1, command = lambda: sendKey("KEY_REWIND", sock, self.tvappstring)) 
        	btn_key_rewind.grid(row=13, column=0)

		btn_key_pause = Button(self.master, text = "▌▌", width=4, height=1, command = lambda: sendKey("KEY_PAUSE", sock, self.tvappstring)) 
        	btn_key_pause.grid(row=13, column=1)

		btn_key_ff = Button(self.master, text = "↠", width=4, height=1, command = lambda: sendKey("KEY_FF", sock, self.tvappstring)) 
        	btn_key_ff.grid(row=13, column=2)

		btn_key_rec = Button(self.master, text = "⚫", fg="red", width=4, height=1, command = lambda: sendKey("KEY_REC", sock, self.tvappstring)) 
        	btn_key_rec.grid(row=14, column=0)

		btn_key_ad = Button(self.master, text = "▶", width=4, height=1, command = lambda: sendKey("KEY_AD", sock, self.tvappstring)) 
        	btn_key_ad.grid(row=14, column=1)

		btn_key_stop = Button(self.master, text = "◼", width=4, height=1, command = lambda: sendKey("KEY_STOP", sock, self.tvappstring)) 
        	btn_key_stop.grid(row=14, column=2)

		btn_key_red = Button(self.master, text = "A", bg="red", width=2, height=1, command = lambda: sendKey("KEY_RED", sock, self.tvappstring)) 
        	btn_key_red.grid(row=0, column=3, padx=(15,0))

		btn_key_green = Button(self.master, text = "B", bg="green", width=2, height=1, command = lambda: sendKey("KEY_GREEN", sock, self.tvappstring)) 
        	btn_key_green.grid(row=0, column=4)

		btn_key_yellow = Button(self.master, text = "C", bg="yellow", width=2, height=1, command = lambda: sendKey("KEY_YELLOW", sock, self.tvappstring)) 
        	btn_key_yellow.grid(row=0, column=5)

		btn_key_cyan = Button(self.master, text = "D", bg="blue", width=2, height=1, command = lambda: sendKey("KEY_CYAN", sock, self.tvappstring)) 
        	btn_key_cyan.grid(row=0, column=6)

		entry_send_custom = Entry(self.master, width=22)
		entry_send_custom.grid(row=1, column=3, columnspan=4, padx=(15,0), ipady=8)

		btn_send_custom = Button(self.master, text = "SEND CUSTOM KEY", width=19, height=2, command = lambda: sendKey(entry_send_custom.get(), sock, self.tvappstring)) 
        	btn_send_custom.grid(row=2, column=3, columnspan=5, padx=(15,0))

		label_tvip = Label(self.master, text="TV IP:")
		label_tvip.grid(row=3, column=3, columnspan=1, padx=(15,0), ipady=8)

		self.entry_tvip = Entry(self.master, width=16)
		self.entry_tvip.grid(row=3, column=4, columnspan=3, ipady=8)

		label_tvappstring = Label(self.master, text="TV MODEL (Tv App String)")
		label_tvappstring.grid(row=4, column=3, columnspan=4, padx=(15,0), ipady=8, sticky=W)

		self.entry_tvappstring = Entry(self.master, width=22)
		self.entry_tvappstring.grid(row=5, column=3, columnspan=4, padx=(15,0), ipady=8)
		self.entry_tvappstring.insert(0, "UE55C8000")

		btn_connect = Button(self.master, text = "CONNECT TO TV", width=19, height=2, command = lambda: self.connection()) 
        	btn_connect.grid(row=6, column=3, columnspan=5, padx=(15,0))	

		self.label_connection_status = Label(self.master, text= "Status: Not Connected", fg="orange")
		self.label_connection_status.grid(row=7, column=3, columnspan=4, padx=(15,0), ipady=8, sticky=W) 

app = Application(root)
root.mainloop()

sock.close()

print("Exiting Pepin's Samsung Smart TV Remote")
