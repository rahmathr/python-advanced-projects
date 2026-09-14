class Task:
    kategori = ["Kuliah", "Pribadi", "Kerja", "Belajar"]
    prioritas = ["Rendah", "Sedang", "Tinggi"]

    def __init__(self, id_task, judul, kategori, prioritas, status):
        if id_task != "":
            if str(id_task).isdigit():
                self.id_task = int(id_task)
            else:
                raise ValueError("ID harus berupa angka")
        else:
            raise ValueError("ID tidak boleh kosong!")

        if judul.strip() != "":
            self.__judul = judul
        else:
            raise ValueError("Nama tugas tidak boleh kosong!")

        if kategori != "":
            if kategori in Task.kategori:
                self.__kategori = kategori
            else:
                raise ValueError("Pilihan kategori tidak tersedia!")
        else:
            raise ValueError("Kategori tidak boleh kosong!")

        if prioritas != "":
            if prioritas in Task.prioritas:
                self.__prioritas = prioritas
            else:
                raise ValueError("Pilihan prioritas tidak tersedia!")
        else:
            raise ValueError("Prioritas tidak boleh kosong!")

        self.__status = status

    def tandai_selesai(self):
        self.__status = "Selesai"

    def ubah_judul(self, judul_baru):
        if judul_baru.strip() != "":
            self.__judul = judul_baru
        else:
            raise ValueError("Nama tugas tidak boleh kosong!")

    def ubah_kategori(self, kategori_baru):
        if kategori_baru.strip() != "":
            if kategori_baru in Task.kategori:
                self.__kategori = kategori_baru
            else:
                raise ValueError("Pilihan kategori tidak tersedia!")
        else:
            raise ValueError("Nama kategori tidak boleh kosong!")

    def ubah_prioritas(self, prioritas_baru):
        if prioritas_baru.strip() != "":
            if prioritas_baru in Task.prioritas:
                self.__prioritas = prioritas_baru
            else:
                raise ValueError("Pilihan prioritas tidak tersedia!")
        else:
            raise ValueError("Nama prioritas tidak boleh kosong!")

    def ambil_id(self):
        return self.id_task

    def ambil_judul(self):
        return self.__judul

    def ambil_status(self):
        return self.__status

    def ambil_kategori(self):
        return self.__kategori

    def ambil_prioritas(self):
        return self.__prioritas

    def tampilkan_info(self):
        print(f"\nID-{self.id_task}")
        print(f"Judul: {self.__judul}")
        print(f"Kategori: {self.__kategori}")
        print(f"Prioritas: {self.__prioritas}")
        print(f"Status: {self.__status}")

class TaskKuliah(Task):
    def __init__(self, id_task, judul, kategori, prioritas, status, mata_kuliah):
        super().__init__(id_task, judul, kategori, prioritas, status)

        if mata_kuliah.strip() != "":
            self.__mata_kuliah = mata_kuliah
        else:
            raise ValueError("Nama mata kuliah tidak boleh kosong!")

    def ambil_mata_kuliah(self):
        return self.__mata_kuliah

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Mata Kuliah: {self.__mata_kuliah}")

class TaskKerja(Task):
    def __init__(self, id_task, judul, kategori, prioritas, status, nama_meeting):
        super().__init__(id_task, judul, kategori, prioritas, status)

        if nama_meeting.strip() != "":
            self.__nama_meeting = nama_meeting
        else:
            raise ValueError("Nama meeting tidak boleh kosong!")

    def ambil_nama_meeting(self):
        return self.__nama_meeting

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Nama Meeting: {self.__nama_meeting}")
