#!/usr/bin/env python
import strgen
from bip38 import *
from bitcoin import *

batch_num = input("Please enter a batch ID:")
serialqty = input("How many products would you like to mark?:")

serials = strgen.StringGenerator("[\d\w]{7}").render_list(serialqty,unique=True)

for serial in serials:
    serial = serial.encode('utf-8')
    pasw = serial
    priv = random_key()
    priv2 = decode_privkey(priv,'hex')
    wif = encode_privkey(priv, 'wif')
    addr = privtoaddr(priv)
    bip = bip38_encrypt(priv,pasw)
    print(bip,serial)