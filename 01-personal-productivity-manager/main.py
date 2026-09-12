daftar_tugas = []
id_berikutnya = 1

def masukkan_id():
    while True:
        id_tugas = input("\nMasukkan ID: ").strip()
        if id_tugas == "":
            print("\nError: ID tidak boleh kosong!")
            continue
        elif not id_tugas.isdigit():
            print("\nError: ID harus berupa angka, tidak boleh huruf atau simbol!")
            continue
        else:
            break
    return int(id_tugas)

def masukkan_judul():
    while True:
        judul_tugas = input("\nNama tugas: ").strip()
        if judul_tugas == "":
            print("\nError: Nama tugas tidak boleh kosong!")
        else:
            break
    return judul_tugas

def pilih_kategori():
    while True:
        print("\nKategori Tugas")
        print("1. Kuliah")
        print("2. Pribadi")
        print("3. Kerja")
        print("4. Belajar")
        pilihan_kategori = input("\nPilih kategori: ").strip()
        if pilihan_kategori != "":
            if pilihan_kategori.isdigit():
                if int(pilihan_kategori) == 1:
                    kategori_tugas = "Kuliah"
                    break
                elif int(pilihan_kategori) == 2:
                    kategori_tugas = "Pribadi"
                    break
                elif int(pilihan_kategori) == 3:
                    kategori_tugas = "Kerja"
                    break
                elif int(pilihan_kategori) == 4:
                    kategori_tugas = "Belajar"
                    break
                else:
                    print("\nError: Pilihan kategori tidak tersedia! Pilih hanya angka 1, 2, 3 atau 4.")
                    continue
            else:
                print("\nError: Pilihan kategori harus berupa angka, tidak boleh huruf atau simbol!")
                continue
        else:
            print("\nError: Pilihan kategori tidak boleh kosong!")
            continue
    return kategori_tugas

def pilih_prioritas():
    while True:
        print("\nPrioritas Tugas")
        print("1. Rendah")
        print("2. Sedang")
        print("3. Tinggi")
        pilihan_prioritas = input("\nPilih prioritas: ").strip()
        if pilihan_prioritas != "":
            if pilihan_prioritas.isdigit():
                if int(pilihan_prioritas) == 1:
                    prioritas_tugas = "Rendah"
                    break
                elif int(pilihan_prioritas) == 2:
                    prioritas_tugas = "Sedang"
                    break
                elif int(pilihan_prioritas) == 3:
                    prioritas_tugas = "Tinggi"
                    break
                else:
                    print("\nError: Pilihan prioritas tidak tersedia! Pilih hanya angka 1, 2, atau 3.")
                    continue
            else:
                print("\nError: Pilihan prioritas harus berupa angka, tidak boleh huruf atau simbol!")
            continue
        else:
            print("\nError: Pilihan prioritas tidak boleh kosong!")
            continue
    return prioritas_tugas

def tambah_tugas():
    global id_berikutnya
    judul_tugas = masukkan_judul()
    kategori_tugas = pilih_kategori()
    prioritas_tugas = pilih_prioritas()
    tugas_baru = {
        "id": id_berikutnya,
        "judul_tugas": judul_tugas,
        "kategori_tugas": kategori_tugas,
        "prioritas_tugas": prioritas_tugas,
        "status_tugas": "Belum selesai"
    }
    id_berikutnya += 1
    daftar_tugas.append(tugas_baru)

def tampilkan_tugas():
    if daftar_tugas:
        for tugas in daftar_tugas:
            print("")
            print(f'ID-{tugas["id"]}')
            print(f'Judul: {tugas["judul_tugas"]}')
            print(f'Kategori: {tugas["kategori_tugas"]}')
            print(f'Prioritas: {tugas["prioritas_tugas"]}')
            print(f'Status: {tugas["status_tugas"]}')
    else:
        print("\nTugas belum ada!")

def hapus_tugas():
    while True:
        target_id = masukkan_id()
        tugas_ditemukan = False
        for tugas in daftar_tugas:
            if target_id == tugas["id"]:
                daftar_tugas.remove(tugas)
                tugas_ditemukan = True
                print("\nTugas berhasil dihapus!")
                break
        if not tugas_ditemukan:
            print("\nTugas dengan ID tersebut tidak ditemukan!")
            continue
        break

def cari_tugas():
    while True:
        kata_kunci = input("\nMasukkan kata kunci: ").strip()
        if kata_kunci != "":
            tugas_ditemukan = False
            for tugas in daftar_tugas:
                if kata_kunci in tugas["judul_tugas"]:
                    print("")
                    print(f'ID-{tugas["id"]}')
                    print(f'Judul: {tugas["judul_tugas"]}')
                    print(f'Kategori: {tugas["kategori_tugas"]}')
                    print(f'Prioritas: {tugas["prioritas_tugas"]}')
                    print(f'Status: {tugas["status_tugas"]}')
                    tugas_ditemukan = True
            if not tugas_ditemukan:
                print("\nKata kunci tidak ditemukan!")
                continue
            break
        else:
            print("\nError: Kata kunci tidak boleh kosong!")
            continue

def filter_tugas():
    while True:
        print("\nFilter Tugas")
        print("1. Berdasarkan Kategori")
        print("2. Berdasarkan Prioritas")
        print("3. Berdasarkan Status")
        pilihan_filter = input("\nPilih filter: ")
        if pilihan_filter != "":
            if pilihan_filter.isdigit():
                if int(pilihan_filter) == 1:
                    kategori_tugas = pilih_kategori()
                    tugas_ditemukan = False
                    for tugas in daftar_tugas:
                        if kategori_tugas == tugas["kategori_tugas"]:
                            print("")
                            print(f'ID-{tugas["id"]}')
                            print(f'Judul: {tugas["judul_tugas"]}')
                            print(f'Kategori: {tugas["kategori_tugas"]}')
                            print(f'Prioritas: {tugas["prioritas_tugas"]}')
                            print(f'Status: {tugas["status_tugas"]}')
                            tugas_ditemukan = True
                    if not tugas_ditemukan:
                        print("\nKategori tidak ditemukan!")
                        continue
                    break
                elif int(pilihan_filter) == 2:
                    prioritas_tugas = pilih_prioritas()
                    tugas_ditemukan = False
                    for tugas in daftar_tugas:
                        if prioritas_tugas == tugas["prioritas_tugas"]:
                            print("")
                            print(f'ID-{tugas["id"]}')
                            print(f'Judul: {tugas["judul_tugas"]}')
                            print(f'Kategori: {tugas["kategori_tugas"]}')
                            print(f'Prioritas: {tugas["prioritas_tugas"]}')
                            print(f'Status: {tugas["status_tugas"]}')
                            tugas_ditemukan = True
                    if not tugas_ditemukan:
                        print("\nPrioritas tidak ditemukan!")
                        continue
                    break
                elif int(pilihan_filter) == 3:
                    print("\n1. Belum selesai")
                    print("2. Selesai")
                    pilihan_status = input("\nPilih status: ").strip()
                    if pilihan_status != "":
                        if pilihan_status.isdigit():
                            if int(pilihan_status) == 1:
                                tugas_ditemukan = False
                                for tugas in daftar_tugas:
                                    if "Belum selesai" == tugas["status_tugas"]:
                                        print("")
                                        print(f'ID-{tugas["id"]}')
                                        print(f'Judul: {tugas["judul_tugas"]}')
                                        print(f'Kategori: {tugas["kategori_tugas"]}')
                                        print(f'Prioritas: {tugas["prioritas_tugas"]}')
                                        print(f'Status: {tugas["status_tugas"]}')
                                        tugas_ditemukan = True
                                if not tugas_ditemukan:
                                    print("\nStatus tidak ditemukan!")
                                    continue
                                break
                            elif int(pilihan_status) == 2:
                                tugas_ditemukan = False
                                for tugas in daftar_tugas:
                                    if "Selesai" == tugas["status_tugas"]:
                                        print("")
                                        print(f'ID-{tugas["id"]}')
                                        print(f'Judul: {tugas["judul_tugas"]}')
                                        print(f'Kategori: {tugas["kategori_tugas"]}')
                                        print(f'Prioritas: {tugas["prioritas_tugas"]}')
                                        print(f'Status: {tugas["status_tugas"]}')
                                        tugas_ditemukan = True
                                if not tugas_ditemukan:
                                    print("\nStatus tidak ditemukan!")
                                    continue
                                break
                            else:
                                print("\nError: Pilihan status tidak tersedia! Pilih hanya angka 1 dan 2.")
                                continue
                        else:
                            print("\nError: Pilihan status harus berupa angka, tidak boleh huruf atau simbol!")
                            continue
                    else:
                        print("\nError: Pilihan status tidak boleh kosong!")
                        continue
                else:
                    print("\nError: Pilihan filter tidak tersedia! Pilih hanya angka 1, 2, atau 3.")
                    continue
            else:
                print("\nError: Pilihan filter harus berupa angka, tidak boleh huruf atau simbol!")
                continue
        else:
            print("\nError: Pilihan filter tidak boleh kosong!")
            continue

def sort_tugas():
    while True:
        print("\nSort Tugas")
        print("1. Berdasarkan Judul")
        print("2. Berdasarkan Prioritas")
        print("3. Berdasarkan Kategori")
        pilihan_sort = input("\nPilih sort: ")
        if pilihan_sort != "":
            if pilihan_sort.isdigit():
                if int(pilihan_sort) == 1:
                    print("\nJenis Sort")
                    print("1. A -> Z")
                    print("2. Z -> A")
                    pilihan_jenis_sort = input("\nPilih jenis sort: ")
                    if pilihan_jenis_sort != "":
                        if pilihan_jenis_sort.isdigit():
                            if int(pilihan_jenis_sort) == 1:
                                tugas_urut_judul_a_ke_z = sorted(daftar_tugas, key=lambda x: x["judul_tugas"])
                                for tugas in tugas_urut_judul_a_ke_z:
                                    print(f'\nID-{tugas["id"]}')
                                    print(f'Judul: {tugas["judul_tugas"]}')
                                    print(f'Kategori: {tugas["kategori_tugas"]}')
                                    print(f'Prioritas: {tugas["prioritas_tugas"]}')
                                    print(f'Status: {tugas["status_tugas"]}')
                                break
                            elif int(pilihan_jenis_sort) == 2:
                                tugas_urut_judul_z_ke_a = sorted(daftar_tugas, key=lambda x: x["judul_tugas"], reverse=True)
                                for tugas in tugas_urut_judul_z_ke_a:
                                    print(f'\nID-{tugas["id"]}')
                                    print(f'Judul: {tugas["judul_tugas"]}')
                                    print(f'Kategori: {tugas["kategori_tugas"]}')
                                    print(f'Prioritas: {tugas["prioritas_tugas"]}')
                                    print(f'Status: {tugas["status_tugas"]}')
                                break
                            else:
                                print("\nError: Pilihan sort tidak tersedia! Pilih hanya angka 1 dan 2.")
                                continue
                        else:
                            print("\nError: Pilihan sort harus berupa angka, tidak boleh huruf atau simbol!")
                            continue
                    else:
                        print("\nError: Pilihan sort tidak boleh kosong!")
                        continue

                elif int(pilihan_sort) == 2:
                    print("\nJenis Sort")
                    print("1. Tinggi -> Rendah")
                    print("2. Rendah -> Tinggi")
                    bobot_prioritas = {"Tinggi": 1, "Sedang": 2, "Rendah": 3}
                    pilihan_jenis_sort = input("\nPilih jenis sort: ")
                    if pilihan_jenis_sort != "":
                        if pilihan_jenis_sort.isdigit():
                            if int(pilihan_jenis_sort) == 1:
                                tugas_urut_prioritas_tinggi_ke_rendah = sorted(daftar_tugas, key=lambda x: bobot_prioritas[x["prioritas_tugas"]])
                                for tugas in tugas_urut_prioritas_tinggi_ke_rendah:
                                    print(f'\nID-{tugas["id"]}')
                                    print(f'Judul: {tugas["judul_tugas"]}')
                                    print(f'Kategori: {tugas["kategori_tugas"]}')
                                    print(f'Prioritas: {tugas["prioritas_tugas"]}')
                                    print(f'Status: {tugas["status_tugas"]}')
                                break
                            elif int(pilihan_jenis_sort) == 2:
                                tugas_urut_prioritas_rendah_ke_tinggi = sorted(daftar_tugas, key=lambda x: bobot_prioritas[x["prioritas_tugas"]], reverse=True)
                                for tugas in tugas_urut_prioritas_rendah_ke_tinggi:
                                    print(f'\nID-{tugas["id"]}')
                                    print(f'Judul: {tugas["judul_tugas"]}')
                                    print(f'Kategori: {tugas["kategori_tugas"]}')
                                    print(f'Prioritas: {tugas["prioritas_tugas"]}')
                                    print(f'Status: {tugas["status_tugas"]}')
                                break
                            else:
                                print("\nError: Pilihan sort tidak tersedia! Pilih hanya angka 1 dan 2.")
                                continue
                        else:
                            print("\nError: Pilihan sort harus berupa angka, tidak boleh huruf atau simbol!")
                            continue
                    else:
                        print("\nError: Pilihan sort tidak boleh kosong!")
                        continue

                elif int(pilihan_sort) == 3:
                    print("\nJenis Sort")
                    print("1. A -> Z")
                    print("2. Z -> A")
                    pilihan_jenis_sort = input("\nPilih jenis sort: ")
                    if pilihan_jenis_sort != "":
                        if pilihan_jenis_sort.isdigit():
                            if int(pilihan_jenis_sort) == 1:
                                tugas_urut_kategori_a_ke_z = sorted(daftar_tugas, key=lambda x: x["kategori_tugas"])
                                for tugas in tugas_urut_kategori_a_ke_z:
                                    print(f'\nID-{tugas["id"]}')
                                    print(f'Judul: {tugas["judul_tugas"]}')
                                    print(f'Kategori: {tugas["kategori_tugas"]}')
                                    print(f'Prioritas: {tugas["prioritas_tugas"]}')
                                    print(f'Status: {tugas["status_tugas"]}')
                                break
                            elif int(pilihan_jenis_sort) == 2:
                                tugas_urut_kategori_z_ke_a = sorted(daftar_tugas, key=lambda x: x["kategori_tugas"], reverse=True)
                                for tugas in tugas_urut_kategori_z_ke_a:
                                    print(f'\nID-{tugas["id"]}')
                                    print(f'Judul: {tugas["judul_tugas"]}')
                                    print(f'Kategori: {tugas["kategori_tugas"]}')
                                    print(f'Prioritas: {tugas["prioritas_tugas"]}')
                                    print(f'Status: {tugas["status_tugas"]}')
                                break
                            else:
                                print("\nError: Pilihan sort tidak tersedia! Pilih hanya angka 1 dan 2.")
                                continue
                        else:
                            print("\nError: Pilihan sort harus berupa angka, tidak boleh huruf atau simbol!")
                            continue
                    else:
                        print("\nError: Pilihan sort tidak boleh kosong!")
                        continue
            else:
                print("\nError: Pilihan sort harus berupa angka, tidak boleh huruf atau simbol!")
                continue
        else:
            print("\nError: Pilihan Sort tidak boleh kosong!")
            continue

def tandai_selesai():
    while True:
        target_id = masukkan_id()
        tugas_ditemukan = False
        for tugas in daftar_tugas:
            if target_id == tugas["id"]:
                tugas["status_tugas"] = "Selesai"
                print("\nTugas berhasil ditandai selesai!")
                tugas_ditemukan = True
                break
        if not tugas_ditemukan:
            print("\nTugas dengan ID tersebut tidak ditemukan!")
            continue
        break

def edit_tugas():
    while True:
        target_id = masukkan_id()
        tugas_ditemukan = False
        for tugas in daftar_tugas:
            if target_id == tugas["id"]:
                while True:
                    print("\nData Tugas yang Dapat Diedit")
                    print("1. Judul")
                    print("2. Kategori")
                    print("3. Prioritas")
                    pilihan_edit = input("\nPilih data yang ingin diedit: ").strip()
                    if not pilihan_edit.isdigit():
                        print("\nError: Pilihan harus berupa angka, tidak boleh huruf atau simbol!")
                        continue
                    elif int(pilihan_edit) not in (1,2,3):
                        print("\nError: Pilihan tidak tersedia!")
                        continue
                    else:
                        break
                if int(pilihan_edit) == 1:
                    judul_baru = masukkan_judul()
                    tugas["judul_tugas"] = judul_baru
                    print("\nTugas berhasil diedit!")
                elif int(pilihan_edit) == 2:
                    kategori_baru = pilih_kategori()
                    tugas["kategori_tugas"] = kategori_baru
                    print("\nTugas berhasil diedit!")
                elif int(pilihan_edit) == 3:
                    prioritas_baru = pilih_prioritas()
                    tugas["prioritas_tugas"] = prioritas_baru
                    print("\nTugas berhasil diedit!")
                else:
                    print("\nError: Pilihan tidak tersedia!")
                    continue
                tugas_ditemukan = True
                break
        if not tugas_ditemukan:
            print("\nTugas dengan ID tersebut tidak ditemukan!")
            continue
        break

while True:
    print("\n===== PERSONAL PRODUCTIVITY MANAGER =====")
    print('''
    1. Tambah tugas
    2. Tampilkan tugas
    3. Hapus tugas
    4. Cari tugas
    5. Filter tugas
    6. Sort tugas
    7. Tandai tugas selesai
    8. Edit tugas
    9. Keluar
    ''')
    pilihan_menu = input("Pilih menu: ").strip()
    if pilihan_menu.isdigit():
        if int(pilihan_menu) == 1:
            tambah_tugas()
        elif int(pilihan_menu) == 2:
            tampilkan_tugas()
        elif int(pilihan_menu) == 3:
            hapus_tugas()
        elif int(pilihan_menu) == 4:
            cari_tugas()
        elif int(pilihan_menu) == 5:
            filter_tugas()
        elif int(pilihan_menu) == 6:
            sort_tugas()
        elif int(pilihan_menu) == 7:
            tandai_selesai()
        elif int(pilihan_menu) == 8:
            edit_tugas()
        elif int(pilihan_menu) == 9:
            break
        else:
            print("\nError: Pilihan menu tidak tersedia!")
            continue
    else:
        print("\nError: Pilihan menu harus berupa angka, tidak boleh huruf atau simbol!")
        continue