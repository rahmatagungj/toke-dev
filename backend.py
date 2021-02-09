# Copyright (c) 2020-2021 Rahmat Agung Julians

import random,time,os,sys,datetime,urllib.request,ctypes,re
from tkinter import *
from datetime import date
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename

# GLOBAL VARIABLE
VERSION = 'v.1.6'
MessageBox = ctypes.windll.user32.MessageBoxW

def rand_sleep(start,end):
	randomis = random.uniform(start,end)
	return time.sleep(randomis)


def isExpired(datet):
	datet = str(datet)
	ExpirationDate = datetime.datetime.strptime(datet,"%Y-%m-%d").date()
	now = "{:%Y-%m-%d}".format(date.today())
	if str(ExpirationDate) <= now:
		return True
	else:
		return False


def check_regist(name,key):
	curr = '';last = ''
	ndate = ''; tdate = ''
	key = key.replace("-"," ")
	mins = key.split()
	mins = mins[10][::-1]
	# for date expired
	for k in key.split()[:10:]:
		ndate += str(k[::-1]) + ' '
	for l in ndate.split():
		tdate += str(chr(int(l) - int(mins)))
	# for username
	for j in key.split()[11::]:
		last += str(j[::-1]) + ' '
	for i in last.split():
		curr += str(chr((int(i) - int(mins))))
	if name == curr and isExpired(tdate) :
		return 'expired'
	elif name == curr and not isExpired(tdate) :
		return 'valid'
	else:
		return 'invalid'
	return name,curr


def write_license(username,license):
	content = username + '\n' + license
	with open('license.tlic','w') as lic:
		lic.write(content)
		lic.close()
		os.system("attrib +h license.tlic" )
		return True


def status_license():
	if os.path.isfile('license.tlic'):
		filename = open('license.tlic','r')
		inside = filename.read()
		try:
			fusername = inside.split()[0]
			fserial = inside.split()[1]
		except:
			fusername = ''
			fserial = ''
		filename.close()
		try:
			if check_regist(fusername,fserial) == 'expired':
				return "expired"
			elif check_regist(fusername,fserial) == 'valid':
				return 'valid'
			else:
				return 'invalid'
		except:
			MessageBox(0, 'The license file does not contain a valid user license.', 'TOKE SYSTEM',16)
			filename.close()
			try:
				os.remove("license.tlic")
			except:
				check_license()
			return 'invalid'
	else:
		 return 'invalid'


def open_license():
	if os.path.isfile('license.tlic'):
		filename = open('license.tlic','r')
		inside = filename.read()
		fusername = inside.split()[0]
		fserial = inside.split()[1]
		filename.close()
	else:
		fusername = 'None'
		fserial = 'None'
	return fusername,fserial


def check_license():
	global forusername
	if os.path.isfile('license.tlic'):
		if status_license() == 'valid':
			return 'valid'
		elif status_license() == 'expired':
			if os.path.exists("license.tlic"):
			  os.remove("license.tlic")
			  check_license()
			else:
			  check_license()
		elif status_license() == 'invalid':
			return 'invalid'
			check_license()
		else:
			return 'invalid'
			check_license()
	else:
		return 'register'


def keygen_make(s):
	keygens = '';toPull = '';pKey = ''
	hour24 = datetime.datetime.now().strftime("%H")
	hour12 = datetime.datetime.now().strftime("%I")
	second60 = datetime.datetime.now().strftime("%S")
	for i in s:
		toPull = random.randint(int(second60),int(len(s)+int(second60)))
		if i.isnumeric():
			esum = int(int(i) * toPull)
		else:
			esum = i
		esum = str(esum) + '|'
		keygens += str(esum)
		pKey += str(toPull) + '|'
	pKey = '|' + pKey
	return '|' + keygens,pKey[::-1]


def keygen_hash(s,r):
	check = 0;cek=''
	s = s.replace("|"," ")
	s = s.split()
	r = r[::-1].replace("|"," ")  
	r = r.split()
	for _v,i in enumerate(s):
		if i.isnumeric(): 
			esum = int(int(i) / int(r[check]))
		else:
			esum = i
		cek += str(esum)
		check += 1
	return cek

	
def encrypt(text,key):
	text = text[::-1]
	curr = '';curr_key = ''
	if key != '':
		if ' ' in key:
			return "failed"
		elif not len(str(key)) == 4:
			return "failed"
		for k in str(key):
			curr_key += str(ord(k)) + ' '
		curr_key = curr_key.split()
		key = int(curr_key[0]) + int(curr_key[1]) * int(curr_key[2]) - int(curr_key[3])
	else:
		key = 23
	try:
		for i in text:
			a = ord(i) + key
			curr += chr(a) 
		text = ''.join(curr.encode().hex())
		text = keygen_make(text)
	except:
		text = str('failed')
	return text

		
def decrypt(l1,l2,key):
	text = keygen_hash(l1,l2)
	curr = '';curr_key = '';pop = 0
	if key != '':
		if ' ' in key:
			return "failed"
		elif not len(str(key)) == 4:
			return "failed"
		for k in str(key):
			curr_key += str(ord(k)) + ' '
		curr_key = curr_key.split()
		key = int(curr_key[0]) + int(curr_key[1]) * int(curr_key[2]) - int(curr_key[3])
	else:
		key = 23
	try:
		text = bytes.fromhex(text).decode('utf-8')
		text = text[::-1]
		for i in text:
			a = ord(i) - key
			curr += chr(a)
		text = curr
	except:
		text = str('failed')
	return text 


def isOnline():
	try:
		result = urllib.request.urlopen(f'https://github.com/',timeout=10)
		return True
	except:
		return False

def isEmail(email):  
	regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
	if(re.search(regex,email)):  
		return True  
	else:  
		return False 


def email(emailed,file,filename,key):
	mail_content = f'''
	Hi {os.getlogin()}.

	File has been successfully encrypted, the following is the detailed information:

	Original File        : {file}
	Encrypted File    : {filename}.tl1e , {filename}.tl2e
	PIN code            : {str(key)}

	Here are the original files and encrypted files, thank you for using TOKE.
	* Make sure you save this information along with the PIN code to open the encrypted files.

																									  Thanks and Regards
																									 Rahmat Agung Julians
																											( Developer )
	'''
	message = MIMEMultipart()
	message['From'] = "TOKE SYSTEM"
	message['To'] = str(emailed)
	message['Subject'] = 'File has been successfully encrypted'
	message.attach(MIMEText('<img src="https://raw.githubusercontent.com/rahmatagungj/toke/main/Documentation/LOGO%20PANJANG.png" width="350" style="padding-left: 95px;"/>', 'html', 'utf-8'))   
	message.attach(MIMEText(mail_content, 'plain'))
	# file 
	files = [f'{filename}.tl1e',f'{filename}.tl2e']
	for f in files:
		with open(f, "rb") as fil:
			part = MIMEApplication(
				fil.read(),
				Name=basename(f)
			)
		part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
		message.attach(part)
	text = message.as_string()
	#login
	context = ssl.create_default_context()
	try:
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
			try:
				server.login('toke.system@gmail.com','pzolhdonudngbotf')
				server.sendmail('toke.system@gmail.com', str(emailed), text)
				return 'success'
			except:
				return 'failed'
	except:
		return 'Something went wrong'


def check_main_update():
	for check in range(5):
		try:
			GitHub = urllib.request.urlopen(f'https://github.com/rahmatagungj/toke/releases/tag/v.{int(VERSION[2]) + check + 1}.0')
			return f'v.{int(VERSION[2]) + check}.0'
		except:
			for check_sub in range(5):
				try:
					GitHub = urllib.request.urlopen(f'https://github.com/rahmatagungj/toke/releases/tag/v.{VERSION[2]}.{int(VERSION[4]) + check_sub + 1}')
					return f'v.{VERSION[2]}.{int(VERSION[4]) + check_sub  + 1}'
				except:
					pass


def make_auto_update():
	if isOnline():
		update = init_auto_update()
		return update 
	else:
		return 'offline'


def make_license_check():
	username, serial = open_license()
	curr = '';last = ''
	ndate = ''; tdate = ''
	key = serial.replace("-"," ")
	mins = key.split()
	mins = mins[10][::-1]
	# for date expired
	for k in key.split()[:10:]:
		ndate += str(k[::-1]) + ' '
	for l in ndate.split():
		tdate += str(chr(int(l) - int(mins)))
	# for username
	for j in key.split()[11::]:
		last += str(j[::-1]) + ' '
	for i in last.split():
		curr += str(chr((int(i) - int(mins))))
	if isExpired(tdate):
		return curr,tdate,'Expired'
	else:
		return curr,tdate,'Valid'

		
def remove_license():
	if os.path.isfile('license.tlic'):
		try:
			os.remove("license.tlic")
		except:
			remove_license()
	return True


def killme():
	os.system("taskkill /F /IM toke_64bit.exe /T")
	os.system("taskkill /F /IM toke_32bit.exe /T")
	os.system('taskkill /F /IM python.exe /T')
	sys.exit()
	exit()