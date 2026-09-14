from exceptions import TaskTidakDitemukanError

class TaskManager():
    def __init__(self):
        self.__tasks = []

    def tambah_task(self, task):
        self.__tasks.append(task)

    def tampilkan_task(self):
        for task in self.__tasks:
            task.tampilkan_info()

    def cari_id_task(self, id_task):
        ditemukan = False

        for task in self.__tasks:
            if id_task == task.id_task:
                task.tampilkan_info()
                ditemukan = True
                break
        if not ditemukan:
            raise TaskTidakDitemukanError("ID Task tidak ditemukan!")

    def hapus_id_task(self, id_task):
        ditemukan = False

        for task in self.__tasks:
            if id_task == task.id_task:
                self.__tasks.remove(task)
                ditemukan = True
                break
        if not ditemukan:
            raise TaskTidakDitemukanError("ID Task tidak ditemukan!")

    def edit_judul_task(self, id_task, judul_baru):
        ditemukan = False

        for task in self.__tasks:
            if id_task == task.id_task:
                task.ubah_judul(judul_baru)
                ditemukan = True
                break
        if not ditemukan:
            raise TaskTidakDitemukanError("ID Task tidak ditemukan!")

    def edit_kategori_task(self, id_task, kategori_baru):
        ditemukan = False

        for task in self.__tasks:
            if id_task == task.id_task:
                task.ubah_kategori(kategori_baru)
                ditemukan = True
                break
        if not ditemukan:
            raise TaskTidakDitemukanError("ID Task tidak ditemukan!")

    def edit_prioritas_task(self, id_task, prioritas_baru):
        ditemukan = False

        for task in self.__tasks:
            if id_task == task.id_task:
                task.ubah_prioritas(prioritas_baru)
                ditemukan = True
                break
        if not ditemukan:
            raise TaskTidakDitemukanError("ID Task tidak ditemukan!")

    def tandai_selesai_task(self, id_task):
        ditemukan = False

        for task in self.__tasks:
            if id_task == task.id_task:
                task.tandai_selesai()
                ditemukan = True
                break
        if not ditemukan:
            raise TaskTidakDitemukanError("ID Task tidak ditemukan!")
