#x = 0x7c3e2075 # cntlz
x = 0x7c389191
x = 0x7c3ac026 # mfcr 1
x = 0x7ed3d1d5 # addme
x = 0x7c314e17 # modsw
x = 0x7e3cb026 # mfcr 17
x = 0x7e698027 # mfcr 19
x = 0x7cd04d95 # addzeo.
x = 0x7ed3d1d5 # addme.
x = 0x7cb2d413 # minor 19
x = 0x7cb7c0d1 # minor 104
x = 0x7cbce174 # minor 106
x = 0x7cbe51d1 # minor 232
x = 0x7cb43734
x = 0x48010000
x = 0x7cb87826 # mfocr 5 
x = 0x7e698027 # mfcr 19
x = 0x7eefdc34 # cntlzw 23, 15
x = 0x7c79d213 # modud 3, 25, 26
x = 0x7ccc7827
x = 0x7fc12c97 # mulhwo. 30, 1, 5
x = 0x7ca33595 # addzeo. 5,3,6
x = 0x4d950343 # crorc 12, 21, 0
x = 0x7e33ffb5 # extswo. 
x = 0x7e4cd7b4
x = 0x7d335840 # cmpld    10428
x = 0x7c0d6074
x = 0x4c0fe12d # stwcx.
x = 0x7e33ffb5 # extsw. 19, 17
x = 0x7d96d921
x = 0x7f3b2195 # addzeo 25, 27, 4 116ac
#x = 0x7c2c9475
x = 0x4f855b83  # cror 28, 5, 11
x = 0x7ed56735  # extsh. 22, 21       115b0
x = 0x7d99d02d  # icbt?   115a4
x = 0x7cd15040  # cmpl 6, 0, 17, 10   115b8
x = 0x40490008  # bc      2,4*cr2+gt,0x11fbc  - bc 2, 9, 8
x = 0x7d211027  # mfcr 9        125a8:   27 10 21 7d     .long 0x7d211027
x = 0x7d4f2027  #         1494c:   27 20 4f 7d     .long 0x7d4f2027
x = 0x7e100921







x = bin(x)[2:]
while len(x) != 32:
    x = '0' + x
print ("major", int(x[0:6], 2))
print ("minor", int(x[22:31], 2), x[22:31])
print ("minor21-31", int(x[21:31], 2), x[21:31])
print ("Oe", int(x[21], 2))
print ("bit 11, 12-19", int(x[11], 2), x[12:20])
print ("rt", int(x[6:11], 2))
print ("    bf", int(x[6:9], 2))
print ("    bit 10, L", x[10])
print ("ra", int(x[11:16], 2))
print ("rb", int(x[16:21], 2))
print ("Rc", int(x[31], 2))
