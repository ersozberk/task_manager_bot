import unittest
from db import add_task, delete_task, get_tasks, create_table, connect_db

class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        create_table()
        add_task("Silinecek görev")

    def tearDown(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks")
        conn.commit()
        conn.close()

    def test_delete_task(self):
        tasks = get_tasks()
        task_id = tasks[0][0]  # İlk görevin ID'sini al
        delete_task(task_id)
        
        tasks_after_deletion = get_tasks()
        self.assertEqual(len(tasks_after_deletion), 0)  # Görev silindikten sonra sayının 0 olması gerekir

if __name__ == '__main__':
    unittest.main()
