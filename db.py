import sqlite3

def connect_db():
    return sqlite3.connect('tasks.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            status INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_task(description):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (description) VALUES (?)', (description,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def get_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def complete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status = 1 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def show_tasks():
    tasks = get_tasks()
    if tasks:
        print("Görev Listesi:")
        for task in tasks:
            status = "Tamamlandı" if task[2] == 1 else "Tamamlanmadı"
            print(f"{task[0]}. {task[1]} - Durum: {status}")
    else:
        print("Görev yok.")
