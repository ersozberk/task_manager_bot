import unittest
from db import add_task, get_tasks, create_table, connect_db

class TestAddTask(unittest.TestCase):
    def setUp(self):
        # Her testten önce tabloyu oluştur
        create_table()

    def tearDown(self):
        # Test sonrası veritabanını temizle
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks")
        conn.commit()
        conn.close()

    def test_add_task(self):
        # Bir görev ekleyelim
        add_task("Yeni görev")
        
        # Veritabanındaki görevleri al
        tasks = get_tasks()

        # Eklenen görevin var olup olmadığını kontrol et
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][1], "Yeni görev")  # Görev açıklaması kontrolü

if __name__ == '__main__':
    unittest.main()
