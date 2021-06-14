    #cek total trasanksi pembelian printer Epson T20
ulangprog = "y"
while ulangprog=="y" or ulangprog=="Y":

    hargaprinter=660000
    print("*************************************************")
    print(" CEK TOTAL TRANSAKSI PEMBELIAN PRINTER EPSON T20 ")
    print("*************************************************")
    #input jumlah printer
    jumlahbeli=input("masukan jumlah printer Epson T20 yang dibeli = ")

    #menghitung total transaksi
    total = int(hargaprinter)*int(jumlahbeli)
    
    print("total pembelian printer epson T20 = Rp " + str(total))
    
    ulangprog = input(">> ulang program ? y/t = ")  
    if ulangprog=="t" or ulangprog=="T":
        break     
    