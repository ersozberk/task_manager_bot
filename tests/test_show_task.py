import unittest
from db import add_task, get_tasks, create_table, connect_db

class TestShowTasks(unittest.TestCase):
    def setUp(self):
        create_table()

    def tearDown(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks")
        conn.commit()
        conn.close()

    def test_show_tasks(self):
        add_task("Görev 1")
        add_task("Görev 2")
        
        tasks = get_tasks()
        
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0][1], "Görev 1")
        self.assertEqual(tasks[1][1], "Görev 2")

if __name__ == '__main__':
    unittest.main()
