from os import system
#HEADER
print(
"""
       +================================+
       |                                |
       |       Welcome to PyFit!        |
       |                                |
       +================================+
""")
print(
"""
   +==========================================+
   |        Program Untuk Mengetahui          |
   |   Indeks Massa Tubuh, Persentase Lemak,  |
   |      dan Kategori Massa Tubuh Anda       |
   +==========================================+
""")

#fungsi untuk menghitung indeks massa tubuh (IMT)
def indeks_massa():

    #list kosong untuk menampung hasil perhitungan indeks massa masing-masing data pada setiap perulangan
    list_IMT = []
    print()

    #keterangan perhitungan indeks massa
    print("MENGHITUNG INDEKS MASSA TUBUH".center(50, "+"))

    #user input satuan yang ingin digunakan dan banyak data yang ingin dihitung
    satuan = int(input("\nPilih satuan yang ingin digunakan : \n[1]inci / lbs\n[2]meter / kg\n[3]Kembali memilih jenis kelamin\nMasukkan angka sesuai dengan satuan yang dipilih = "))
    if satuan == 3:
        print()
        main()
    frekuensi = int(input("Masukkan banyak orang yang akan dihitung = "))
    if frekuensi <= 0:
        print("Frekuensi tidak valid")
        indeks_massa()
    print()

    #perhitungan untuk opsi 1 (satuan inci / lbs)
    if satuan == 1:
        print("Masukkan angka [0] untuk kembali memilih jenis kelamin")
        #perulangan sebanyak jumlah data yang diinginkan user
        for i in range(frekuensi):
            #user input massa dan tinggi badan masing-masing data
            massa = float(input(f"Masukkan berat badan untuk orang ke-{i+1} (lbs) = "))
            if massa == 0:
                print()
                main()

            tinggi = float(input(f"Masukkan tinggi badan untuk orang ke-{i+1} (inci)=  "))
            if tinggi == 0:
                print()
                main()

            #perhitungan indeks massa satuan imperial, dibulatkan 2 angka di belakang koma
            IMT = 703 * (massa / (tinggi*tinggi))
            IMT_bulat = round(IMT, 2)

            #hasil indeks massa pada setiap perulangan dimasukkan ke list indeks massa
            list_IMT.append(IMT_bulat)   

        #mencetak indeks massa tubuh untuk masing-masing data
        print()
        print("INDEKS MASSA TUBUH MASING-MASING DATA".center(50, "+"))
        for i  in range(len(list_IMT)):
            print(f"Indeks Massa Tubuh Orang ke-{i+1} = {list_IMT[i]}")  

    #perhitungan untuk opsi 2 (satuan meter / kg)
    elif satuan == 2:
        print("Masukkan angka [0] untuk kembali memilih jenis kelamin")
        #perulangan sebanyak jumlah data yang diinginkan user
        for i in range(frekuensi):
            #user input massa dan tinggi badan masing-masing data
            massa = float(input(f"Masukkan berat badan untuk orang ke-{i+1} (kg) = "))
            if massa == 0:
                print()
                main()

            tinggi = float(input(f"Masukkan tinggi badan untuk orang ke-{i+1} (meter)=  "))
            if tinggi == 0:
                print()
                main()

            #perhitungan indeks massa satuan metrik, dibulatkan 2 angka di belakang koma
            IMT = massa / (tinggi*tinggi)
            IMT_bulat = round(IMT, 2)

            #hasil indeks massa pada setiap perulangan dimasukkan ke list indeks massa
            list_IMT.append(IMT_bulat)  

        #mencetak indeks massa tubuh untuk masing-masing data
        print()
        print("INDEKS MASSA TUBUH MASING-MASING DATA".center(50, "+"))
        for i  in range(len(list_IMT)):
            print(f"Indeks Massa Tubuh Orang ke-{i+1} = {list_IMT[i]}")   

    #jika opsi yang dimasukkan tidak valid atau tidak tersedia
    else:
        print("opsi satuan tidak tersedia atau tidak valid")
        return indeks_massa()
    
    #menyimpan hasil atau isi dari list indeks massa untuk perhitungan persentase lemak
    return list_IMT

#fungsi untuk menghitung persentase lemak jika user memilih jenis kelamin pria
def persen_lemak_pria(list_IMT):   

    #keterangan perhitungan persentase lemak 
    print()
    print("MENGHITUNG PERSEN LEMAK TUBUH PRIA".center(50, "~"))

    #list kosong untuk menyimpan hasil perhitungan persentase lemak pria
    lemak_percent_pria = []
    print()

    #perulangan sebanyak jumlah indeks dari list indeks massa
    print("Masukkan angka [0] untuk kembali memilih jenis kelamin")
    for i in range(len(list_IMT)):
        #user input umur masing-masing data
        umur = int(input(f"Masukkan usia pria ke-{i+1} = "))
        if umur == 0:
            print()
            main()

        #perhitungan persentase lemak pria, hasil dibulatkan 2 angka di belakang koma
        lemak_percent = (1.20 * list_IMT[i]) + (0.23 * umur) - 16.2
        percent_bulat = round(lemak_percent, 2)

        #hasil persentase lemak pria setiap perulangan dimasukkan ke list persentase lemak pria
        lemak_percent_pria.append(percent_bulat)  

    #mencetak persentase lemak masing-masing data
    print()
    print("PERSENTASE LEMAK MASING-MASING DATA".center(50, "~"))
    for i in range(len(lemak_percent_pria)):
        print(f"Persentase lemak tubuh pria ke-{i+1} = {lemak_percent_pria[i]}%")

    #menyimpan isi list persentase lemak pria untuk status tubuh pria
    return lemak_percent_pria

#fungsi untuk menghitung persentase lemak jika user memilih jenis kelamin wanita
def persen_lemak_wanita(list_IMT):

    #keterangan perhitungan persentase lemak 
    print()
    print("MENGHITUNG PERSEN LEMAK TUBUH WANITA".center(50, "~"))

    #list kosong untuk menyimpan hasil perhitungan persentase lemak wanita
    lemak_percent_wanita = []
    print()

    #perulangan sebanyak jumlah indeks dari list indeks massa
    print("Masukkan angka [0] untuk kembali memilih jenis kelamin")
    for i in range(len(list_IMT)):
        #user input umur masing-masing data
        umur = int(input(f"Masukkan usia wanita ke-{i+1} = "))
        if umur == 0:
            print()
            main()

        #perhitungan persentase lemak wanita, dibulatkan 2 angka di belakang koma
        lemak_percent = (1.20 * list_IMT[i]) + (0.23 * umur) - 5.4
        percent_bulat = round(lemak_percent, 2)

        #hasil persentase lemak wanita setiap perulangan dimasukkan ke list persentase lemak wanita
        lemak_percent_wanita.append(percent_bulat)

    #mencetak persentase lemak masing-masing data
    print()
    print("PERSENTASE LEMAK MASING-MASING DATA".center(50, "~"))
    for i in range(len(lemak_percent_wanita)):
        print(f"Persentase lemak tubuh wanita ke-{i+1} = {lemak_percent_wanita[i]}%")

    #menyimpan isi list persentase lemak wanita untuk status tubuh wanita
    return lemak_percent_wanita

#fungsi untuk menentukan kategori massa tubuh
def kategori_massa_pria(lemak_percent_pria):

    #keterangan untuk menunjukkan kategori massa tubuh masing-masing data
    print()
    print("KATEGORI MASSA TUBUH MASING-MASING DATA".center(50, "="))

    #perulangan sebanyak jumlah indeks pada list persentase lemak pria
    for i in range(len(lemak_percent_pria)):

        #kondisi untuk menentukan masing-masing kategori massa tubuh pria
        if lemak_percent_pria[i] < 8 :
            print(f"Massa tubuh pria ke-{i+1} jauh di bawah normal (sangat kurus)")
        elif 8 <= lemak_percent_pria[i] < 12 :
            print(f"Massa tubuh pria ke-{i+1} di bawah normal (kurus)")
        elif 12 <= lemak_percent_pria[i] < 20 :
            print(f"Massa tubuh pria ke-{i+1} normal")
        elif 20 <= lemak_percent_pria[i] < 25 :
            print(f"Massa tubuh pria ke-{i+1} berlebihan (gemuk)")
        elif 25 <= lemak_percent_pria[i] < 35 :
            print(f"Massa tubuh pria ke-{i+1} sangat berlebihan (obesitas kelas I)")
        elif 35 <= lemak_percent_pria[i] < 40:
            print(f"Massa tubuh pria ke-{i+1} ekstrem (obesitas kelas II)")
        elif 40 <= lemak_percent_pria[i] :
            print(f"Massa tubuh pria ke-{i+1} sangat ekstrem (obesitas kelas III)")
    
    #mencetak pembatas akhir program
    print()
    print("(*Kategori yang dihasilkan merupakan perkiraan kasar)".ljust(50, "-"))
    print(" ".ljust(50, "-"))
    print()


#fungsi untuk menentukan kategori massa tubuh
def kategori_massa_wanita(lemak_percent_wanita):
    #keterangan untuk menunjukkan kategori massa tubuh masing-masing data
    print()
    print("KATEGORI MASSA TUBUH MASING-MASING DATA".center(50, "="))
    
    #perulangan sebanyak jumlah indeks pada list persentase lemak pria
    for i in range(len(lemak_percent_wanita)):
        #kondisi untuk menentukan masing-masing kategori massa tubuh pria
        if lemak_percent_wanita[i] < 18 :
            print(f"Massa tubuh wanita ke-{i+1} jauh di bawah normal (sangat kurus)")
        elif 18 <= lemak_percent_wanita[i] < 22:
            print(f"Massa tubuh wanita ke-{i+1} di bawah normal (kurus)")
        elif 22 <= lemak_percent_wanita[i] < 30:
            print(f"Massa tubuh wanita ke-{i+1} normal")
        elif 30 <= lemak_percent_wanita[i] < 35:
            print(f"Massa tubuh wanita ke-{i+1} berlebihan (gemuk)")
        elif 35 <= lemak_percent_wanita[i] < 40:
            print(f"Massa tubuh wanita ke-{i+1} sangat berlebihan (obesitas kelas I)")
        elif 40 <= lemak_percent_wanita[i] < 45:
            print(f"Massa tubuh wanita ke-{i+1} ekstrem (obesitas kelas II)")
        elif 45 <= lemak_percent_wanita[i]:
            print(f"Massa tubuh wanita ke-{i+1} sangat ekstrem (obesitas kelas III)")
    print()
    print("(*Kategori yang dihasilkan merupakan perkiraan kasar)".ljust(50, "-"))
    print(" ".ljust(50, "-"))
    print()

#fungsi untuk memanggil masing-masing fungsi sebelumnya
def main():

    #keterangan awal
    print("MASUKKAN OPSI SESUAI KETERANGAN YANG TERTERA".center(50, "*"))

    #user input jenis kelamin untuk perhitungan persentase lemak
    jenis_kelamin = int(input("\nPilih jenis kelamin untuk data yang akan dihitung\n[1]Pria\n[2]Wanita\nAtau masukkan angka [3] untuk keluar = "))

    #kondisi jika jenis kelamin yang dipilih adalah pria[1]
    if jenis_kelamin == 1:
        system('cls')
        #memanggil fungsi indeks_massa untuk mendapat isi list indeks massa tubuh
        list_IMT = indeks_massa()

        #memanggil fungsi persen_lemak_pria menggunakan list indeks massa tubuh untuk mendapat isi list persentase lemak pria
        lemak_percent_pria = persen_lemak_pria(list_IMT)
  
        #memanggil fungsi kategori tubuh pria untuk mendapat kategori massa tubuh masing-masing data
        kategori_massa_pria(lemak_percent_pria)
    
    #kondisi jika jenis kelamin yang dipilih adalah wanita[2]
    elif jenis_kelamin == 2:
        system('cls')
        #keterangan bahwa list indeks massa didapat dari fungsi indeks massa()
        list_IMT = indeks_massa()

        #keterangan bahwa list persentase lemak wanita didapat dari fungsi persen_lemak_wanita dengan menggunakan nilai pada list indeks massa
        lemak_percent_wanita = persen_lemak_wanita(list_IMT)

        #keterangan bahwa fungsi kategori_massa_wanita menggunakan nilai dari list persentase lemak wanita dan list indeks massa
        kategori_massa_wanita(lemak_percent_wanita)

    #kondisi jika user memasukkan angka 3, yaitu program akan ditutup
    elif jenis_kelamin == 3:
        exit()

#kondisi jika file dijalankan sebagai program utama
if __name__ == "__main__":
    #fungsi main akan terus dijalankan selama user belum keluar dari program
    while (True):
        main()