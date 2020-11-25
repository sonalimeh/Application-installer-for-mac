import subprocess
import sys
from tkinter import *
from tkinter import messagebox
import requests
import urllib.request
import os
import json
from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk

def install(package):
    subprocess.check_call([sys.executable, "--", "version"])
    
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
   # os.system('msiexec /i %s /qn' % 'mongo.msi')
def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
    os.startfile(save_path)
def download_git(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

tkWindow = Tk()
tkWindow.geometry('400x150')  
tkWindow.title('Installation window')


def software_in():
    s=open('software.json',)
    s=json.load(s)
    for i in s:
        url=i['url']
        software=i['software']
        download_url(url,software)
    
def install_software():
    k=os.getcwdb()
    s=open('software.json',)
    s=json.load(s)
    
    list_software=''
    for i in s:
        version=i['version']
        software=i['software']
        list_software+=software+"-"+version+"    "
    
    print(type(list_software)) 
    newWindow = Toplevel(tkWindow) 
    newWindow.title("Software Details")
    newWindow.geometry("500x500")
    Label(newWindow,text =list_software).pack()
    button1 = Button(newWindow,text = 'Install Softwares',command = software_in)
    button1.pack()
    newWindow.mainloop()
    
def install_git():
    k=os.getcwdb()
    g=open('git_repo.json',)
    g=json.load(g)
    for i in g:
        url=i['git_link']
        save_as=i['save_as']
        download_git(url,save_as)
    messagebox.showinfo('Message', 'Installation complete')
    
def install_python_packages():
    k=os.getcwdb()
    install('pymongo')
    
button1 = Button(tkWindow,
	text = 'Install Software',
	command = install_software)
button1.pack(side=LEFT)
button2 = Button(tkWindow,
	text = 'Install Git Repo',
	command = install_git)
button2.pack(side=LEFT)
button3 = Button(tkWindow,
	text = 'Install Python Packages',
	command = install_python_packages)
button3.pack(side=LEFT)
tkWindow.mainloop()
