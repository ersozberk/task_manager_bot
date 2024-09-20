import discord
from db import add_task, delete_task, get_tasks, complete_task

async def add_task_command(message, description):
    add_task(description)
    await message.channel.send(f"Görev eklendi: {description}")

async def delete_task_command(message, task_id):
    delete_task(task_id)
    await message.channel.send(f"Görev silindi: {task_id}")

async def show_tasks_command(message):
    tasks = get_tasks()
    if tasks:
        response = "\n".join([f"{task[0]} - {task[1]} - {'Tamamlandı' if task[2] else 'Devam ediyor'}" for task in tasks])
    else:
        response = "Görev yok."
    await message.channel.send(response)

async def complete_task_command(message, task_id):
    complete_task(task_id)
    await message.channel.send(f"Görev tamamlandı: {task_id}")
