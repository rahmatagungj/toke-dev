# Copyright (c) 2020-2021 Rahmat Agung Julians

import random,time,os,sys,datetime,winsound,multiprocessing,urllib.request,ctypes
from datetime import date
import colorama,re
from colorama import Fore,Back,Style
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename

colorama.init(autoreset=True,wrap=True)

# GLOBAL VARIABLE
VERSION = 'v.1.5'
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
    curr = '';curr_num = 1;real = '';last = ''
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
        curr_num += 1
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
        return True

def status_license():
    filename = open('license.tlic','r')
    inside = filename.read()
    try:
        fusername = inside.split()[0]
        fserial = inside.split()[1]
        filename.close()
    except:
        MessageBox(0, 'The license file does not contain a valid user license.', 'TOKE SYSTEM',16)
        filename.close()
        try:
            os.remove("license.tlic")
        except:
            MessageBox(0, 'Unable to delete license file automatically, please delete the license file before running the application.', 'TOKE SYSTEM',16)
        check_license()
        return 'invalid'
    if check_regist(fusername,fserial) == 'expired':
        return "expired"
    elif check_regist(fusername,fserial) == 'valid':
        return 'valid'
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
        try:
            if status_license() == 'valid':
                forusername = open_license()[0]
                main()
            elif status_license() == 'expired':
                MessageBox(0, 'License Expired.', 'TOKE SYSTEM',64)
                if os.path.exists("license.tlic"):
                  os.remove("license.tlic")
                  check_license()
                else:
                  MessageBox(0, 'The License does not exist.', 'TOKE SYSTEM',16)
                  check_license()
            else:
                MessageBox(0, 'Invalid License.', 'TOKE SYSTEM',16)
                check_license()
        except:
            exit()
    else:
        os.system(f'title TOKE - Unregistered')
        username = input(str("Enter username : "))
        license = input(str("Enter the serial number : "))
        try:
            if check_regist(username,license) == 'valid':
                if write_license(username,license):
                    check_license()
                else:
                    t_error = MessageBox(None, 'Oops, something went wrong.', 'TOKE SYSTEM',2)
                    if t_error == 3:
                        exit()
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
        except:
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
    except Exception as e:
        return False

def isEmail(email):  
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):  
        return True  
    else:  
        return False 

def try_email(file,key):
    emailed = str(input(f'{Back.CYAN} * {Back.BLACK} Enter email address: '))
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
    sys.stdout.write("\r" + str(int(count)).rjust(3,'0')+"/"+str(int(total)).rjust(3,'0') + ' [' + '='*int(percent/10)*size + ' '*(10-int(percent/10))*size + ']')

def make_update():
    print('\n')
    print(f"              {Back.GREEN + Style.BRIGHT}     CHECKING FOR UPDATES      {Back.BLACK + Style.RESET_ALL}\n")
    try:
        GitHub = urllib.request.urlopen(f'https://github.com/rahmatagungj/toke/releases/tag/v.{int(VERSION[2]) + 1}.0')
        MessageBox(0, f'''  The application has a new version (v.{int(VERSION[2]) + 1}.0), visit: {Fore.BLUE}https:
  //github.com/rahmatagungj/toke/releases/tag/v.{int(VERSION[2]) + 1}.0''', 'TOKE SYSTEM',64)
    except:
        try:
            GitHub = urllib.request.urlopen(f'https://github.com/rahmatagungj/toke/releases/tag/v.{VERSION[2]}.{int(VERSION[4]) + 1}')
            MessageBox(0, f'''  The application has a new version (v.{VERSION[2]}.{int(VERSION[4]) + 1}), visit: {Fore.BLUE}https:
  //github.com/rahmatagungj/toke/releases/tag/v.{VERSION[2]}.{int(VERSION[4]) + 1}''', 'TOKE SYSTEM',64)
        except:
            MessageBox(0, f'''  The application is up to date.''', 'TOKE SYSTEM',64)
    main()

def make_encrypt():
    print('\n')
    print(f"                   {Back.GREEN + Style.BRIGHT}      ENCRYPTION      {Back.BLACK + Style.RESET_ALL}\n")
    name_file = str(input(f"{Back.CYAN} * {Back.BLACK} Enter a file name (with the extension): "))
    key_file = str(input(f"{Back.CYAN} * {Back.BLACK} Enter PIN code (4 digits or blank): "))
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
                    print(' Encryption Success!')
                    print(f"\n{Back.CYAN} * {Back.BLACK} OUTPUT: ")
                    print('> {}.tl1e'.format(os.path.splitext(name_file)[0]))
                    print('> {}.tl2e'.format(os.path.splitext(name_file)[0]))
                    ask_email = str(input(f"\n{Back.CYAN} * {Back.BLACK} Will you send encrypted data to email? (y) / (n): "))
                    if ask_email == 'y' or ask_email == 'yes':
                        emailed = str(input(f"{Back.CYAN} * {Back.BLACK} Enter email address: "))
                        print(f"\nSending email to {emailed} .... ",end="")
                        email(emailed,name_file,key_file)
    
def make_decrypt():     
    print("\n")
    print(f"                   {Back.GREEN + Style.BRIGHT}      DECRYPTION      {Back.BLACK + Style.RESET_ALL}\n")
    name_file_decrypt = str(input(f"{Back.CYAN} * {Back.BLACK} Enter a TOKE file name (without the extension): ")) 
    name_file_decrypt_format = str(input(f"{Back.CYAN} * {Back.BLACK} Enter the output file extension name: "))
    key_file = str(input(f"{Back.CYAN} * {Back.BLACK} Enter PIN code (4 digits or blank): ")) 
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
                    with open('{}.{}'.format(name_file_decrypt,name_file_decrypt_format), 'w') as x_file:
                        curr_dec = decrypt(b,c,key_file)
                        print("\n")
                        for i in range(0,101):
                            loading_bar(i,100,2)
                            time.sleep(0.01)
                            if i == 100:
                                if curr_dec == 'failed':
                                    print('Decryption failed!')
                                else:
                                    x_file.write(curr_dec)
                                    x_file.close()
                                    print(' Decryption Success!')
                                    print(f"\n{Back.CYAN} * {Back.BLACK} OUTPUT: ")
                                    print('> {}.{}'.format(name_file_decrypt,name_file_decrypt_format))
                                    option = str(input(f"\n{Back.MAGENTA} ? {Back.BLACK} Do you want to delete TOKE files? (y) / (n) :"))
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
    p = str(input(f"{Back.MAGENTA} ? {Back.BLACK} Press ENTER to continue ... "))
    if p == '' or p == ' ':
        main()
    else:
        main()     

def main():
    times = datetime.datetime.now()
    os.system('cls')
    os.system(f'title TOKE - Registered for {forusername}')
    os.system('mode 60,37')
    print(f'''
          {Fore.RED}
             ████████  ██████  ██   ██ ███████   
                ██    ██    ██ ██  ██  ██       
                ██    ██    ██ █████   █████   
                ██    ██    ██ ██  ██  ██      
                ██     ██████  ██   ██ ███████ 
             {Fore.GREEN}Two   Original   Key   Encryption 

{Back.WHITE + Fore.BLACK}   PID : {os.getpid()} | CORE : {multiprocessing.cpu_count()} | TIME : {times.strftime("%H")}:{times.strftime("%M")} | VERSION : {VERSION[2]}.{VERSION[4]}    {Back.BLACK}

{Back.YELLOW + Fore.BLACK} 1. {Back.BLACK + Fore.WHITE} Encrypt {Back.YELLOW+ Fore.BLACK} 3. {Back.BLACK + Fore.WHITE} Help  {Back.YELLOW+ Fore.BLACK} 5. {Back.BLACK + Fore.WHITE} Check For Updates
{Back.YELLOW+ Fore.BLACK} 2. {Back.BLACK + Fore.WHITE} Decrypt {Back.YELLOW+ Fore.BLACK} 4. {Back.BLACK + Fore.WHITE} About {Back.YELLOW+ Fore.BLACK} 6. {Back.BLACK + Fore.WHITE} Exit                                
          ''')
    p = str(input(f"{Back.MAGENTA} # {Back.BLACK} Choose an option :"))
    if p == 'encrypt' or p == '1':
        make_encrypt()
    elif p == 'decrypt' or p == '2':
        make_decrypt()
    elif p == 'help' or p == '3':
        make_help()
    elif p == 'about' or p == '4':
        make_about()
    elif p == 'exit' or p == '5':
        make_update()
    elif p == 'exit' or p == '6':
        exit()
    else:
        main()
    make_ask()

def init():
    passed = 0
    os.system(f'title TOKE - Two Original Key Encryption {VERSION}')
    try:
        print(f"[*] Checking Operating System ...\t\t",end="")
        rand_sleep(0,0.5)
        if os.name == 'nt':
            print(" Success") 
            winsound.Beep(1000, 200) 
            passed += 1
        else:
            passed = 0
            return passed
    except Exception as e:
        print(e)
        print(" Failed")
        winsound.Beep(1000, 1000)

    try:
        print(f"[*] Customizing Interface ...\t\t\t",end="")
        rand_sleep(0,0.5)
        if callable(main):
            print(" Success") 
            winsound.Beep(1000, 200) 
            passed += 1
    except:
        print(" Failed")
        winsound.Beep(1000, 1000)

    try:
        print(f"[*] Checking Encryption Algorithm ...\t\t",end="")
        rand_sleep(0,0.5)
        if callable(encrypt):
            print(" Success") 
            winsound.Beep(1000, 200) 
            passed += 1
    except:
        print(" Failed")
        winsound.Beep(1000, 1000)

    try:
        print(f"[*] Checking Decryption Algorithm ...\t\t",end="")
        rand_sleep(0,0.5)
        if callable(decrypt):
            print(" Success") 
            winsound.Beep(1000, 200) 
            passed += 1
    except:
        print(" Failed")
        winsound.Beep(1000, 1000)

    try:
        print("[*] Loading KEY Generator ...\t\t\t",end="")
        rand_sleep(0,0.5)
        if callable(keygen_make):
            print(" Success")
            winsound.Beep(1000, 200)
            passed += 1
    except:
        print(" Failed")
        winsound.Beep(1000, 1000)

    try:
        print(f"[*] Running KEY Hash ...\t\t\t",end="")
        rand_sleep(0,0.5)
        if callable(keygen_hash):
            print(" Success") 
            winsound.Beep(1000, 200) 
            passed += 1
    except:
        print(" Failed")
        winsound.Beep(1000, 1000)

    try:
        print(f"[*] Check out additional systems ...\t\t",end="")
        rand_sleep(0,0.5)
        if callable(make_update):
            print(" Success") 
            winsound.Beep(1000, 200) 
            passed += 1
    except:
        print(" Failed")
        winsound.Beep(1000, 1000)
    return passed

if __name__ == "__main__":
    os.system('mode 60,37')
    check_license() #DELETE THIS LINE BEFORE BUILD
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        if init() > 6:
            winsound.Beep(1000, 100)
            winsound.Beep(1200, 100)
            winsound.Beep(1400, 100)
            try:
                check_license()
            except KeyboardInterrupt:
                exit()
            except:
                pass
        else:
            MessageBox(0, 'An error occurred while running the TOKE system, Contact: https://github.com/rahmatagungj/toke', 'TOKE SYSTEM',16)
            exit()
    else:
        MessageBox(0, 'An error occurred while running the TOKE system, Contact: https://github.com/rahmatagungj/toke', 'TOKE SYSTEM',16)
        exit()