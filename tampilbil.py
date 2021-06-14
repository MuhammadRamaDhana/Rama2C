# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 21:12:04 2021

@author: ASUS
"""

#Menampilkan nilai huruf dengan Menginputkan sebuah bilangan bulat dari 0-100

jwbulangprog= "y"
while jwbulangprog=="y" or jwbulangprog=="Y":
    print("===========================")
    print(">>> CEK NILAI HURUF")
    print("===========================")
    
    n = input(">> Input nilai = ")
    #cek batasan inputan nilai 0-100
    if int(n)>0 and int(n)<=100:
        if int(n)>80: sts="BAIK SEKALI"
        elif int(n)>=65: sts="BAIK"
        elif int(n)>=55: sts="CUKUP BAIK"
        elif int(n)>=40: sts="KURANG"
        else:
            sts="KURANG SEKALI"
        print(sts)  
    else: 
        pesan=">>> Masukkan nilai 0-100 saja"
        print(pesan)
    jwbulangprog = input(">>> ulang program? y/t = ")
    if jwbulangprog=="t" or jwbulangprog=="T":
        break
     
        
    