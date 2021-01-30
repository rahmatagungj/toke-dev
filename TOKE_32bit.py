# Copyright (c) 2020-2021 Rahmat Agung Julians

import random,time,os,sys,datetime,winsound,multiprocessing,urllib.request,ctypes,threading,win32api,requests
from datetime import date
import colorama,re
from colorama import Fore,Back,Style
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename
from playsound import playsound

colorama.init(autoreset=True,wrap=True)

# GLOBAL VARIABLE
VERSION = 'v.1.3'
MessageBox = ctypes.windll.user32.MessageBoxW
times = datetime.datetime.now()
full_path = os.path.realpath(__file__)
curr_path = os.getcwd().split('\\')[-1]
CRASHED = False


def make_crashed():
    global CRASHED
    CRASHED = True
    with open('toke_crash.tset','w') as tcrash:
        data_crash = str("{:%Y-%m-%d}".format(date.today())+" "+times.strftime("%H")+":"+times.strftime("%M")+":"+times.strftime("%S"))
        tcrash.write(str(data_crash))
        tcrash.close()
        os.system( "attrib +h toke_crash.tset" )
        return True

def on_exit(sig, func=None):
    make_crashed()
    os.system('cls')
    make_shutdown()

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
                MessageBox(0, 'Unable to delete license file automatically, please delete the license file before running the application.', 'TOKE SYSTEM',16)
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
    os.system('cls')
    os.system('mode 60,37')
    if os.path.isfile('license.tlic'):
        os.system('cls')
        if status_license() == 'valid':
            os.system('cls')
            print(f'''
















                         LOGGING IN''')
            for i in range(0,101):
                loading_bar_center(i,100,2)
                time.sleep(0.01)
                forusername = open_license()[0]
                if i == 100:
                    main()
        elif status_license() == 'expired':
            MessageBox(0, 'License Expired.', 'TOKE SYSTEM',64)
            if os.path.exists("license.tlic"):
              os.remove("license.tlic")
              check_license()
            else:
              MessageBox(0, 'The License does not exist.', 'TOKE SYSTEM',16)
              check_license()
        elif status_license() == 'invalid':
            MessageBox(0, 'Invalid License.', 'TOKE SYSTEM',16)
            check_license()
        else:
            check_license()
    else:
        os.system(f'title TOKE - Unregistered')
        print("Enter username : ",end="")
        username = input(str())
        print("Enter the serial number : ",end="")
        license = input(str())
        if len(username) == 12 and len(license) > 30 :
            if check_regist(username,license) == 'valid':
                if write_license(username,license):
                    check_license()
                else:
                    t_error = MessageBox(None, 'Oops, something went wrong.', 'TOKE SYSTEM',2)
                    if t_error == 3:
                        make_shutdown()
                    elif t_error == 4:
                        check_license()
            elif check_regist(username,license) == 'expired':
                MessageBox(0, 'License Expired.', 'TOKE SYSTEM',64)
                os.system('cls')
                check_license()
            else:
                MessageBox(0, 'Invalid License.', 'TOKE SYSTEM',16)
                os.system('cls')
                check_license()
        else:
            MessageBox(0, 'Invalid License.', 'TOKE SYSTEM',16)
            os.system('cls')
            check_license()

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

def download_toke_64bit():
    time.sleep(0.1)
    try:
        GitHub = urllib.request.urlopen(f'https://github.com/rahmatagungj/toke/releases/tag/v.{int(VERSION[2]) + 1}.0')
        get_response = requests.get(f"https://github.com/rahmatagungj/toke/releases/download/v.{int(VERSION[2]) + 1}.0/TOKE.exe",stream=True)
        print("complete")
        with open('temp_TOKE_64bit.exe', 'wb') as f:
            print("  Installing update ...\t\t\t",end="")
            for chunk in get_response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
            print("complete")
    except:
        try:
            GitHub = urllib.request.urlopen(f'https://github.com/rahmatagungj/toke/releases/tag/v.{VERSION[2]}.{int(VERSION[4]) + 1}')
            get_response = requests.get(f"https://github.com/rahmatagungj/toke/releases/download/v.{VERSION[2]}.{int(VERSION[4]) + 1}/TOKE.exe",stream=True)
            print("complete")
            with open('temp_TOKE_64bit.exe', 'wb') as f:
                print("  Installing update ...\t\t\t",end="")
                for chunk in get_response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                print("complete")
        except:
            print("failed")
            return
    try:
        if getattr(sys, 'frozen', False):
            bundle_dir = sys._MEIPASS
        else:
            bundle_dir = os.path.dirname(os.path.abspath('tinit_auto_update_64bit.bat'))
        file = os.path.join(bundle_dir, 'tinit_auto_update_64bit.bat')
        os.startfile(r"{}".format(file))
    except:
        pass
    print(f"\n\nThe application update installation is complete, please \nreopen the application.")
    rand_sleep(4,6)
    make_shutdown()

def download_toke_32bit():
    time.sleep(0.1)
    try:
        GitHub = urllib.request.urlopen(f'https://github.com/rahmatagungj/toke/releases/tag/v.{int(VERSION[2]) + 1}.0')
        get_response = requests.get(f"https://github.com/rahmatagungj/toke/releases/download/v.{int(VERSION[2]) + 1}.0/TOKE.exe",stream=True)
        print("complete")
        with open('temp_TOKE_32bit.exe', 'wb') as f:
            print("  Installing update ...\t\t\t",end="")
            for chunk in get_response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
            print("complete")
    except:
        try:
            GitHub = urllib.request.urlopen(f'https://github.com/rahmatagungj/toke/releases/tag/v.{VERSION[2]}.{int(VERSION[4]) + 1}')
            get_response = requests.get(f"https://github.com/rahmatagungj/toke/releases/download/v.{VERSION[2]}.{int(VERSION[4]) + 1}/TOKE.exe",stream=True)
            print("complete")
            with open('temp_TOKE_32bit.exe', 'wb') as f:
                print("  Installing update ...\t\t\t",end="")
                for chunk in get_response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            print("complete")
        except:
            print("failed")
            return
    try:
        if getattr(sys, 'frozen', False):
            bundle_dir = sys._MEIPASS
        else:
            bundle_dir = os.path.dirname(os.path.abspath('tinit_auto_update_32bit.bat'))
        file = os.path.join(bundle_dir, 'tinit_auto_update_32bit.bat')
        os.startfile(r"{}".format(file))
    except:
        pass
    print(f"\n\nThe application update installation is complete, please \nreopen the application.")
    rand_sleep(4,6)
    make_shutdown()

def init_auto_update():
    print("\n  Downloading Updates ...\t\t",end="")
    iver = os.path.split(sys.argv[0])[1][5:7:]
    if int(iver) == 32:
        download_toke_32bit()
    elif int(iver) == 64:
        download_toke_64bit()
    else:
        download_toke_32bit()

def check_online():
    print(f"\n                {Back.GREEN + Style.BRIGHT}      CHECKING NETWORK      {Back.BLACK + Style.RESET_ALL}\n")
    online = isOnline()
    if online == True:
        MessageBox(0, f'''  You are online.''', 'TOKE SYSTEM',64)
    else:
        MessageBox(0, ' You are offline.', 'TOKE SYSTEM',16)
    main()

def isEmail(email):  
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):  
        return True  
    else:  
        return False 

def try_email(file,key):
    print(f'{Back.CYAN} * {Back.BLACK} Enter email address: ',end="")
    emailed = str(input())
    print(f"\nSending email to {emailed} .... ",end="")
    email(emailed,file,key)

def email(emailed,file,key):
    if not isOnline():
        return print(f'{Back.YELLOW} ! {Back.BLACK}Unable to send email when you are offline!')
    if not isEmail(str(emailed)):
        print(f' invalid email!\n')
        try_email(file,key)
        return 
    mail_content = f'''
    Hi {os.getlogin()}.

    File "{file}"" has been successfully encrypted, the following is the detailed information:

    Original File        : {file}
    Encrypted File    : {os.path.splitext(file)[0]}.tl1e , {os.path.splitext(file)[0]}.tl2e
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
    message['Subject'] = f'File "{file}"" has been successfully encrypted'
    message.attach(MIMEText('<img src="https://raw.githubusercontent.com/rahmatagungj/toke/main/Documentation/LOGO%20PANJANG.png" width="350" style="padding-left: 95px;"/>', 'html', 'utf-8'))   
    message.attach(MIMEText(mail_content, 'plain'))
    # file 
    files = [f'{os.path.splitext(file)[0]}.tl1e',f'{os.path.splitext(file)[0]}.tl2e']
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
                return print('Success!')
            except:
                return print("Failed!")
    except:
        return print('Something went wrong...')

def loading_bar(count,total,size):
    percent = float(count)/float(total)*100
    sys.stdout.write("\r" + str(int(count)).rjust(3,'0')+"/"+str(int(total)).rjust(3,'0') + f'{Fore.CYAN} |' + '█'*int(percent/10)*size + ' '*(10-int(percent/10))*size + '| ')

def loading_bar_center(count,total,size):
    percent = float(count)/float(total)*100
    sys.stdout.write(F'\r{Fore.CYAN}                   |' + '█'*int(percent/10)*size + ' '*(10-int(percent/10))*size + '|')

def make_update():
    print('\n')
    print(f"              {Back.GREEN + Style.BRIGHT}     CHECKING FOR UPDATES      {Back.BLACK + Style.RESET_ALL}\n")
    try:
        GitHub = urllib.request.urlopen(f'https://github.com/rahmatagungj/toke/releases/tag/v.{int(VERSION[2]) + 1}.0')
        MessageBox(0, f'''  The application has a new version (v.{int(VERSION[2]) + 1}.0), visit: https:
  //github.com/rahmatagungj/toke/releases/tag/v.{int(VERSION[2]) + 1}.0''', 'TOKE SYSTEM',64)
    except:
        try:
            GitHub = urllib.request.urlopen(f'https://github.com/rahmatagungj/toke/releases/tag/v.{VERSION[2]}.{int(VERSION[4]) + 1}')
            MessageBox(0, f'''  The application has a new version (v.{VERSION[2]}.{int(VERSION[4]) + 1}), visit: https:
  //github.com/rahmatagungj/toke/releases/tag/v.{VERSION[2]}.{int(VERSION[4]) + 1}''', 'TOKE SYSTEM',64)
        except:
            MessageBox(0, f'''  The application is up to date.''', 'TOKE SYSTEM',64)
    main()

def check_main_update():
    irand = random.randint(1,2)
    if irand == 2:
        try:
            GitHub = urllib.request.urlopen(f'https://github.com/rahmatagungj/toke/releases/tag/v.{int(VERSION[2]) + 1}.0')
            print(f"{Back.YELLOW} ! {Back.BLACK} WARNING",)
            print(f'''\n  A new version v.{int(VERSION[2]) + 1}.0 is available, we recommend updating \n  to the latest version.\n''')
        except:
            try:
                GitHub = urllib.request.urlopen(f'https://github.com/rahmatagungj/toke/releases/tag/v.{VERSION[2]}.{int(VERSION[4]) + 1}')
                print(f"{Back.YELLOW} ! {Back.BLACK} WARNING")
                print(f'''\n  A new version v.{VERSION[2]}.{int(VERSION[4]) + 1} is available, we recommend updating \n  to the latest version.\n''')
            except:
                pass
    else:
        pass

def make_encrypt():
    print('\n')
    print(f"                   {Back.GREEN + Style.BRIGHT}      ENCRYPTION      {Back.BLACK + Style.RESET_ALL}\n")
    print(f"{Back.CYAN} * {Back.BLACK} Enter a file name (with the extension): ",end="")
    name_file = str(input())
    print(f"{Back.CYAN} * {Back.BLACK} Enter PIN code (4 digits or blank): ",end="")
    key_file = str(input())
    file_message = '{}'.format(name_file)
    if os.path.isfile(file_message):
        try:
            inp = open(file_message, 'r')
            inp = inp.read()
        except:
            MessageBox(0, 'File Not Supported!', 'TOKE SYSTEM',16)
            main()
    else:
        MessageBox(0, 'File Not Found!', 'TOKE SYSTEM',16)
        main()
    layer = encrypt(inp,key_file)
    print("\n")
    if layer == 'failed':
        for i in range(0,101):
            loading_bar(i,100,2)
            time.sleep(0.01)
            if i == 100:
                print(' Encryption Failed!')
    else: 
        with open('{}.tl1e'.format(os.path.splitext(name_file)[0]), 'w') as x_file:
            x_file.write(layer[0])

        with open('{}.tl2e'.format(os.path.splitext(name_file)[0]), 'w') as x_file:
            x_file.write(layer[1])
            for i in range(0,101):
                loading_bar(i,100,2)
                time.sleep(0.01)
                if i == 100:
                    print('Encryption Success!')
                    print(f"\n{Back.CYAN} * {Back.BLACK} OUTPUT: ")
                    print('> {}.tl1e'.format(os.path.splitext(name_file)[0]))
                    print('> {}.tl2e'.format(os.path.splitext(name_file)[0]))
                    print(f"\n{Back.CYAN} * {Back.BLACK} Will you send encrypted data to email? (y) / (n): ",end="")
                    ask_email = str(input())
                    if ask_email == 'y' or ask_email == 'yes':
                        print(f"{Back.CYAN} * {Back.BLACK} Enter email address: ",end="")
                        emailed = str(input())
                        print(f"\nSending email to {emailed} .... ",end="")
                        email(emailed,name_file,key_file)
    
def make_decrypt():     
    print("\n")
    print(f"                   {Back.GREEN + Style.BRIGHT}      DECRYPTION      {Back.BLACK + Style.RESET_ALL}\n")
    print(f"{Back.CYAN} * {Back.BLACK} Enter a TOKE file name (without the extension): ",end="")
    name_file_decrypt = str(input()) 
    print(f"{Back.CYAN} * {Back.BLACK} Enter the output file extension name: ",end="")
    name_file_decrypt_format = str(input())
    print(f"{Back.CYAN} * {Back.BLACK} Enter PIN code (4 digits or blank): ",end="")
    key_file = str(input()) 
    layer1_key = '{}.tl1e'.format(name_file_decrypt)
    layer2_key = '{}.tl2e'.format(name_file_decrypt)
    if os.path.isfile(layer1_key):
        if os.path.splitext(layer1_key)[1] == ".tl1e":
            b = open(layer1_key, 'r')
            b = b.read()
            if os.path.isfile(layer2_key):
                if os.path.splitext(layer2_key)[1] == ".tl2e":
                    c = open(layer2_key, 'r')
                    c = c.read()
                    curr_dec = decrypt(b,c,key_file)
                    print("\n")
                    for i in range(0,101):
                        loading_bar(i,100,2)
                        time.sleep(0.01)
                        if i == 100:
                            if curr_dec == 'failed':
                                print('Decryption failed!')
                            else:
                                with open('{}.{}'.format(name_file_decrypt,name_file_decrypt_format), 'w') as x_file:
                                    x_file.write(curr_dec)
                                    x_file.close()
                                    print('Decryption Success!')
                                    print(f"\n{Back.CYAN} * {Back.BLACK} OUTPUT: ")
                                    print('> {}.{}'.format(name_file_decrypt,name_file_decrypt_format))
                                    print(f"\n{Back.MAGENTA} ? {Back.BLACK} Do you want to delete TOKE files? (y) / (n) : ",end="")
                                    option = str(input())
                                    if option == 'y' or option == 'yes':
                                        if os.remove(layer1_key):
                                            print('- {} file failed to delete!'.format(layer1_key))
                                        else:
                                            print('- {} file deleted successfully!'.format(layer1_key)) 
                                        if os.remove(layer2_key):
                                            print('- {} file failed to delete!'.format(layer2_key))
                                        else:
                                            print('- {} file deleted successfully!'.format(layer2_key)) 
                                            make_ask()               
                else:
                    MessageBox(0, 'Files are not part of the encryption layer 2.', 'TOKE SYSTEM',16)
            else:
                MessageBox(0, 'File Not Found!', 'TOKE SYSTEM',16)
        else:
            MessageBox(0, 'Files are not part of the encryption layer 1.', 'TOKE SYSTEM',16)
    else:
        MessageBox(0, 'File Not Found!', 'TOKE SYSTEM',16)

def make_help():
    print("\n")
    print(f"                    {Back.GREEN + Style.BRIGHT}      HELP      {Back.BLACK + Style.RESET_ALL}\n")
    print(f'''\n{Back.MAGENTA} * {Back.BLACK} ENCRYPTION''')
    print(f'''\n  The message files that enter the system will be convert
  ed into 2 files containing the message keys, the 2 file
  s have different contents (in the form of numbers and c
  haracters). Make sure the file to be encrypted is in th
  e TOKE application folder.''')
    print(f'''\n{Back.MAGENTA} * {Back.BLACK} DECRYPTION''')
    print(f'''\n  The decrypt process will take place by combining 2 TOKE 
  files, namely TL1E and TL2E, if the two match, the orig
  inal file will be translated.Make sure the file to be d
  ecrypted is in the TOKE application folder.''')
    make_ask()

def make_about():
    print("\n")
    print(f"                   {Back.GREEN + Style.BRIGHT}      ABOUT      {Back.BLACK + Style.RESET_ALL}\n")
    print(f'''\n{Back.MAGENTA} * {Back.BLACK} TOKE SYSTEM''')
    print(f'''\n  {Fore.RED}TOKE {Fore.WHITE}({Fore.GREEN}Two Original Key Encryption{Fore.WHITE}) is a security method 
  through encryption of data in the form of numbers and c
  haracters, this system uses a mathematical algorithm th
  at can be used to secure certain messages. This service
  can convert ordinary messages in human language and fi
  les into more secure data.''')
    print(f'''\n{Back.MAGENTA} * {Back.BLACK} AUTHOR''')
    print(f'''\n  Rahmat Agung Julians, Indonesia. Contact : {Fore.BLUE + Style.BRIGHT}https://gith
  ub.com/rahmatagungj/toke''')
    make_ask()

def make_ask():
    print("\n")
    print(f"{Back.MAGENTA} ? {Back.BLACK} Press ENTER to continue ... ",end="")
    p = str(input())
    if p == '' or p == ' ':
        main()
    else:
        main()     

def make_auto_udpate():
    if isOnline():
        init_auto_update()
    else:
        print("Sorry, you are offline.")

def show_dir():
    print("\n")
    try:
        inlist = os.listdir('.')
        for show in inlist:
            if show.endswith('tl1e') or show.endswith('tl2e'):
                print(f"{Fore.GREEN + Style.BRIGHT}  ===>",show)
            else:
                pass
    except:
        print("  Directory location not found!")    

def show_command():
    print(f"\n                    {Back.GREEN + Style.BRIGHT}      COMMAND      {Back.BLACK + Style.RESET_ALL}\n")
    print(f'''
   COMMAND         DESCRIPTION
   -----------     ------------
   encrypt         Encrypt a file with or without a passw
                   ord.
   decrypt         Decrypt an encrypted file with or with
                   out a password.
   online          Check the user's network status.
   files           Displays files supported by the TOKE s
                   ystem in the program directory.
   license         Checks user license information data u
                   sed.
   shutdown        Turn off the TOKE system.
   exit            Exit application (same as shutdown).
   command         Displays all command functions (cmd).
   help            Displays encryption and decryption inf
                   ormation.
   about           Displays a page about the application.
        ''')

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
    print("\n")
    print(f"  Name\t\t: {curr}")
    print(f"  Expired\t: {tdate}")
    if isExpired(tdate):
        print(f"  Status\t: Expired")
    else:
        print(f"  Status\t: Valid")

def main():
    os.system('cls')
    os.system(f'title TOKE - Two Original Key Encryption {VERSION}')
    os.system('mode 60,37')
    print(f'''{Back.WHITE + Fore.BLACK} HI, {forusername.upper()}                                     {times.strftime("%H")}:{times.strftime("%M")} {Back.BLACK}                      ''')
    check_main_update()
    print(f"{Back.MAGENTA} # {Back.BLACK} {forusername.lower()}@toke> ",end="")
    p = str(input()).lower()
    if p == 'encrypt' or p == 'e':
        make_encrypt()
    elif p == 'decrypt' or p == 'd':
        make_decrypt()
    elif p == 'files' or p == 'show file':
        show_dir()
    elif p == 'help' or p == '?':
        make_help()
    elif p == 'about' or p == 'abot':
        make_about()
    elif p == 'update' or p == 'check update':
        make_auto_udpate()
    elif p == 'updates' or p == 'check updates':
        make_update()
    elif p == 'online' or p == 'check online':
        check_online()
    elif p == 'license' or p == 'show license':
        make_license_check()
    elif p == 'command' or p == 'show command' or p == 'cmd' or p == 'show cmd':
        show_command()
    elif p == 'remove license' or p == 'logout':
        remove_license()
    elif p == 'shutdown' or p == 'exit' or p == 's':
        make_shutdown()
    else:
        main()
    make_ask()

def init():
    passed = 0
    os.system(f'title TOKE - Two Original Key Encryption {VERSION}')
    if os.path.isfile('toke_crash.tset'):
        print(f'''{Back.WHITE + Fore.BLACK}                    TOKE SYSTEM - ERROR                     {Back.BLACK}                      ''')
        print("TOKE system fails to start, crashes while shutting down the\nprogram. Make sure to exit the program using the 'shutdown' \nor 'exit' command.")
        winsound.Beep(1000, 1000)
        print("\nPerforming an automatic repair :\n")
        rand_sleep(2,3)
        try:
            print(f"   Checking Operating System ...\t",end="")
            rand_sleep(0.5,1)
            if os.name == 'nt':
                print(" complete") 
                passed += 1
            else:
                passed = 0
                return passed
        except Exception as e:
            print(e)
            print(" failed")
            winsound.Beep(1000, 1000)
        try:
            print(f"   Reloading all function ...\t\t",end="")
            rand_sleep(0.8,1)
            if callable(main):
                print(" complete") 
                passed += 1
            else:
                passed = 0
                return passed
        except Exception as e:
            print(e)
            print(" failed")
            winsound.Beep(1000, 1000)
        try:
            print(f"   Repairing system files ...\t\t",end="")
            rand_sleep(0.6,1.1)
            if os.path.isfile('toke_crash.tset'):
                dateCrash = open('toke_crash.tset')
                dateCrashed = dateCrash.read()
                dateCrash.close()
                os.remove("toke_crash.tset")
                if callable(main):
                    print(" complete") 
                    passed += 1
                else:
                    passed = 0
                    return passed
            else:
                print(" failed")
        except:
            print(" failed")
            winsound.Beep(1000, 1000)
        print(f"\nThe crash has occurred at {dateCrashed}, \nrestarting ...")
    time.sleep(5)
    os.system('cls')
    print("Two Original Key Encryption {}".format(VERSION.upper()))
    print("Copyright (c) 2020-2023,Rahmat Agung Julians\n")
    print(f'''#{os.getpid()}-{multiprocessing.cpu_count()}\n''')
    print("Initialize all systems :\n")
    rand_sleep(1,2)
    try:
        print(f"   Checking Operating System ...\t",end="")
        rand_sleep(0,0.5)
        if os.name == 'nt':
            print(" complete") 
            passed += 1
        else:
            passed = 0
            return passed
    except Exception as e:
        print(" failed")
        winsound.Beep(1000, 1000)

    try:
        print(f"   Customizing Interface ...\t\t",end="")
        rand_sleep(0,0.5)
        if callable(main):
            print(" complete") 
            passed += 1
    except:
        print(" Failed")
        winsound.Beep(1000, 1000)

    try:
        print(f"   Checking Encryption Algorithm ...\t",end="")
        rand_sleep(0,0.5)
        if callable(encrypt):
            print(" complete") 
            passed += 1
    except:
        print(" failed")
        winsound.Beep(1000, 1000)

    try:
        print(f"   Checking Decryption Algorithm ...\t",end="")
        rand_sleep(0,0.5)
        if callable(decrypt):
            print(" complete") 
            passed += 1
    except:
        print(" failed")
        winsound.Beep(1000, 1000)

    try:
        print("   Loading KEY Generator ...\t\t",end="")
        rand_sleep(0,0.5)
        if callable(keygen_make):
            print(" complete")
            passed += 1
    except:
        print(" failed")
        winsound.Beep(1000, 1000)

    try:
        print(f"   Running KEY Hash ...\t\t\t",end="")
        rand_sleep(0,0.5)
        if callable(keygen_hash):
            print(" complete") 
            passed += 1
    except:
        print(" failed")
        winsound.Beep(1000, 1000)

    try:
        rand_sleep(0,0.5)
        print(f"   Check out additional systems ...\t",end="")
        if callable(make_update):
            print(" complete") 
            passed += 1
    except:
        print(" failed")
        winsound.Beep(1000, 1000)

    print(f"\nAll systems were successfully checked with 0 errors.")
    rand_sleep(0.8,2)
    return passed

def startup_sound():
    os.system('cls')
    try:
        if getattr(sys, 'frozen', False):
            bundle_dir = sys._MEIPASS
        else:
            bundle_dir = os.path.dirname(os.path.abspath('tstartup.mp3'))
        file = os.path.join(bundle_dir, 'tstartup.mp3')
        playsound(file)
    except:
        pass

def startup_splash():
    time.sleep(2)
    print(f'''












          {Fore.RED}
             ████████  
                ██   
                ██ 
        {Fore.WHITE}        ██  
                ██     ''')
    time.sleep(1)
    os.system('cls')
    print(f'''












          {Fore.RED}
             ████████  ██████ 
                ██    ██    ██ 
                ██    ██    ██ 
        {Fore.WHITE}        ██    ██    ██ 
                ██     ██████  ''')
    time.sleep(0.5)
    os.system('cls')
    print(f'''












          {Fore.RED}
             ████████  ██████  ██   ██
                ██    ██    ██ ██  ██      
                ██    ██    ██ █████   
        {Fore.WHITE}        ██    ██    ██ ██  ██ 
                ██     ██████  ██   ██''')
    time.sleep(0.2)
    os.system('cls')
    print(f'''












          {Fore.RED}
             ████████  ██████  ██   ██ ███████   
                ██    ██    ██ ██  ██  ██       
                ██    ██    ██ █████   █████   
        {Fore.WHITE}        ██    ██    ██ ██  ██  ██      
                ██     ██████  ██   ██ ███████ 
                ''')

def shutdown_sound():
    os.system('cls')
    try:
        if getattr(sys, 'frozen', False):
            bundle_dir = sys._MEIPASS
        else:
            bundle_dir = os.path.dirname(os.path.abspath('tshutdown.mp3'))
        file = os.path.join(bundle_dir, 'tshutdown.mp3')
        playsound(file)
    except:
        pass

def shutdown_splash():
    time.sleep(0.1)
    print(f'''












          {Fore.RED}
             ████████  ██████  ██   ██ ███████   
                ██    ██    ██ ██  ██  ██       
                ██    ██    ██ █████   █████   
        {Fore.WHITE}        ██    ██    ██ ██  ██  ██      
                ██     ██████  ██   ██ ███████ ''')
    time.sleep(1.9)
    os.system('cls')
    print(f'''












          {Fore.RED}
             ████████  ██████  ██   ██
                ██    ██    ██ ██  ██      
                ██    ██    ██ █████   
        {Fore.WHITE}        ██    ██    ██ ██  ██ 
                ██     ██████  ██   ██''')
    time.sleep(1)
    os.system('cls')
    print(f'''












          {Fore.RED}
             ████████  ██████ 
                ██    ██    ██ 
                ██    ██    ██ 
        {Fore.WHITE}        ██    ██    ██ 
                ██     ██████  ''')
    time.sleep(0.2)
    os.system('cls')
    print(f'''












          {Fore.RED}
             ████████  
                ██   
                ██ 
        {Fore.WHITE}        ██  
                ██     ''')
    time.sleep(0.5)
    os.system('cls')

def make_startup():
    global t_startup_sound,t_startup_splash,CRASHED
    try:
        win32api.SetConsoleCtrlHandler(on_exit, True)
        t_startup_sound = threading.Thread(target=startup_sound)
        t_startup_splash = threading.Thread(target=startup_splash)
        t_startup_sound.start()
        t_startup_splash.start()
    except:
        CRASHED = True
        MessageBox(0, 'An error occurred while running the TOKE system, Contact: https://github.com/rahmatagungj/toke', 'TOKE SYSTEM',16)
        exit()
    finally:
        time.sleep(8)

def make_shutdown():
    try:
        t_shutdown_sound = threading.Thread(target=shutdown_sound)
        t_shutdown_splash = threading.Thread(target=shutdown_splash)
        t_shutdown_sound.start()
        t_shutdown_splash.start()
    except:
        MessageBox(0, 'An error occurred while running the TOKE system, Contact: https://github.com/rahmatagungj/toke', 'TOKE SYSTEM',16)
        exit()
    finally:
        time.sleep(9)
        exit()

def remove_license():
    if os.path.isfile('license.tlic'):
        try:
            os.remove("license.tlic")
            os.system('cls')
            print(f'''
















                         LOGGING OUT''')
            for i in range(0,101):
                loading_bar_center(i,100,2)
                time.sleep(0.01)
                if i == 100:
                    check_license()
        except:
            remove_license()
    return True

if __name__ == "__main__":
    os.system('mode 60,37')
    check_license()
    if init() > 6:
        # make_startup()
        try:
            check_license()
        except KeyboardInterrupt:
            make_shutdown()
        except:
            pass
    else:
        CRASHED = True
        MessageBox(0, 'An error occurred while running the TOKE system, Contact: https://github.com/rahmatagungj/toke', 'TOKE SYSTEM',16)
        exit()

# if __name__ == "__main__":
#     os.system('mode 60,37')
#     if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
#         if init() > 6:
#             make_startup()
#             try:
#                 check_license()
#             except KeyboardInterrupt:
#                 make_shutdown()
#             except:
#                 pass
#         else:
#             MessageBox(0, 'An error occurred while running the TOKE system, Contact: https://github.com/rahmatagungj/toke', 'TOKE SYSTEM',16)
#             exit()
#     else:
#         MessageBox(0, 'An error occurred while running the TOKE system, Contact: https://github.com/rahmatagungj/toke', 'TOKE SYSTEM',16)
#         exit()
