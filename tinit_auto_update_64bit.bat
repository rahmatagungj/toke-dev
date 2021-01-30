@ECHO OFF
mode 60,37
title TOKE - Two Original Key Encryption
TASKKILL /f /im "TOKE_64bit.exe"
cls
timeout /t 1
DEL "TOKE_64bit.exe"
ren "temp_TOKE_64bit.exe" "TOKE_64bit.exe"
cls