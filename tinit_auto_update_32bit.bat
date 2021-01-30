@ECHO OFF
mode 60,37
title TOKE - Two Original Key Encryption
TASKKILL /f /im "TOKE_32bit.exe"
cls
timeout /t 1
DEL "TOKE_32bit.exe"
ren "temp_TOKE_32bit.exe" "TOKE_32bit.exe"
cls