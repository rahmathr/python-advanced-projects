from manager import TaskManager
from models import Task, TaskKuliah, TaskKerja
from exceptions import TaskTidakDitemukanError

manajer_tugas = TaskManager()
try:
    tugas_1 = Task("1", "Belajar Python", "Belajar", "Tinggi", "Belum selesai")
    manajer_tugas.tambah_task(tugas_1)
    tugas_2 = TaskKuliah("2", "Mengerjakan Tugas Basis Data", "Kuliah", "Sedang", "Belum selesai", "Basis Data")
    manajer_tugas.tambah_task(tugas_2)
    tugas_3 = TaskKerja("3", "Rapat Mingguan Sprint", "Kerja", "Tinggi", "Belum selesai", "Sprint Planning")
    manajer_tugas.tambah_task(tugas_3)
    tugas_4 = Task("4", "Beli Kebutuhan Rumah", "Pribadi", "Rendah", "Belum selesai")
    manajer_tugas.tambah_task(tugas_4)
except ValueError as error:
    print(error)

manajer_tugas.tampilkan_task()

try:
    manajer_tugas.cari_id_task(99)
except TaskTidakDitemukanError as error:
    print(error)