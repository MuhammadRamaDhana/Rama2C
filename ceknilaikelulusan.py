# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
jwb = "y"
while jwb =="y" or jwb=="Y":
    print("==========================")
    print("      CEK KELULUSAN NILAI")
    print("==========================")
    n = input(">> Masukkan nilai anda = ")
    #cek nilai
    if int(n)>60:
        sts = "lulus"
        
    else:
        sts = "Tidak Lulus"
        
    print(sts)
    
    #inputn untuk break
    jwb = input(">> Mulai Lagi? y/t =")
    if jwb=="t" or jwb  =="T":
        break 