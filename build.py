import random ,time ,os ,sys ,datetime ,winsound ,multiprocessing ,urllib .request #line:1
import colorama #line:2
from colorama import Fore ,Back ,Style #line:3
colorama .init (autoreset =True ,wrap =True )#line:5
VERSION ='v.1.3'#line:7
def keygen_make (O0O0O0OO000OO0O0O ):#line:9
    O000O00O0OO0OOOOO ='';O0O0O0OOO00OOO0OO ='';OO00O0OOOOOO000O0 =''#line:10
    OOOO0OO0O000O0000 =datetime .datetime .now ().strftime ("%H")#line:11
    O0O00O0000OO000OO =datetime .datetime .now ().strftime ("%I")#line:12
    OOO0O0OOO000OO00O =datetime .datetime .now ().strftime ("%S")#line:13
    OO0O0O00O00O0O0OO =int (int (OOOO0OO0O000O0000 )/int (O0O00O0000OO000OO ))#line:14
    for O0O0000O00OOO000O in O0O0O0OO000OO0O0O :#line:15
        O0O0O0OOO00OOO0OO =random .randint (int (OOO0O0OOO000OO00O ),int (len (O0O0O0OO000OO0O0O )+OO0O0O00O00O0O0OO +int (OOO0O0OOO000OO00O )))#line:16
        if O0O0000O00OOO000O .isnumeric ():#line:17
            OOOO0O0O00OO00OO0 =int (int (O0O0000O00OOO000O )*O0O0O0OOO00OOO0OO )#line:18
        else :#line:19
            OOOO0O0O00OO00OO0 =O0O0000O00OOO000O #line:20
        OOOO0O0O00OO00OO0 =str (OOOO0O0O00OO00OO0 )+'|'#line:21
        O000O00O0OO0OOOOO +=str (OOOO0O0O00OO00OO0 )#line:22
        OO00O0OOOOOO000O0 +=str (O0O0O0OOO00OOO0OO )+'|'#line:23
    O000O00O0OO0OOOOO ='|'+O000O00O0OO0OOOOO #line:24
    return O000O00O0OO0OOOOO [::-1 ],'|'+OO00O0OOOOOO000O0 #line:25
def keygen_hash (OOOOO0O0OOOOOOOOO ,O00O00O000O0OO00O ):#line:27
    O00O0OO000O00O000 =0 ;OOO0OOO0OO0OO0OOO =''#line:28
    OOOOO0O0OOOOOOOOO =OOOOO0O0OOOOOOOOO [::-1 ].replace ("|"," ")#line:29
    OOOOO0O0OOOOOOOOO =OOOOO0O0OOOOOOOOO .split ()#line:30
    O00O00O000O0OO00O =O00O00O000O0OO00O .replace ("|"," ")#line:31
    O00O00O000O0OO00O =O00O00O000O0OO00O .split ()#line:32
    for _O0O00OO0O0O0O0000 ,OO0O000OOO00OOOOO in enumerate (OOOOO0O0OOOOOOOOO ):#line:33
        if OO0O000OOO00OOOOO .isnumeric ():#line:34
            OO0O0OOO0OO0OOOOO =int (int (OO0O000OOO00OOOOO )/int (O00O00O000O0OO00O [O00O0OO000O00O000 ]))#line:35
        else :#line:36
            OO0O0OOO0OO0OOOOO =OO0O000OOO00OOOOO #line:37
        OOO0OOO0OO0OO0OOO +=str (OO0O0OOO0OO0OOOOO )#line:38
        O00O0OO000O00O000 +=1 #line:39
    return OOO0OOO0OO0OO0OOO #line:40
def encrypt (O0O0OO0O00OOOOO0O ):#line:42
    O0O0OO0O00OOOOO0O =O0O0OO0O00OOOOO0O [::-1 ]#line:43
    OOOO0O00OOOOO0OOO =''#line:44
    try :#line:45
        for O00O00000O0O0OOO0 in O0O0OO0O00OOOOO0O :#line:46
            O00OOO00O0O0OOO00 =ord (O00O00000O0O0OOO0 )+23 #line:47
            OOOO0O00OOOOO0OOO +=chr (O00OOO00O0O0OOO00 )#line:48
        O0O0OO0O00OOOOO0O =''.join (OOOO0O00OOOOO0OOO .encode ().hex ())#line:49
        O0O0OO0O00OOOOO0O =keygen_make (O0O0OO0O00OOOOO0O )#line:50
    except :#line:51
        O0O0OO0O00OOOOO0O =str ('failed')#line:52
    return O0O0OO0O00OOOOO0O #line:53
def decrypt (O0O000OOOO0OO0O00 ,OO00O0O0O00OO0O0O ):#line:55
    O00OO000O0OO0O0O0 =keygen_hash (O0O000OOOO0OO0O00 ,OO00O0O0O00OO0O0O )#line:56
    OO0000OO0OO000O0O =''#line:57
    try :#line:58
        O00OO000O0OO0O0O0 =bytes .fromhex (O00OO000O0OO0O0O0 ).decode ('utf-8')#line:59
        O00OO000O0OO0O0O0 =O00OO000O0OO0O0O0 [::-1 ]#line:60
        for O0O0O0O0OOO00O000 in O00OO000O0OO0O0O0 :#line:61
            O0OO0OOO00OOO0000 =ord (O0O0O0O0OOO00O000 )-23 #line:62
            OO0000OO0OO000O0O +=chr (O0OO0OOO00OOO0000 )#line:63
        O00OO000O0OO0O0O0 =OO0000OO0OO000O0O #line:64
    except :#line:65
        O00OO000O0OO0O0O0 =str ('failed')#line:66
    return O00OO000O0OO0O0O0 #line:67
def loading_bar (O000O0OOOOO0OOO00 ,OO000OO00O000OOO0 ,OO00OOOOO0OOO00OO ):#line:69
    O0OO000OO0O00OOOO =float (O000O0OOOOO0OOO00 )/float (OO000OO00O000OOO0 )*100 #line:70
    sys .stdout .write ("\r"+str (int (O000O0OOOOO0OOO00 )).rjust (3 ,'0')+"/"+str (int (OO000OO00O000OOO0 )).rjust (3 ,'0')+' ['+'='*int (O0OO000OO0O00OOOO /10 )*OO00OOOOO0OOO00OO +' '*(10 -int (O0OO000OO0O00OOOO /10 ))*OO00OOOOO0OOO00OO +']')#line:71
def make_update ():#line:73
    print ('\n')#line:74
    print (f"               {Back.GREEN + Style.BRIGHT}      CHECK FOR UPDATES      {Back.BLACK + Style.RESET_ALL}\n")#line:75
    try :#line:76
        O000O0OOOOOOO00O0 =urllib .request .urlopen (f'https://github.com/rahmatagungj/toke/releases/tag/v.{int(VERSION[2]) + 1}.0')#line:77
        print (f'''  The application has a new version (v.{int(VERSION[2]) + 1}.0), visit: {Fore.BLUE}https:
  //github.com/rahmatagungj/toke/releases/tag/v.{int(VERSION[2]) + 1}.0''')#line:79
    except :#line:80
        try :#line:81
            O000O0OOOOOOO00O0 =urllib .request .urlopen (f'https://github.com/rahmatagungj/toke/releases/tag/v.{VERSION[2]}.{int(VERSION[4]) + 1}')#line:82
            print (f'''  The application has a new version (v.{VERSION[2]}.{int(VERSION[4]) + 1}), visit: {Fore.BLUE}https:
  //github.com/rahmatagungj/toke/releases/tag/v.{VERSION[2]}.{int(VERSION[4]) + 1}''')#line:84
        except :#line:85
            print (f'''  The application is up to date.''')#line:86
def make_encrypt ():#line:88
    print ('\n')#line:89
    print (f"                   {Back.GREEN + Style.BRIGHT}      ENCRYPTION      {Back.BLACK + Style.RESET_ALL}\n")#line:90
    O0O0OOO0OOO00OO00 =str (input (f"{Back.CYAN} * {Back.BLACK} Enter a file name (with the extension): "))#line:91
    O000O00O0OOOO000O ='{}'.format (O0O0OOO0OOO00OO00 )#line:93
    if os .path .isfile (O000O00O0OOOO000O ):#line:94
        try :#line:95
            OO0OOO00O0OOO0000 =open (O000O00O0OOOO000O ,'r')#line:96
            OO0OOO00O0OOO0000 =OO0OOO00O0OOO0000 .read ()#line:97
        except :#line:98
            print (f"{Back.YELLOW} ! {Back.BLACK} File Not Supported!")#line:99
            make_try ()#line:100
    else :#line:101
        print (f"{Back.YELLOW} ! {Back.BLACK} File Not Found!")#line:102
        make_try ()#line:103
    O00OOO0OOO0OOO00O =encrypt (OO0OOO00O0OOO0000 )#line:104
    if O00OOO0OOO0OOO00O =='failed':#line:105
        for OOO0O000OOOO000OO in range (0 ,101 ):#line:106
            loading_bar (OOO0O000OOOO000OO ,100 ,2 )#line:107
            time .sleep (0.01 )#line:108
            if OOO0O000OOOO000OO ==100 :#line:109
                print (' Encryption Failed!')#line:110
    else :#line:111
        with open ('{}.tl1e'.format (os .path .splitext (O0O0OOO0OOO00OO00 )[0 ]),'w')as O0OO00OO0000OO00O :#line:112
            O0OO00OO0000OO00O .write (O00OOO0OOO0OOO00O [0 ])#line:113
        with open ('{}.tl2e'.format (os .path .splitext (O0O0OOO0OOO00OO00 )[0 ]),'w')as O0OO00OO0000OO00O :#line:115
            O0OO00OO0000OO00O .write (O00OOO0OOO0OOO00O [1 ])#line:116
            for OOO0O000OOOO000OO in range (0 ,101 ):#line:117
                loading_bar (OOO0O000OOOO000OO ,100 ,2 )#line:118
                time .sleep (0.01 )#line:119
                if OOO0O000OOOO000OO ==100 :#line:120
                    print (' Encryption Success!')#line:121
                    print (f"\n{Back.CYAN} * {Back.BLACK} OUTPUT: ")#line:122
                    print ('> {}.tl1e'.format (os .path .splitext (O0O0OOO0OOO00OO00 )[0 ]))#line:123
                    print ('> {}.tl2e'.format (os .path .splitext (O0O0OOO0OOO00OO00 )[0 ]))#line:124
def make_decrypt ():#line:126
    print ("\n")#line:127
    print (f"                   {Back.GREEN + Style.BRIGHT}      DECRYPTION      {Back.BLACK + Style.RESET_ALL}\n")#line:128
    OOO0O0OO0OOO0O00O =str (input (f"{Back.CYAN} * {Back.BLACK} Enter a TOKE file name (without the extension): "))#line:129
    O00O0O00OOOO0OOOO =str (input (f"{Back.CYAN} * {Back.BLACK} Enter the output file extension name: "))#line:130
    O0OO00000OO0OO00O ='{}.tl1e'.format (OOO0O0OO0OOO0O00O )#line:131
    OO00OO000O0OO0000 ='{}.tl2e'.format (OOO0O0OO0OOO0O00O )#line:132
    if os .path .isfile (O0OO00000OO0OO00O ):#line:133
        if os .path .splitext (O0OO00000OO0OO00O )[1 ]==".tl1e":#line:134
            OO00O0O00O0OOOO0O =open (O0OO00000OO0OO00O ,'r')#line:135
            OO00O0O00O0OOOO0O =OO00O0O00O0OOOO0O .read ()#line:136
            if os .path .isfile (OO00OO000O0OO0000 ):#line:137
                if os .path .splitext (OO00OO000O0OO0000 )[1 ]==".tl2e":#line:138
                    O0000O00O00OOOO0O =open (OO00OO000O0OO0000 ,'r')#line:139
                    O0000O00O00OOOO0O =O0000O00O00OOOO0O .read ()#line:140
                    with open ('{}.{}'.format (OOO0O0OO0OOO0O00O ,O00O0O00OOOO0OOOO ),'w')as O00OOO0O0O00O0O0O :#line:142
                        OO0O0OO0O000O0OO0 =decrypt (OO00O0O00O0OOOO0O ,O0000O00O00OOOO0O )#line:143
                        for OOOOOO0O0OO0O0OO0 in range (0 ,101 ):#line:144
                            loading_bar (OOOOOO0O0OO0O0OO0 ,100 ,2 )#line:145
                            time .sleep (0.01 )#line:146
                            if OOOOOO0O0OO0O0OO0 ==100 :#line:147
                                if OO0O0OO0O000O0OO0 =='failed':#line:148
                                    print ('Decryption failed!')#line:149
                                else :#line:150
                                    O00OOO0O0O00O0O0O .write (OO0O0OO0O000O0OO0 )#line:151
                                    print (' Decryption Success!')#line:152
                                    print (f"\n{Back.CYAN} * {Back.BLACK} OUTPUT: ")#line:153
                                    print ('> {}.{}'.format (OOO0O0OO0OOO0O00O ,O00O0O00OOOO0OOOO ))#line:154
                                    OOOOO0O0O0OO0OOO0 =str (input (f"\n{Back.MAGENTA} ? {Back.BLACK} Do you want to delete TOKE files? (y) / (n) :"))#line:155
                                    if OOOOO0O0O0OO0OOO0 =='y'or OOOOO0O0O0OO0OOO0 =='yes':#line:156
                                        if os .remove (O0OO00000OO0OO00O ):#line:157
                                            print ('- {} file failed to delete!'.format (O0OO00000OO0OO00O ))#line:158
                                        else :#line:159
                                            print ('- {} file deleted successfully!'.format (O0OO00000OO0OO00O ))#line:160
                                        if os .remove (OO00OO000O0OO0000 ):#line:161
                                            print ('- {} file failed to delete!'.format (OO00OO000O0OO0000 ))#line:162
                                        else :#line:163
                                            print ('- {} file deleted successfully!'.format (OO00OO000O0OO0000 ))#line:164
                                            make_try ()#line:165
                else :#line:166
                    print (f"{Back.YELLOW} ! {Back.BLACK} Files are not part of the encryption layer 2")#line:167
            else :#line:168
                print (f"{Back.YELLOW} ! {Back.BLACK} File Not Found!")#line:169
        else :#line:170
            print (f"{Back.YELLOW} ! {Back.BLACK} Files are not part of the encryption layer 1")#line:171
    else :#line:172
        print (f"{Back.YELLOW} ! {Back.BLACK} File Not Found!")#line:173
def make_help ():#line:175
    print ("\n")#line:176
    print (f"                    {Back.GREEN + Style.BRIGHT}      HELP      {Back.BLACK + Style.RESET_ALL}\n")#line:177
    print (f'''\n{Back.MAGENTA} * {Back.BLACK} ENCRYPTION''')#line:178
    print (f'''\n  The message files that enter the system will be convert
  ed into 2 files containing the message keys, the 2 file
  s have different contents (in the form of numbers and c
  haracters). Make sure the file to be encrypted is in th
  e TOKE application folder.''')#line:183
    print (f'''\n{Back.MAGENTA} * {Back.BLACK} DECRYPTION''')#line:184
    print (f'''\n  The decrypt process will take place by combining 2 TOKE 
  files, namely TL1E and TL2E, if the two match, the orig
  inal file will be translated.Make sure the file to be d
  ecrypted is in the TOKE application folder.''')#line:188
    make_try ()#line:189
def make_about ():#line:191
    print ("\n")#line:192
    print (f"                   {Back.GREEN + Style.BRIGHT}      ABOUT      {Back.BLACK + Style.RESET_ALL}\n")#line:193
    print (f'''\n{Back.MAGENTA} * {Back.BLACK} TOKE SYSTEM''')#line:194
    print (f'''\n  {Fore.RED}TOKE {Fore.WHITE}({Fore.GREEN}Two Original Key Encryption{Fore.WHITE}) is a security method 
  through encryption of data in the form of numbers and c
  haracters, this system uses a mathematical algorithm th
  at can be used to secure certain messages. This service
  can convert ordinary messages in human language and fi
  les into more secure data.''')#line:200
    print (f'''\n{Back.MAGENTA} * {Back.BLACK} AUTHOR''')#line:201
    print (f'''\n  Rahmat Agung Julians, Indonesia. Contact : {Fore.BLUE + Style.BRIGHT}https://gith
  ub.com/rahmatagungj/toke''')#line:203
    make_try ()#line:204
def make_try ():#line:206
    print ("\n")#line:207
    OOO0O000O0O00OO00 =str (input (f"{Back.MAGENTA} ? {Back.BLACK} Back to menu? (y) / (n) :"))#line:208
    if OOO0O000O0O00OO00 =='y'or OOO0O000O0O00OO00 =='yes':#line:209
        main ()#line:210
    elif OOO0O000O0O00OO00 =='n'or OOO0O000O0O00OO00 =='no':#line:211
        exit ()#line:212
    else :#line:213
        exit ()#line:214
def main ():#line:216
    OOO00OO0O00O0000O =datetime .datetime .now ()#line:217
    os .system ('cls')#line:218
    os .system (f'title TOKE - Two Original Key Encryption {VERSION}')#line:219
    os .system ('mode 60,37')#line:220
    print (f'''
          {Fore.RED}
             ████████  ██████  ██   ██ ███████   
                ██    ██    ██ ██  ██  ██       
                ██    ██    ██ █████   █████   
                ██    ██    ██ ██  ██  ██      
                ██     ██████  ██   ██ ███████ 
             {Fore.GREEN}Two   Original   Key   Encryption 

{Back.WHITE + Fore.BLACK}   PID : {os.getpid()} | CORE : {multiprocessing.cpu_count()} | TIME : {OOO00OO0O00O0000O.strftime("%H")}:{OOO00OO0O00O0000O.strftime("%M")} | VERSION : {VERSION[2]}.{VERSION[4]}    {Back.BLACK}

{Back.YELLOW + Fore.BLACK} 1. {Back.BLACK + Fore.WHITE} Encrypt {Back.YELLOW+ Fore.BLACK} 3. {Back.BLACK + Fore.WHITE} Help  {Back.YELLOW+ Fore.BLACK} 5. {Back.BLACK + Fore.WHITE} Check For Updates
{Back.YELLOW+ Fore.BLACK} 2. {Back.BLACK + Fore.WHITE} Decrypt {Back.YELLOW+ Fore.BLACK} 4. {Back.BLACK + Fore.WHITE} About {Back.YELLOW+ Fore.BLACK} 6. {Back.BLACK + Fore.WHITE} Exit                                
          ''')#line:234
    O0OO0OOOOOOOOO000 =str (input (f"{Back.MAGENTA} # {Back.BLACK} Choose an option :"))#line:235
    if O0OO0OOOOOOOOO000 =='encrypt'or O0OO0OOOOOOOOO000 =='1':#line:236
        make_encrypt ()#line:237
    elif O0OO0OOOOOOOOO000 =='decrypt'or O0OO0OOOOOOOOO000 =='2':#line:238
        make_decrypt ()#line:239
    elif O0OO0OOOOOOOOO000 =='help'or O0OO0OOOOOOOOO000 =='3':#line:240
        make_help ()#line:241
    elif O0OO0OOOOOOOOO000 =='about'or O0OO0OOOOOOOOO000 =='4':#line:242
        make_about ()#line:243
    elif O0OO0OOOOOOOOO000 =='exit'or O0OO0OOOOOOOOO000 =='5':#line:244
        make_update ()#line:245
    elif O0OO0OOOOOOOOO000 =='exit'or O0OO0OOOOOOOOO000 =='6':#line:246
        exit ()#line:247
    else :#line:248
        main ()#line:249
    make_try ()#line:250
def Finished ():#line:252
    winsound .Beep (1000 ,100 )#line:253
    winsound .Beep (1200 ,100 )#line:254
    winsound .Beep (1400 ,100 )#line:255
def init ():#line:257
    OO00OOOO0000OO0O0 =0 #line:258
    os .system (f'title TOKE - Two Original Key Encryption {VERSION}')#line:259
    try :#line:260
        print (f"[*] Customizing Interface ...",end ="")#line:261
        if callable (main ):#line:262
            print (" Success")#line:263
            winsound .Beep (1000 ,200 )#line:264
            OO00OOOO0000OO0O0 +=1 #line:265
    except :#line:266
        print (" Failed")#line:267
        winsound .Beep (1000 ,1000 )#line:268
    try :#line:270
        print (f"[*] Checking Encryption Algorithm ...",end ="")#line:271
        if callable (encrypt ):#line:272
            print (" Success")#line:273
            winsound .Beep (1000 ,200 )#line:274
            OO00OOOO0000OO0O0 +=1 #line:275
    except :#line:276
        print (" Failed")#line:277
        winsound .Beep (1000 ,1000 )#line:278
    try :#line:280
        print (f"[*] Checking Decryption Algorithm ...",end ="")#line:281
        if callable (decrypt ):#line:282
            print (" Success")#line:283
            winsound .Beep (1000 ,200 )#line:284
            OO00OOOO0000OO0O0 +=1 #line:285
    except :#line:286
        print (" Failed")#line:287
        winsound .Beep (1000 ,1000 )#line:288
    try :#line:290
        print ("[*] Loading KEY Generator ...",end ="")#line:291
        if callable (keygen_make ):#line:292
            print (" Success")#line:293
            winsound .Beep (1000 ,200 )#line:294
            OO00OOOO0000OO0O0 +=1 #line:295
    except :#line:296
        print (" Failed")#line:297
        winsound .Beep (1000 ,1000 )#line:298
    try :#line:300
        print (f"[*] Running KEY Hash ...",end ="")#line:301
        if callable (keygen_hash ):#line:302
            print (" Success")#line:303
            winsound .Beep (1000 ,200 )#line:304
            OO00OOOO0000OO0O0 +=1 #line:305
    except :#line:306
        print (" Failed")#line:307
        winsound .Beep (1000 ,1000 )#line:308
    try :#line:310
        print (f"[*] Check out additional systems ...",end ="")#line:311
        if callable (make_update ):#line:312
            print (" Success")#line:313
            winsound .Beep (1000 ,200 )#line:314
            OO00OOOO0000OO0O0 +=1 #line:315
    except :#line:316
        print (" Failed")#line:317
        winsound .Beep (1000 ,1000 )#line:318
    return OO00OOOO0000OO0O0 #line:319
if __name__ =="__main__":#line:321
    os .system ('mode 60,37')#line:322
    if init ()>5 :#line:323
        Finished ()#line:324
        try :#line:325
            main ()#line:326
        except KeyboardInterrupt :#line:327
            exit ()#line:328
        except :#line:329
            pass #line:330
    else :#line:331
        print ("\n\nAn error occurred while running the TOKE system,\nContact: https://github.com/rahmatagungj/toke")#line:332
        time .sleep (60 )#line:333
        exit ()