import os
import subprocess as sp

paths = {
    'notepad': "shell:AppsFolder\\Microsoft.WindowsNotepad_8wekyb3d8bbwe!App",
    # Update the path if Discord is installed
    # 'discord': "C:\\Users\\pk612\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def open_notepad():
    os.system(paths['notepad'])  # Works for Windows Store apps

# def open_discord():
#     os.startfile(paths['discord'])  # Uncomment if Discord path is set

def open_cmd():
    os.system('start cmd')

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_calculator():
     sp.Popen(paths['calculator'])
import psutil


