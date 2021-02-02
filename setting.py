# Copyright (c) 2020-2021 Rahmat Agung Julians

import random,time,os,sys,datetime,winsound,multiprocessing,urllib.request,ctypes,threading,win32api
from tkinter import *
from datetime import date
import colorama,re
from colorama import Fore,Back,Style
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename
from playsound import playsound

import win32file
import pywintypes

# main logic function
def changeFileCreateTime(path, ctime):
    # path: your file path
    # ctime: Unix timestamp

    # open file and get the handle of file
    # API: http://timgolden.me.uk/pywin32-docs/win32file__CreateFile_meth.html
    handle = win32file.CreateFile(
        path,                          # file path
        win32file.GENERIC_WRITE,       # must opened with GENERIC_WRITE access
        0,
        None,
        win32file.OPEN_EXISTING,
        0,
        0
    )

    # create a PyTime object
    # API: http://timgolden.me.uk/pywin32-docs/pywintypes__Time_meth.html
    PyTime = pywintypes.Time(ctime)

    # reset the create time of file
    # API: http://timgolden.me.uk/pywin32-docs/win32file__SetFileTime_meth.html
    win32file.SetFileTime(
        handle,
        PyTime
    )

# example
changeFileCreateTime('folder_structure.txt',202001010)
print('oke')
time.sleep(60)