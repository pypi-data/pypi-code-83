# coding=utf-8

import platform
import sys

import cv2
import pyperclip
import pyscreenshot
import qrcode
from PIL import Image
from pyzbar import pyzbar


def generate(args):
    if args.string is not None:
        content = args.string
    elif args.clipboard:
        content = pyperclip.paste()
        print(content)
    else:
        content = args.file.read()
        print(content)
    if args.screen:
        qrcode.make(content).show()
    elif args.output_file is sys.stdout:
        print(qr_str(content))
    else:
        qrcode.make(content).save(args.output_file.name)


def scan(args):
    result = []
    if args.file is not None:
        img = Image.open(args.file)
        result = pyzbar.decode(img)
    elif args.camera:
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            result = pyzbar.decode(frame)
            if len(result) != 0:
                break
        cap.release()
    elif args.screen:
        img = pyscreenshot.grab()
        result = pyzbar.decode(img)
    if len(result) == 0:
        print('No qrcode detected.')
    texts = ''
    for decoded in result:
        text = decoded.data.decode()
        if texts != '':
            texts += '\n'
        texts += text
        print(text)
    if args.clipboard:
        pyperclip.copy(texts)


def qr_str(content):
    if platform.system() == "Windows":
        white_block = '▇'
        black_block = '  '
        new_line = '\n'
    else:
        white_block = '\033[0;37;47m  '
        black_block = '\033[0;37;40m  '
        new_line = '\033[0m\n'

    qr = qrcode.QRCode()
    qr.add_data(content)
    qr.make()
    output = white_block * (qr.modules_count + 2) + new_line
    for mn in qr.modules:
        output += white_block
        for m in mn:
            if m:
                output += black_block
            else:
                output += white_block
        output += white_block + new_line
    output += white_block * (qr.modules_count + 2) + new_line
    return output
