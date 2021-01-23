import random,time,os,sys,datetime,winsound,multiprocessing,urllib.request
import colorama
from colorama import Fore,Back,Style

colorama.init(autoreset=True,wrap=True)

VERSION = 'v.1.3'

def keygen_make(s):
    keygens = '';toPull = '';pKey = ''
    hour24 = datetime.datetime.now().strftime("%H")
    hour12 = datetime.datetime.now().strftime("%I")
    second60 = datetime.datetime.now().strftime("%S")
    curr_clock = int(int(hour24)/int(hour12))
    for i in s:
        toPull = random.randint(int(second60),int(len(s)+curr_clock+int(second60)))
        if i.isnumeric():
            esum = int(int(i) * toPull)
        else:
            esum = i
        esum = str(esum) + '|'
        keygens += str(esum)
        pKey += str(toPull) + '|'
    keygens = '|' + keygens
    return keygens[::-1],'|' + pKey

def keygen_hash(s,r):
    check = 0;cek=''
    s = s[::-1].replace("|"," ")
    s = s.split()
    r = r.replace("|"," ")  
    r = r.split()
    for _v,i in enumerate(s):
        if i.isnumeric(): 
            esum = int(int(i) / int(r[check]))
        else:
            esum = i
        cek += str(esum)
        check += 1
    return cek
    
def encrypt(text):
    text = text[::-1]
    curr = ''
    try:
        for i in text:
            a = ord(i) + 23
            curr += chr(a) 
        text = ''.join(curr.encode().hex())
        text = keygen_make(text)
    except:
        text = str('failed')
    return text
        
def decrypt(l1,l2):
    text = keygen_hash(l1,l2)
    curr = ''
    try:
        text = bytes.fromhex(text).decode('utf-8')
        text = text[::-1]
        for i in text:
            a = ord(i) - 23
            curr += chr(a)
        text = curr
    except:
        text = str('failed')
    return text 

def loading_bar(count,total,size):
    percent = float(count)/float(total)*100
    sys.stdout.write("\r" + str(int(count)).rjust(3,'0')+"/"+str(int(total)).rjust(3,'0') + ' [' + '='*int(percent/10)*size + ' '*(10-int(percent/10))*size + ']')

def make_update():
    print('\n')
    print(f"               {Back.GREEN + Style.BRIGHT}      CHECK FOR UPDATES      {Back.BLACK + Style.RESET_ALL}\n")
    try:
        GitHub = urllib.request.urlopen(f'https://github.com/rahmatagungj/toke/releases/tag/v.{int(VERSION[2]) + 1}.0')
        print(f'''  The application has a new version (v.{int(VERSION[2]) + 1}.0), visit: {Fore.BLUE}https:
  //github.com/rahmatagungj/toke/releases/tag/v.{int(VERSION[2]) + 1}.0''')
    except:
        try:
            GitHub = urllib.request.urlopen(f'https://github.com/rahmatagungj/toke/releases/tag/v.{VERSION[2]}.{int(VERSION[4]) + 1}')
            print(f'''  The application has a new version (v.{VERSION[2]}.{int(VERSION[4]) + 1}), visit: {Fore.BLUE}https:
  //github.com/rahmatagungj/toke/releases/tag/v.{VERSION[2]}.{int(VERSION[4]) + 1}''')
        except:
            print(f'''  The application is up to date.''')

def make_encrypt():
    print('\n')
    print(f"                   {Back.GREEN + Style.BRIGHT}      ENCRYPTION      {Back.BLACK + Style.RESET_ALL}\n")
    name_file = str(input(f"{Back.CYAN} * {Back.BLACK} Enter a file name (with the extension): "))
    
    file_message = '{}'.format(name_file)
    if os.path.isfile(file_message):
        try:
            inp = open(file_message, 'r')
            inp = inp.read()
        except:
            print(f"{Back.YELLOW} ! {Back.BLACK} File Not Supported!")
            make_try()
    else:
        print(f"{Back.YELLOW} ! {Back.BLACK} File Not Found!")
        make_try()
    layer = encrypt(inp)
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
    
def make_decrypt():     
    print("\n")
    print(f"                   {Back.GREEN + Style.BRIGHT}      DECRYPTION      {Back.BLACK + Style.RESET_ALL}\n")
    name_file_decrypt = str(input(f"{Back.CYAN} * {Back.BLACK} Enter a TOKE file name (without the extension): ")) 
    name_file_decrypt_format = str(input(f"{Back.CYAN} * {Back.BLACK} Enter the output file extension name: ")) 
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
                        curr_dec = decrypt(b,c)
                        for i in range(0,101):
                            loading_bar(i,100,2)
                            time.sleep(0.01)
                            if i == 100:
                                if curr_dec == 'failed':
                                    print('Decryption failed!')
                                else:
                                    x_file.write(curr_dec)
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
                                            make_try()               
                else:
                    print(f"{Back.YELLOW} ! {Back.BLACK} Files are not part of the encryption layer 2")
            else:
                print(f"{Back.YELLOW} ! {Back.BLACK} File Not Found!")
        else:
            print(f"{Back.YELLOW} ! {Back.BLACK} Files are not part of the encryption layer 1")
    else:
        print(f"{Back.YELLOW} ! {Back.BLACK} File Not Found!")

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
    make_try()

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
    make_try()

def make_try():
    print("\n")
    p = str(input(f"{Back.MAGENTA} ? {Back.BLACK} Back to menu? (y) / (n) :"))
    if p == 'y' or p == 'yes':
        main()
    elif p == 'n' or p == 'no':
        exit()
    else:
        exit()
        
def main():
    times = datetime.datetime.now()
    os.system('cls')
    os.system(f'title TOKE - Two Original Key Encryption {VERSION}')
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
    make_try()

def Finished():
    winsound.Beep(1000, 100)
    winsound.Beep(1200, 100)
    winsound.Beep(1400, 100)

def init():
    passed = 0
    os.system(f'title TOKE - Two Original Key Encryption {VERSION}')
    try:
        print(f"[*] Customizing Interface ...",end="")
        if callable(main):
            print(" Success") 
            winsound.Beep(1000, 200) 
            passed += 1
    except:
        print(" Failed")
        winsound.Beep(1000, 1000)

    try:
        print(f"[*] Checking Encryption Algorithm ...",end="")
        if callable(encrypt):
            print(" Success") 
            winsound.Beep(1000, 200) 
            passed += 1
    except:
        print(" Failed")
        winsound.Beep(1000, 1000)

    try:
        print(f"[*] Checking Decryption Algorithm ...",end="")
        if callable(decrypt):
            print(" Success") 
            winsound.Beep(1000, 200) 
            passed += 1
    except:
        print(" Failed")
        winsound.Beep(1000, 1000)

    try:
        print("[*] Loading KEY Generator ...",end="")
        if callable(keygen_make):
            print(" Success")
            winsound.Beep(1000, 200)
            passed += 1
    except:
        print(" Failed")
        winsound.Beep(1000, 1000)

    try:
        print(f"[*] Running KEY Hash ...",end="")
        if callable(keygen_hash):
            print(" Success") 
            winsound.Beep(1000, 200) 
            passed += 1
    except:
        print(" Failed")
        winsound.Beep(1000, 1000)

    try:
        print(f"[*] Check out additional systems ...",end="")
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
    if init() > 5:
        Finished()
        try:
            main()   
        except KeyboardInterrupt:
            exit()
        except:
            pass
    else:
        print("\n\nAn error occurred while running the TOKE system,\nContact: https://github.com/rahmatagungj/toke")
        time.sleep(60)
        exit()