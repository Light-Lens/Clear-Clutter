@ECHO OFF

title Compile Clear Clutter
echo Compiling Clear Clutter.

pyinstaller.exe --icon=Icon.ico --onefile main.py
move dist\main.exe ".\Clear Clutter.exe"

rmdir /s /q dist
rmdir /s /q build
rmdir /s /q __pycache__

del main.spec

cls
if EXIST ".\Clear Clutter.exe" goto Compiled
if NOT EXIST ".\Clear Clutter.exe" goto NotCompiled

:Compiled
echo Clear Clutter Compiled Successfully!
echo Get ready to Clear all your Desktop Clutter!
echo|set /p="Continue."
pause >nul
exit

:NotCompiled
echo Can't Compile Clear Clutter!
echo|set /p="Continue."
pause >nul
exit
