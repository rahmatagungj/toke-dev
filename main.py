# Copyright (c) 2020-2021 Rahmat Agung Julians

import eel
import os,platform,sys,threading,time,socket
import tkinter 
from tkinter.filedialog import askopenfilename,asksaveasfilename,askdirectory
import backend as backend

#GLOBAL VARIABLE
DEVMODE = False
canDecrypt = False	
canEncrypt = False

eel.init('GUI',allowed_extensions=['.js', '.html','.css'])

def get_port():
    """ Get an available port by starting a new server, stopping and and returning the port """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    port = sock.getsockname()[1]
    sock.close()
    return port


def startup_check_update():
	""" get new version if available """
	time.sleep(5)
	update = backend.check_main_update()
	if update != None:
		eel.js_show_startup_update(update)


@eel.expose
def check_version():
	""" Check version from tools """
	eel.js_modal_info('TOKE SYSTEM',"Currently at {}".format(backend.VERSION.upper()))


@eel.expose
def check_system():
	""" Check system from tools """
	eel.js_in_execute(True)
	point = 0
	if callable(get_port):
		point += 5
	if callable(pick_file):
		point += 5
	if callable(encrypt_now):
		point += 5
	if callable(decrypt_now):
		point += 5
	if callable(main):
		point += 5

	if point >= 20:
		eel.js_modal_info('TOKE SYSTEM','System checked successfully, no failures.')
	else:
		eel.js_modal_error('TOKE SYSTEM','System checked successfully, with failure.')
	eel.js_in_execute(False)


@eel.expose
def pick_file(mode):
	""" To Pick file and folder from UI """
	eel.js_in_execute(True)
	root = tkinter.Tk()
	root.attributes("-topmost", True)
	root.withdraw()
	if mode == 'encrypt':
		filepath = askopenfilename(filetypes=(("text files","*.txt"),("All files","*.*")), parent=root)
		if len(filepath) > 0:
			eel.js_set_path(filepath)
	elif mode == 'decrypt_tl1e':
		filepath = askopenfilename(filetypes=(("toke 1 files","*.tl1e"),), parent=root)
		if len(filepath) > 0:
			eel.js_set_path_tl1e(filepath)
	elif mode == 'decrypt_tl2e':
		filepath = askopenfilename(filetypes=(("toke 2 files","*.tl2e"),), parent=root)
		if len(filepath) > 0:
			eel.js_set_path_tl2e(filepath)
	elif mode == 'output':
		filepath = askdirectory(parent=root)
		if len(filepath) > 0:
			eel.js_set_path_output(filepath)
	elif mode == 'output_decrypt':
		filepath = askdirectory(parent=root)
		if len(filepath) > 0:
			eel.js_set_path_output_decrypt(filepath)
	elif mode == 'note':
		filepath = askopenfilename(filetypes=(("text files","*.txt"),("All files","*.*")), parent=root)
		if len(filepath) > 0:
			try:
				note = open(filepath)
				text = note.read()
				eel.js_set_note(text)
				note.close()
			except:
				eel.js_modal_error('TOKE SYSTEM','File Not Supported!')
	eel.js_in_execute(False)


@eel.expose
def save_note(text):
	""" To Save text from text editor """
	eel.js_in_execute(True)
	root = tkinter.Tk()
	root.attributes("-topmost", True)
	root.withdraw()
	try:
		withSave = asksaveasfilename(defaultextension='.txt',filetypes=(("text files","*.txt"),("All files","*.*")))
		note = open(withSave, 'w')
		note.write(text)
		note.close()
		eel.js_modal_success('TOKE SYSTEM','Saved successfully')
	except:
		eel.js_in_execute(False)
	finally:
		eel.js_in_execute(False)


@eel.expose
def encrypt_now(filename,fileE,keyE,emailE,sendEmail,fileEOutput):
	""" Main Encrypt function """
	global canEncrypt
	if fileE == 'None':
		eel.js_modal_error('TOKE SYSTEM','Information entered is incomplete!')
		return
	eel.js_in_execute(True)
	if sendEmail == 'yes': #Check if user will send a email ( Validation )
		if not backend.isOnline():
			eel.js_modal_error('TOKE SYSTEM','You are offline.')
			eel.js_in_execute(False)
			return 
		if not backend.isEmail(str(emailE)):
			eel.js_modal_error('TOKE SYSTEM','Invalid email address.')
			eel.js_in_execute(False)
			return
	else:
		pass 
	try:
		inp = open(fileE, 'r')
		inp = inp.read()
		canEncrypt = True
	except:
		canEncrypt = False
		eel.js_modal_error('TOKE SYSTEM','File Not Supported!')
		eel.js_in_execute(False)
		return
	if canEncrypt:
		layer = backend.encrypt(inp,str(keyE))
		if len(filename) <= 1:
			filename = 'encrypted'
		with open('{}.tl1e'.format(filename), 'w') as x_file:
				x_file.write(layer[0])
				x_file.close()
		with open('{}.tl2e'.format(filename), 'w') as x_file:
			x_file.write(layer[1])
			x_file.close()
		if keyE == '':
			keyE = 'without security key'
		eel.js_modal_success('TOKE SYSTEM','Encryption Success')
		if str(fileEOutput) == 'None':
			fileEOutput = ""
		toDir = str(fileEOutput)
		toke1 = os.path.join(toDir,'{}.tl1e'.format(filename)).replace('/','\\')
		toke2 = os.path.join(toDir,'{}.tl2e'.format(filename)).replace('/','\\')
		try:
			os.rename('{}.tl1e'.format(filename),toke1)
			os.rename('{}.tl2e'.format(filename),toke2)
		except:
			toke1 = '{}.tl1e'.format(filename)
			toke2 = '{}.tl2e'.format(filename)
		eel.js_set_result(f'''TOKE 1> {toke1}
TOKE 2> {toke2}
Security Key> {keyE}''')
		if sendEmail == 'yes':
			emailed = backend.email(emailE,fileE,str(filename),str(keyE))
			if emailed == 'success':
				eel.js_modal_info('TOKE SYSTEM',f'Email sent successfully')
			else:
				eel.js_modal_error('TOKE SYSTEM',f'Failed to send email')
		eel.js_in_execute(False)


@eel.expose
def decrypt_now(filenameD,extension,fileTL1E,fileTL2E,keyD,fileEOutputDecrypt):
	""" Main Decrypt function """
	global canDecrypt
	if fileTL1E == 'None' or fileTL2E == 'None' or len(extension) <= 1 or len(filenameD) <= 1:
		eel.js_modal_error('TOKE SYSTEM','Information entered is incomplete!')
		return
	if len(keyD) < 1:
		keyD = ''
	eel.js_in_execute(True)
	try: # Try to open file
		fileTl1e = open(fileTL1E, 'r')
		fileTl1e = fileTl1e.read()
		fileTl2e = open(fileTL2E, 'r')
		fileTl2e = fileTl2e.read()
		canDecrypt = True
	except:
		canDecrypt = False
		eel.js_modal_error('TOKE SYSTEM','Invalid file path!')
		eel.js_in_execute(False)
		return
	if canDecrypt:
		curr_dec = backend.decrypt(fileTl1e,fileTl2e,str(keyD))
		if curr_dec == 'failed':
			eel.js_modal_error('TOKE SYSTEM','Decryption failed!')
			eel.js_in_execute(False)
		else:
			try:
				with open('{}.{}'.format(filenameD,extension), 'w') as output_file:
					output_file.write(curr_dec)
					output_file.close()
					if str(fileEOutputDecrypt) == 'None':
						fileEOutputDecrypt = ""
					toDir = str(fileEOutputDecrypt)
					originalFile = os.path.join(toDir,'{}.{}'.format(filenameD,extension)).replace('/','\\')
					try:
						os.rename('{}.{}'.format(filenameD,extension),originalFile)
					except:
						originalFile = '{}.{}'.format(filenameD,extension)
					eel.js_set_result_decrypt(f'''ORIGINAL FILE> {originalFile}''')
					eel.js_modal_success('TOKE SYSTEM','Decryption success!')
					eel.js_in_execute(False)
			except:
				os.remove('{}.{}'.format(filenameD,extension))
				eel.js_modal_error('TOKE SYSTEM','Decryption failed!')
				eel.js_in_execute(False)


@eel.expose
def tools_check_update():
	""" To check Update application """
	eel.js_in_execute(True)
	update = backend.check_main_update()
	if update != None:
		eel.js_show_startup_update(update)
	else:
		eel.js_restore_update()
	eel.js_in_execute(False)


@eel.expose
def check_connection():
	""" To check connection user """
	eel.js_in_execute(True)
	if backend.isOnline():
		eel.js_set_check_connection('online')
	else:
		eel.js_set_check_connection('offline')
	eel.js_in_execute(False)


@eel.expose
def main():
	if DEVMODE:
		inHost = 'localhost'
		inMode = None
		inPort = 2307
	else:
		inHost = 'localhost'
		inMode = 'chrome'
		inPort = 2307 #get_port()
	if backend.isOnline(): # Check if user open this application in online mode, update will be show automatic
		makeUpdate = threading.Thread(target=startup_check_update)
		makeUpdate.start()
	if DEVMODE: 
		""" START SERVER IN DEVELOPMENT MODE 
			Condition : if server off will be automatic restart server
			with port 2307 """
		print('STARTING SERVER : localhost:{}'.format(inPort))
		try:
			eel.start('index.html',host=inHost,mode=inMode,size=(550, 700),port=inPort,disable_cookie=True)
		except EnvironmentError:
			if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
				eel.start('index.html',host=inHost,mode='edge',size=(550, 700),port=inPort,disable_cookie=True)
			else:
				raise
		except (SystemExit,KeyboardInterrupt):
			print('Relaunching server')
			main()
	else:
		""" START SERVER IN PRODUCTION MODE 
			Condition : Application will be kill in task if server off """
		try:
			eel.start('index.html',host=inHost,mode=inMode,size=(550, 700),port=inPort,disable_cookie=True)
		except EnvironmentError:
			if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
				eel.start('index.html',host=inHost,mode='edge',size=(550, 700),port=inPort,disable_cookie=True)
			else:
				raise


if __name__ == '__main__':
	main() #init main function