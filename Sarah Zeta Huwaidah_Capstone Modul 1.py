from tabulate import tabulate

def menampilkan():
    while True:
        menu_tampil=input('''
                    SUB-MENU MENAMPILKAN DATA HASIL PANEN:
                    1. Menampilkan semua data hasil panen
                    2. Menampilkan data hasil panen tertentu
                    3. Kembali ke menu utama
                    Silahkan pilih nomor sub-menu yang ingin dijalankan: ''')
        
        if menu_tampil == '1':
            if hasil_panen != []:
                tabel_data_panen()
            elif hasil_panen == []:
                print('\n')
                print('Data tidak tersedia. Harap menambahkan data terlebih dahulu!')
             
        elif menu_tampil == '2':
            tampil_by_id()
            while True:
                print('\n')
                checker_id_tampil=input('Apakah ingin melihat data hasil panen lain?(Ya/Tidak) ').capitalize()
                if checker_id_tampil == 'Ya':
                    tampil_by_id()
                elif checker_id_tampil == 'Tidak':
                    break
                else:
                    print('\n')
                    print('Input tidak valid! mohon masukkan input "Ya" atau "Tidak"!')
                    continue
            
        elif menu_tampil == '3':
            break

        else:
            print('\n')
            print('Nomor sub-menu yang dimasukkan tidak valid! Silahkan pilih nomor yang telah ditampilkan!')
            continue

def menambah():
    while True:
        menu_tambah=input('''
                        SUB-MENU MENAMBAH DATA HASIL PANEN:
                        1. Menambah data hasil panen baru
                        2. Kembali ke menu utama
                        Silahkan pilih nomor sub-menu yang ingin dijalankan: ''')
        
        if menu_tambah == '1':
            input_tambah()

            while True:
                checker_tambah=input('Apakah ingin menambah data hasil panen lain?(Ya/Tidak) ').capitalize()

                if checker_tambah == 'Ya':
                    input_tambah()
                elif checker_tambah == 'Tidak':
                    break
                else:
                    print('Input tidak valid! mohon masukkan input "Ya" atau "Tidak"!')
                    continue
            
            while True:
                checker_simpan=input('Apakah ingin menyimpan data yang baru saja diinput?(Ya/Tidak)').capitalize()

                if checker_simpan == 'Ya':
                    print('\n')
                    print('Data berhasil disimpan!')
                    tabel_data_panen()
                    break
                elif checker_simpan == 'Tidak':
                    for item in data_baru:
                        hasil_panen.remove(item)
                    tabel_data_panen()
                    break
                else:
                    print('Input tidak valid! mohon masukkan input "Ya" atau "Tidak"!')
                    continue

        elif menu_tambah == '2':
            break

        else:
            print('\n')
            print('Nomor sub-menu yang dimasukkan tidak valid! Silahkan pilih nomor yang telah ditampilkan!')
            continue

def mengedit():
    while True:
        menu_edit=input('''
                        SUB-MENU MENGEDIT DATA HASIL PANEN:
                        1. Mengedit data hasil panen tertentu
                        2. Kembali ke menu utama
                        Silahkan pilih nomor sub-menu yang ingin dijalankan: ''')
        
        if menu_edit == '1':
            edit_data()

            while True:
                checker_edit=input('Apakah ingin mengedit data hasil panen lain?(Ya/Tidak) ').capitalize()

                if checker_edit == 'Ya':
                    edit_data()

                elif checker_edit == 'Tidak':
                    tabel_data_panen()
                    break

                else:
                    print('Input tidak valid! mohon masukkan input "Ya" atau "Tidak"!')
                    continue

        elif menu_edit == '2':
            break

        else:
            print('\n')
            print('Nomor sub-menu yang dimasukkan tidak valid! Silahkan pilih nomor yang telah ditampilkan!')
            continue

def menghapus():
    while True:
        menu_hapus=input('''
                        SUB-MENU MENGHAPUS DATA HASIL PANEN:
                        1. Menghapus data hasil panen tertentu
                        2. Kembali ke menu utama
                        Silahkan pilih nomor sub-menu yang ingin dijalankan: ''')
        
        if menu_hapus == '1':
            hapus_data()

            while True:
                if hasil_panen != []:
                    checker_hapus=input('Apakah ingin menghapus data hasil panen lain?(Ya/Tidak) ').capitalize()

                    if checker_hapus == 'Ya':
                        hapus_data()
                    elif checker_hapus == 'Tidak':
                        tabel_data_panen()
                        break
                    else:
                        print('Input tidak valid! mohon masukkan input "Ya" atau "Tidak"!')
                        continue

                elif hasil_panen == []:
                    print('\n')
                    print('Tidak ada lagi data yang dapat dihapus')
                    break
        
        elif menu_hapus == '2':
            break

        else:
            print('\n')
            print('Nomor sub-menu yang dimasukkan tidak valid! Silahkan pilih nomor yang telah ditampilkan!')
            continue

def tampil_by_id():
    while True:
        try:
            if hasil_panen != []:
                print('\n')
                id_tampil=int(input('Masukkan ID hasil panen yang ingin dilihat datanya! '))
                if 1 <= id_tampil <= len(hasil_panen):
                    table.append([id_tampil, hasil_panen[id_tampil-1][0], hasil_panen[id_tampil-1][1], hasil_panen[id_tampil-1][2], hasil_panen[id_tampil-1][3], hasil_panen[id_tampil-1][4]])
                    print(tabulate(table,headers=['ID','Hasil Panen','Kuantitas (ton)','Tanggal Masuk','Suhu Penyimpanan (°C)','Kelembaban Ruangan (%)'],tablefmt='mixed_grid',numalign='center',stralign='center'))
                    table.clear()
                    break
                else:
                    print('\n')
                    print('ID hasil panen tidak tersedia! Harap masukkan ID hasil panen yang tersedia dalam tabel hasil panen!')
                    continue
            elif hasil_panen == []:
                print('\n')
                print('Data tidak tersedia. Harap menambahkan data terlebih dahulu!')
                break

        except ValueError:
            if_value_error()
            continue

def if_value_error():
    print('\n')
    print('Input tidak valid!')

def tabel_data_panen():
    print('\n')
    print(57*'==')
    print(f'{'DATA HASIL PANEN DI PENYIMPANAN COLD STORAGE':^112}')
    print(57*'==')
    for i in range(len(hasil_panen)):
        table.append([i+1, hasil_panen[i][0], hasil_panen[i][1], hasil_panen[i][2], hasil_panen[i][3], hasil_panen[i][4]])
    print(tabulate(table,headers=['ID','Hasil Panen','Kuantitas (ton)','Tanggal Masuk','Suhu Penyimpanan (°C)','Kelembaban Ruangan (%)'],tablefmt='mixed_grid',numalign='center',stralign='center'))
    table.clear()

def input_tambah():
    while True:
        try:
            print('\n')
            nama_hasil_panen=input('Masukkan nama hasil panen baru! ').capitalize()
            for i in hasil_panen:
                if nama_hasil_panen == i[0]:
                    print(f'Data komoditas {nama_hasil_panen} sudah terdapat dalam pusat data. Mohon input nama hasil panen lain!')
                    continue
                elif nama_hasil_panen != i[0]:
                    break

        except ValueError:
            if_value_error()
            continue

        break
    
    while True:
        try:
            kuantitas=float(input(f'Masukkan kuantitas {nama_hasil_panen} dalam satuan ton! '))

        except ValueError:
            if_value_error()
            continue

        break
    
    while True:
        try:
            tanggal_masuk=input(f'Masukkan tanggal masuk {nama_hasil_panen} ke cold storage dalam format dd-mm-yyyy! ')

        except ValueError:
            if_value_error()
            continue

        break

    while True:
        try:
            suhu_penyimpanan=float(input(f'Masukkan suhu penyimpanan optimal {nama_hasil_panen} di cold storage (°C)! '))

        except ValueError:
            if_value_error()
            continue

        break

    while True:
        try:
            kelembaban=float(input(f'Masukkan kelembaban ruangan optimal {nama_hasil_panen} di cold storage (%)! '))

        except ValueError:
            if_value_error()
            continue

        break

    print('\n')

    entry=[nama_hasil_panen, kuantitas, tanggal_masuk, suhu_penyimpanan, kelembaban]
    data_baru.append(entry)
    hasil_panen.append(entry)
    tabel_data_panen()

def edit_data():
    tabel_data_panen()
    while True:
        try:
            id_edit=int(input('Masukkan ID data hasil panen yang ingin diedit! '))
            if 1 <= id_edit <= len(hasil_panen):
                table.append([id_edit, hasil_panen[id_edit-1][0], hasil_panen[id_edit-1][1], hasil_panen[id_edit-1][2], hasil_panen[id_edit-1][3], hasil_panen[id_edit-1][4]])
                print(tabulate(table,headers=['ID','Hasil Panen','Kuantitas (ton)','Tanggal Masuk','Suhu Penyimpanan (°C)','Kelembaban Ruangan (%)'],tablefmt='mixed_grid',numalign='center',stralign='center'))
                table.clear()
            else:
                print('ID yang diinput tidak tersedia!')
                continue

        except ValueError:
            if_value_error()
            continue

        break

    while True:
        kolom_edit=input('Masukkan nama kolom dari tabel data hasil panen yang ingin diedit! ').title()

        if kolom_edit == 'Hasil Panen':
            while True:
                try:
                    kolom = 0
                    data_baru=input('Masukkan nama hasil panen baru! ').title()
                    hasil_panen[id_edit-1][kolom] = data_baru
                    print(f'Data {kolom_edit} berhasil diubah!')

                except ValueError:
                    if_value_error()
                    continue

                break

        elif kolom_edit == 'Kuantitas':
            while True:
                try:
                    kolom = 1
                    data_baru=int(input('Masukkan kuantitas hasil panen baru dalam satuan ton! '))
                    hasil_panen[id_edit-1][kolom] = data_baru
                    print(f'Data {kolom_edit} berhasil diubah!')

                except ValueError:
                    if_value_error()
                    continue

                break

        elif kolom_edit == 'Tanggal Masuk':
            while True:
                try:
                    kolom = 2
                    data_baru=str(input('Masukkan tanggal masuk hasil panen baru ke cold storage dalam format dd-mm-yyyy! '))
                    hasil_panen[id_edit-1][kolom] = data_baru
                    print(f'Data {kolom_edit} berhasil diubah!')

                except ValueError:
                    if_value_error()
                    continue

                break

        elif kolom_edit == 'Suhu Penyimpanan':
            while True:
                try:
                    kolom = 3
                    data_baru=float(input('Masukkan suhu penyimpanan baru hasil panen dalam satuan °C! '))
                    hasil_panen[id_edit-1][kolom] = data_baru
                    print(f'Data {kolom_edit} berhasil diubah!')

                except ValueError:
                    if_value_error()
                    continue

                break
        
        elif kolom_edit == 'Kelembaban Ruangan':
            while True:
                try:
                    kolom = 4
                    data_baru=float(input('Masukkan kelembaban ruangan baru hasil panen dalam satuan %! '))
                    hasil_panen[id_edit-1][kolom] = data_baru
                    print(f'Data {kolom_edit} berhasil diubah!')

                except ValueError:
                    if_value_error()
                    continue

                break

        else:
            print('Harap masukkan nama kolom yang telah tersedia pada tabel!')
            continue
        
        break

    tabel_data_panen()

def hapus_data():
    while True:
        try:
            print('\n')
            for i in range(len(hasil_panen)):
                tabel_data_panen()
                hapusdata=int(input('Masukkan ID hasil panen yang ingin dihapus! '))
                if 1 <= hapusdata <= len(hasil_panen):
                    del hasil_panen[hapusdata-1]
                    print('\n')
                    print('Data hasil panen berhasil dihapus!')
                    tabel_data_panen()
                    break
                else:
                    print('\n')
                    print('ID hasil panen yang Anda masukkan tidak valid!')
                    continue
        
        except ValueError:
            if_value_error()
            continue

        break

table= []
data_baru= []
hasil_panen=[['Apel',2, '14-03-2025',1,90],
             ['Stroberi',5, '14-03-2025',2,90],
             ['Wortel',3,'14-03-2025',1,90],
             ['Kentang',2,'14-03-2025',8,90],
             ['Kubis',2,'14-03-2025',1,90]]

while True:
    print('\r\n')
    print(f'{'SELAMAT DATANG DI MENU UTAMA PUSAT DATA COLD STORAGE':^91}')
    print('='*96)

    menu_utama = input('''
                DATA PENYIMPANAN HASIL PANEN DI COLD STORAGE        
                List Menu :
                1. Menampilkan Data Hasil Panen
                2. Menambah Data Hasil Panen
                3. Mengedit Data Hasil Panen
                4. Menghapus Data Hasil Panen 
                5. Keluar Aplikasi
                Pilih nomor menu yang ingin dijalankan: ''')
    
    if menu_utama == '1':
       menampilkan()

    elif menu_utama == '2':
       menambah()

    elif menu_utama == '3':
       mengedit()

    elif menu_utama == '4':
       menghapus()

    elif menu_utama == '5':
        print('\n')
        print('KELUAR DARI PROGRAM PUSAT DATA COLD STORAGE...')
        print('\n')
        exit()

    else:
        print('\n')
        print('Harap masukkan menu angka yang telah ditampilkan dalam list menu!')
        continue