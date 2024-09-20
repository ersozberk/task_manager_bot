import unittest
from db import add_task, complete_task, get_tasks, create_table, connect_db

class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        create_table()
        add_task("Tamamlanacak görev")

    def tearDown(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks")
        conn.commit()
        conn.close()

    def test_complete_task(self):
        tasks = get_tasks()
        task_id = tasks[0][0]  # İlk görevin ID'sini al
        
        complete_task(task_id)
        
        tasks = get_tasks()
        self.assertEqual(tasks[0][2], 1)  # Görevin 'status' alanı 1 olmalı (tamamlandı)

if __name__ == '__main__':
    unittest.main()
