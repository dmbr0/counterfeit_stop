#!/usr/bin/env python
import strgen
from bip38 import *
from bitcoin import *
from qrcode import *
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from fpdf import FPDF

batch_num = raw_input("Please enter a batch ID:")
serialqty = input("How many products would you like to mark?:")
wallets = []
serials = strgen.StringGenerator("[\d\w]{7}").render_list(serialqty,unique=True)

for serial in serials:
    serial = serial.encode('utf-8')
    pasw = serial
    priv = random_key()
    wif = encode_privkey(priv, 'wif')
    addr = privtoaddr(wif)
    bip = bip38_encrypt(wif,pasw)

    #image...
    img = Image.open("background.jpg") #around 1000 x 500
    img_w, img_h = img.size

    #QR image for addr
    qr = QRCode(box_size=4, border=3, error_correction=ERROR_CORRECT_Q) 
    qr.add_data(addr)
    im = qr.make_image()
    im_w, im_h = im.size

    #QR image for key
    qr2 = QRCode(box_size=4, border=3, error_correction=ERROR_CORRECT_M) 
    qr2.add_data(bip)
    im2 = qr2.make_image()
    im2_w, im2_h = im2.size

    #draw QRs
    offs = (img_w - im_w - im2_w) / 4
    img.paste(im, (offs,(img_h-im_h)/2) )
    img.paste(im2, (im_w+(3*offs),(img_h-im2_h)/2) )

    #draw labels
    draw = ImageDraw.Draw(img) 
    font = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf",22)
    fcolor =  (0,0,0)
    draw.text((im_w+(3*offs),(img_h-im_h)/3-10), 'BIP38 Key', fcolor, font)
    draw.text((20, 20), 'SERIAL:  ' + serial, fcolor, font)
    draw.text((20, 70), 'ADDRESS:  ' + addr, fcolor, font)
    draw.text((20, (img_h - 100)), 'BIP38 KEY:  ' + bip, fcolor, font)
    os.mkdir(batch_num)
    img.save(batch_num+'/'+addr+'.jpg', "JPEG")
    

    print " "
    print "==============================================================="
    print " Encrypted paper wallet (image file) created."
    print " "
    print 'Bitcoin address:' + addr
    print 'Encrypted key:' + bip
    print 'Serial:' + serial
    print " "
    print " (To decrypt, run 'python unlock-bip38.py')"
    print "==============================================================="
