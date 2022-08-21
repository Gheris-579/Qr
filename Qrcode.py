##!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import qrcode
from termcolor import colored
import pyperclip as py
from pyfiglet import Figlet
import webbrowser




qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=10,
                   border=1)



print('\n')
f = Figlet(font='binary')
print(colored(f.renderText('Qr code'.center(40)), 'yellow'))




while True:
    print(colored('Write your link  Or your phone number ','yellow'))
    link = input()
    qr.make(fit=True)
    qr.add_data(link)
    print('Your link is correct ' + link)
    Yes_No = input(colored("Yes or NO:\n",'red')).lower()
    if Yes_No == 'Yes':
        break
    elif Yes_No == 'No':
        continue

def main():
    global img
    while True:
        try:
            print("\nChoose the color to put on the QR code")
            color = input()
            img = qr.make_image(fill_color=color, back_color='white')
            break
        except ValueError:
            print("\nIf you don't know which color to choose go to this link https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F")
            py.copy('https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F')
            webbrowser.open("https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F")
            continue

    print('What do you want to name the file to save' "\n don't forget to put either .png or .jpg at the end")
    file = input()
    print('Your file has been called ' + file)
    img.save(file)
    print('\n')

main()














