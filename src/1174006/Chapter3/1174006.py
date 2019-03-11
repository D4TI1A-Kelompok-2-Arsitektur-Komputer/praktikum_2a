# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:16:00 2019

@author: divakrishna
"""

#Pemahaman Teori
#Jawaban No. 1
def namaFungsi(inputanFungsi):
    return inputanFungsi

output = namaFungsi("Kembalian Fungsi")
print(output)

#Jawaban No. 2
import math
print("Nilai pi adalah: ", math.pi)

#Jawaban No. 3
class Mahasiswa:
    jumlahMahasiswa = 0
    
    def __init__(self, npm, nama):
        self.npm = npm
        self.nama = nama
        Mahasiswa.jumlahMahasiswa +=1
            
    def tampilkanProfil(self):
        print("NPM :", self.npm)
        print("Nama :", self.nama)
        print()

mahasiswa1 = Mahasiswa("1174006", "Diva Krishna")
mahasiswa2 = Mahasiswa("1174001", "Indah Pramesti")

mahasiswa1.tampilkanProfil()
mahasiswa2.tampilkanProfil()

print("Total mahasiswa adalah ", Mahasiswa.jumlahMahasiswa)

#Jawaban No. 4
from Mahasiswa import Mahasiswa

mhs1 = Mahasiswa("1174006", "Diva Krishna")
mhs2 = Mahasiswa("1174001", "Indah Pramesti")

mhs1.tampilkanProfil()
mhs2.tampilkanProfil()

print("Total mahasiswa adalah ", Mahasiswa.jumlahMahasiswa)

#Jawaban No. 5
from kalkulator import Penambahan

hasil = Penambahan(10, 5)
print(hasil)

#Jawaban No. 6
from folder import kalkulator

a=100
b=50

hasil1=kalkulator.Penambahan(a,b)
hasil2=kalkulator.Pengurangan(a,b)
hasil3=kalkulator.Perkalian(a,b)
hasil4=kalkulator.Pembagian(a,b)

print(hasil1)
print(hasil2)
print(hasil3)
print(hasil4)

#Jawaban No. 7
from folder.Mahasiswa import Mahasiswa

mhs1 = Mahasiswa("1174006", "Diva Krishna")
mhs2 = Mahasiswa("1174001", "Indah Pramesti")

mhs1.tampilkanProfil()
mhs2.tampilkanProfil()

print("Total mahasiswa adalah ", Mahasiswa.jumlahMahasiswa)

#Ketrampilan Pemrograman
#Jawaban No. 1
def printNPM(npm):
    
    npm = list(str(npm))
    
    angka1 = {"0":" ###### ", "1":"  ##", "2":" ####### ", "3":" ####### ", "4":"     ###", "5":"########", "6":" ####### ", "7":"#########", "8":" ####### ", "9":" #######"}
    angka2 = {"0":"###  ###", "1":"####", "2":"##    ###", "3":"##    ###", "4":"   #####", "5":"##      ", "6":"###      ", "7":"     ### ", "8":"###   ###", "9":"##    ###"}
    angka3 = {"0":"###  ###", "1":" ###", "2":"     ### ", "3":"    #### ", "4":" ###  ##", "5":"####### ", "6":"######## ", "7":"    ###  ", "8":" ### ### ", "9":"##    ###"}
    angka4 = {"0":"###  ###", "1":" ###", "2":"    ###  ", "3":"    #### ", "4":"########", "5":"     ###", "6":"###   ###", "7":"   ###   ", "8":" ### ### ", "9":" ########"}
    angka5 = {"0":"###  ###", "1":" ###", "2":"  ####   ", "3":"##    ###", "4":"     ###", "5":"##   ###", "6":"###   ###", "7":"  ###    ", "8":"###   ###", "9":"      ###"}
    angka6 = {"0":" ###### ", "1":" ###", "2":"#########", "3":" ####### ", "4":"     ###", "5":" ###### ", "6":" ####### ", "7":" ###     ", "8":" ####### ", "9":" ####### "}
              
    hasil1 = []
    hasil2 = []
    hasil3 = []
    hasil4 = []
    hasil5 = []
    hasil6 = []
              
    for x in npm:
        hasil1.append(angka1[x])
        hasil2.append(angka2[x])
        hasil3.append(angka3[x])
        hasil4.append(angka4[x])
        hasil5.append(angka5[x])
        hasil6.append(angka6[x])
    
    print(*hasil1, sep=' ')
    print(*hasil2, sep=' ')
    print(*hasil3, sep=' ')
    print(*hasil4, sep=' ')
    print(*hasil5, sep=' ')
    print(*hasil6, sep=' ')
    
printNPM(input("Masukan NPM anda: "))

#Jawaban No. 2
def printNPMDuaDijit(npm):
    ulang = 1
    sampai = int(npm[5:7])
    while(ulang <= sampai):
        print("Halo, "+str(npm)+" apa kabar?")
        ulang += 1

printNPMDuaDijit(input("Masukan NPM anda: "))        

#Jawaban No. 3
def printNPMTigaDijit(npm):
    ulang = 1
    sampai = list(map(int, npm[4:7]))
    sampai = sum(sampai)    
    while(ulang <= sampai):
        print("Halo, "+str(npm[-3:])+" apa kabar?")
        ulang += 1
    
printNPMTigaDijit(input("Masukan NPM anda: "))

#Jawaban No. 4
def printNPMDigitKetiga(npm):
    print("Output:")
    print("Halo, "+str(npm[-3])+" apa kabar?")
    
printNPMDigitKetiga(input("Input: "))

#Jawaban No. 5
def printNPMSatuPersatu(npm):
    npm = list(map(int, npm))  
    for n in npm:
        print(n)
        
printNPMSatuPersatu(input("Masukan NPM anda: "))

#Jawaban No. 6
def printNPMPenjumlahan(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil += x
    
    print(hasil)
    
printNPMPenjumlahan(input("Masukan NPM anda: "))
    
#Jawaban No. 7
def printNPMPerkalian(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil *= x
    
    print(hasil)
    
printNPMPerkalian(input("Masukan NPM anda: "))

#Jawaban No. 8
def printNPMDijitGenap(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end = "")
    
printNPMDijitGenap(input("Masukan NPM anda: "))

#Jawaban No. 9
def printNPMDijitGanjil(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 != 0):
            print(n, end = "")
    
printNPMDijitGanjil(input("Masukan NPM anda: "))

#Jawaban No. 10
def printNPMDijitPrima(npm):
    npm = list(map(int, npm))
    prima = []
    for n in npm:
        isPrime = True
        if n == 0 or n == 1:
            isPrime = False
        for x in range(2, n):
            if n % x == 0:
                isPrime = False
        if isPrime:
            prima.append(n)

    for p in prima:
        print(p, end = "")
    
printNPMDijitPrima(input("Masukan NPM anda: "))

#Jawaban No. 11

#Jawaban No. 12

#Ketrampilan Penanganan Error
#Jawaban No. 1
def sapa(nama):
    try:
        print("Hallo, "+str(nama))
    except:
        print("Terjadi error") 

sapa(input("Masukan nama anda: "))