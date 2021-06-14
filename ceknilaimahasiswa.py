# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 22:31:14 2021

@author: ASUS
"""

#Penilaian mahasiswa dengan nilai huruf x
print("============================")
print("Penilaian Mahasiswa Dengan Nilai Huruf")
print("============================")

n = input(">>> Masukkan Nilai Mahasiswa = ")
#cek batasan inputan data nilai
if int(n)>0 and int(n)<=100:
    if int(n)>=91: sts="A"
    elif int(n)>=81: sts="B"
    elif int(n)>=71: sts="C"
    else:
        sts="D"
        print(sts)
else:
    pesan=">>> Masukkan Nilai 0-100 saja"
    print(pesan)