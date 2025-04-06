from tabulate import tabulate

def menampilkan():
    while True:
        menu_tampil=int(input('''
                    SUB-MENU :
                    1. Menampilkan semua data hasil panen
                    2. Menampilkan data hasil panen tertentu
                    3. Kembali ke menu utama
                    Silahkan pilih nomor sub-menu yang ingin dijalankan: '''))
        
        if menu_tampil == 1:
            tabel_data_panen()
             
        elif menu_tampil == 2:
            while True:
                print('\n')
                id_tampil=int(input('Masukkan ID hasil panen yang ingin dilihat datanya! '))

                if 1 <= id_tampil <= len(hasil_panen):
                    table.append([id_tampil, hasil_panen[id_tampil-1][0], hasil_panen[id_tampil-1][1], hasil_panen[id_tampil-1][2], hasil_panen[id_tampil-1][3], hasil_panen[id_tampil-1][4]])
                    print(tabulate(table,headers=['ID','Hasil Panen','Kuantitas (ton)','Tanggal Masuk','Suhu Penyimpanan (°C)','Kelembaban Ruangan (%)'],tablefmt='mixed_grid',numalign='center',stralign='center'))
                    table.clear()
                else:
                    print('Harap masukkan ID hasil panen yang tersedia dalam tabel hasil panen!')
                    continue

                checker_id_tampil=input('Apakah ingin melihat data hasil panen lain?(Ya/Tidak) ').capitalize()
                if checker_id_tampil == 'Ya':
                    continue
                elif checker_id_tampil == 'Tidak':
                    break
                else:
                    print('Input tidak valid! mohon masukkan input "Ya" atau "Tidak"!')
                    continue
            
        elif menu_tampil == 3:
            break

        else:
            print('\n')
            print('Nomor sub-menu yang dimasukkan tidak valid! Silahkan pilih nomor yang telah ditampilkan!')
            continue

def menambah():
    while True:
        menu_tambah=int(input('''
                        SUB-MENU :
                        1. Menambah data hasil panen baru
                        2. Kembali ke menu utama
                        Silahkan pilih nomor sub-menu yang ingin dijalankan: '''))
        
        if menu_tambah == 1:
            input_tambah()

            while True:
                checker_tambah=input('Apakah ingin menambah data hasil panen lain?(Ya/Tidak) ').capitalize()

                if checker_tambah == 'Ya':
                    input_tambah()
                elif checker_tambah == 'Tidak':
                    break
                else:
                    print('input tidak valid! mohon masukkan input "Ya" atau "Tidak"!')
                    continue

        elif menu_tambah == 2:
            break

        else:
            print('\n')
            print('Nomor sub-menu yang dimasukkan tidak valid! Silahkan pilih nomor yang telah ditampilkan!')
            continue

def mengedit():
    while True:
        menu_edit=int(input('''
                        SUB-MENU :
                        1. Mengedit data hasil panen tertentu
                        2. Kembali ke menu utama
                        Silahkan pilih nomor sub-menu yang ingin dijalankan: '''))
        
        if menu_edit == 1:
            edit_data()

            while True:
                checker_edit=input('Apakah ingin mengedit data hasil panen lain?(Ya/Tidak) ').capitalize()

                if checker_edit == 'Ya':
                    edit_data()

                elif checker_edit == 'Tidak':
                    tabel_data_panen()
                    break

                else:
                    print('input tidak valid! mohon masukkan input "Ya" atau "Tidak"!')
                    continue

        elif menu_edit == 2:
            break

        else:
            print('\n')
            print('Nomor sub-menu yang dimasukkan tidak valid! Silahkan pilih nomor yang telah ditampilkan!')
            continue

def menghapus():
    while True:
        menu_hapus=int(input('''
                        SUB-MENU :
                        1. Menghapus data hasil panen tertentu
                        2. Kembali ke menu utama
                        Silahkan pilih nomor sub-menu yang ingin dijalankan: '''))
        
        if menu_hapus == 1:
            hapus_data()

            while True:
                checker_hapus=input('Apakah ingin menghapus data hasil panen lain?(Ya/Tidak) ').capitalize()

                if checker_hapus == 'Ya':
                    hapus_data()
                elif checker_hapus == 'Tidak':
                    tabel_data_panen()
                    break
                else:
                    print('input tidak valid! mohon masukkan input "Ya" atau "Tidak"!')
                    continue

        elif menu_hapus == 2:
            break

        else:
            print('\n')
            print('Nomor sub-menu yang dimasukkan tidak valid! Silahkan pilih nomor yang telah ditampilkan!')
            continue

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
    for i in range(len(hasil_panen)):
        print('\n')
        tabel_data_panen()
        nama_hasil_panen=input('Masukkan nama hasil panen baru! ').capitalize()
        if any(nama_hasil_panen == i[0] for i in hasil_panen):
            print(f'Data komoditas {nama_hasil_panen} sudah terdapat dalam pusat data. Mohon input nama hasil panen lain!')
            continue
        elif any(nama_hasil_panen != i[0] for i in hasil_panen):
            break

    kuantitas=int(input(f'Masukkan kuantitas {nama_hasil_panen} dalam satuan ton! '))
    tanggal_masuk=input(f'Masukkan tanggal masuk {nama_hasil_panen} ke cold storage dalam format dd-mm-yyyy! ')
    suhu_penyimpanan=int(input(f'Masukkan suhu penyimpanan optimal {nama_hasil_panen} di cold storage (°C)! '))
    kelembaban=int(input(f'Masukkan kelembaban ruangan optimal {nama_hasil_panen} di cold storage (%)! '))

    print('\n')

    hasil_panen.append([nama_hasil_panen,kuantitas,tanggal_masuk,suhu_penyimpanan,kelembaban])
    tabel_data_panen()

def edit_data():
    tabel_data_panen()
    while True:
        id_edit=int(input('Masukkan ID data hasil panen yang ingin diedit! '))
        if 1 <= id_edit <= len(hasil_panen):
            table.append([id_edit, hasil_panen[id_edit-1][0], hasil_panen[id_edit-1][1], hasil_panen[id_edit-1][2], hasil_panen[id_edit-1][3], hasil_panen[id_edit-1][4]])
            print(tabulate(table,headers=['ID','Hasil Panen','Kuantitas (ton)','Tanggal Masuk','Suhu Penyimpanan (°C)','Kelembaban Ruangan (%)'],tablefmt='mixed_grid',numalign='center',stralign='center'))
            table.clear()
        else:
            print('ID yang diinput tidak tersedia!')
            continue

        kolom_edit=input('Masukkan nama kolom dari tabel data hasil panen yang ingin diedit! ').title()

        if kolom_edit == 'Hasil Panen':
            kolom = 0
            data_baru=str(input('Masukkan nama hasil panen baru! ')).title()
            hasil_panen[id_edit-1][kolom] = data_baru
            print(f'Data {kolom_edit} berhasil diubah!')

        elif kolom_edit == 'Kuantitas':
            kolom = 1
            data_baru=int(input('Masukkan kuantitas hasil panen baru dalam satuan ton! '))
            hasil_panen[id_edit-1][kolom] = data_baru
            print(f'Data {kolom_edit} berhasil diubah!')

        elif kolom_edit == 'Tanggal Masuk':
            kolom = 2
            data_baru=str(input('Masukkan tanggal masuk hasil panen baru ke cold storage dalam format dd-mm-yyyy! '))
            hasil_panen[id_edit-1][kolom] = data_baru
            print(f'Data {kolom_edit} berhasil diubah!')

        elif kolom_edit == 'Suhu Penyimpanan':
            kolom = 3
            data_baru=int(input('Masukkan suhu penyimpanan baru hasil panen dalam satuan °C! '))
            hasil_panen[id_edit-1][kolom] = data_baru
            print(f'Data {kolom_edit} berhasil diubah!')
        
        elif kolom_edit == 'Kelembaban Ruangan':
            kolom = 4
            data_baru=int(input('Masukkan kelembaban ruangan baru hasil panen dalam satuan %! '))
            hasil_panen[id_edit-1][kolom] = data_baru
            print(f'Data {kolom_edit} berhasil diubah!')

        tabel_data_panen()
        break

def hapus_data():
    print('\n')
    for i in range(len(hasil_panen)):
        tabel_data_panen()
        hapusdata=int(input('Masukkan ID hasil panen yang ingin dihapus! '))
        if 1 <= hapusdata <= len(hasil_panen):
            del hasil_panen[hapusdata-1]
            print('Data hasil panen berhasil dihapus!')
            tabel_data_panen()
            break
        else:
            print('ID hasil panen yang Anda masukkan tidak valid!')
            continue

table= []
hasil_panen=[['Apel',2, '14-03-2025',1,90],
             ['Stroberi',5, '14-03-2025',2,90],
             ['Wortel',3,'14-03-2025',1,90],
             ['Kentang',2,'14-03-2025',8,90],
             ['Kubis',2,'14-03-2025',1,90]]

while True:
    print('\r\n')
    print(f'{'SELAMAT DATANG DI MENU UTAMA PUSAT DATA COLD STORAGE':^91}')
    print('='*96)

    menu_utama = int(input('''
                DATA PENYIMPANAN HASIL PANEN DI COLD STORAGE        
                List Menu :
                1. Menampilkan Data Hasil Panen
                2. Menambah Data Hasil Panen
                3. Mengedit Data Hasil Panen
                4. Menghapus Data Hasil Panen 
                5. Keluar Aplikasi
                Pilih nomor menu yang ingin dijalankan: '''))
    
    if menu_utama == 1:
       menampilkan()

    elif menu_utama == 2:
       menambah()

    elif menu_utama == 3:
       mengedit()

    elif menu_utama == 4:
       menghapus()

    elif menu_utama == 5:
        exit()

    else:
        print('\n')
        print('Harap masukkan menu angka yang telah ditampilkan dalam list menu!')
        continue