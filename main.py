import eel,os,random,platform,sys,threading,time
import tkinter 
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
import backend as backend

#GLOBAL VARIABLE
DEVMODE = True
canDecrypt = False	
canEncrypt = False

eel.init('web',allowed_extensions=['.js', '.html','.css'])

@eel.expose
def pick_file(mode):
	eel.js_disable_execute()
	root = tkinter.Tk()
	root.attributes("-topmost", True)
	root.withdraw()
	if mode == 'encrypt':
		filepath = askopenfilename(filetypes=(("text files","*.txt"),("All files","*.*")))
		if len(filepath) > 0:
			eel.js_set_path(filepath)
	elif mode == 'decrypt_tl1e':
		filepath = askopenfilename(filetypes=(("toke 1 files","*.tl1e"),))
		if len(filepath) > 0:
			eel.js_set_path_tl1e(filepath)
	elif mode == 'decrypt_tl2e':
		filepath = askopenfilename(filetypes=(("toke 2 files","*.tl2e"),))
		if len(filepath) > 0:
			eel.js_set_path_tl2e(filepath)
	elif mode == 'output':
		filepath = current_directory = filedialog.askdirectory()
		if len(filepath) > 0:
			eel.js_set_path_output(filepath)
	elif mode == 'output_decrypt':
		filepath = current_directory = filedialog.askdirectory()
		if len(filepath) > 0:
			eel.js_set_path_output_decrypt(filepath)
	elif mode == 'note':
		filepath = askopenfilename(filetypes=(("text files","*.txt"),("All files","*.*")))
		if len(filepath) > 0:
			try:
				note = open(filepath)
				text = note.read()
				eel.js_set_note(text)
				note.close()
			except Exception as e:
				print(e)
				eel.js_modal_error('TOKE SYSTEM','File Not Supported!')
	eel.js_enable_execute()

@eel.expose
def save_note(text):
	eel.js_disable_execute()
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
		eel.js_enable_execute()
	finally:
		eel.js_enable_execute()

@eel.expose
def encrypt_now(filename,fileE,keyE,emailE,sendEmail,fileEOutput):
	global canEncrypt
	if fileE == 'None':
		eel.js_modal_error('TOKE SYSTEM','Information entered is incomplete!')
		return
	eel.js_disable_execute()
	if sendEmail == 'yes': #Check if user will send a email
		if not backend.isOnline():
			eel.js_modal_error('TOKE SYSTEM','You are offline.')
			eel.js_enable_execute()
			return 
		if not backend.isEmail(str(emailE)):
			eel.js_modal_error('TOKE SYSTEM','Invalid email address.')
			eel.js_enable_execute()
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
		eel.js_enable_execute()
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
		eel.js_enable_execute()

@eel.expose
def decrypt_now(filenameD,extension,fileTL1E,fileTL2E,keyD,fileEOutputDecrypt):
	global canDecrypt
	if fileTL1E == 'None' or fileTL2E == 'None' or len(extension) <= 1 or len(filenameD) <= 1:
		eel.js_modal_error('TOKE SYSTEM','Information entered is incomplete!')
		return
	if len(keyD) < 1:
		keyD = ''
	eel.js_disable_execute()
	try:
		fileTl1e = open(fileTL1E, 'r')
		fileTl1e = fileTl1e.read()
		fileTl2e = open(fileTL2E, 'r')
		fileTl2e = fileTl2e.read()
		canDecrypt = True
	except:
		canDecrypt = False
		eel.js_modal_error('TOKE SYSTEM','Invalid file path!')
		eel.js_enable_execute()
		return
	if canDecrypt:
		curr_dec = backend.decrypt(fileTl1e,fileTl2e,str(keyD))
		if curr_dec == 'failed':
			eel.js_modal_error('TOKE SYSTEM','Decryption failed!')
			eel.js_enable_execute()
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
					eel.js_enable_execute()
			except:
				os.remove('{}.{}'.format(filenameD,extension))
				eel.js_modal_error('TOKE SYSTEM','Decryption failed!')
				eel.js_enable_execute()

def startup_check_update():
	time.sleep(5)
	update = backend.check_main_update()
	if update != None:
		eel.js_show_startup_update(update)

@eel.expose
def tools_check_update():
	eel.js_disable_execute()
	update = backend.check_main_update()
	if update != None:
		eel.js_show_startup_update(update)
	else:
		eel.js_restore_update()
	eel.js_enable_execute()

@eel.expose
def check_connection():
	eel.js_disable_execute()
	if backend.isOnline():
		eel.js_set_check_connection('online')
	else:
		eel.js_set_check_connection('offline')
	eel.js_enable_execute()

@eel.expose
def check_status_license():
	username,expired,status = backend.make_license_check()
	eel.js_set_check_license(status,expired)

@eel.expose
def main(state):
	if state == 'relaunch':
		inHost = 'localhost'
		inMode = None
		inPort = 2307
	else:
		if DEVMODE:
			inHost = 'localhost'
			inMode = None
			inPort = 2307
		else:
			inHost = 'localhost'
			inMode = 'chrome'
			inPort = 0
		if backend.isOnline():
			makeUpdate = threading.Thread(target=startup_check_update)
			makeUpdate.start()
	if DEVMODE:
		try:
			eel.start('index.html',host=inHost,mode=inMode,size=(550, 700),port=inPort,disable_cookie=True)
		except EnvironmentError:
			if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
				eel.start('index.html',host=inHost,mode='edge',size=(550, 700),port=0,disable_cookie=True)
			else:
				raise
		finally:
			print('Relaunching server development')
			main('relaunch')
	else:
		try:
			eel.start('index.html',host=inHost,mode=inMode,size=(550, 700),port=inPort,disable_cookie=True)
		except EnvironmentError:
			if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
				eel.start('index.html',host=inHost,mode='edge',size=(550, 700),port=0,disable_cookie=True)
			else:
				raise

if __name__ == '__main__':
	main('normal')