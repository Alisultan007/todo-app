import json
import os
from models import TaskManager

def save_tasks_in_json(tasks):
    if isinstance(tasks, list):
        try:
            with open('tasks.json', 'w', encoding='utf-8') as outfile:
                json.dump(tasks, outfile, ensure_ascii=False, indent=4)
            print("Задачи успешно сохранены в файл tasks.json.")
        except Exception as e:
            print(f"Ошибка при сохранении задач в файл: {e}")
    else:
        print("Ошибка: задачи должны быть в формате списка.")

def import_tasks_from_json():
    if os.path.exists('tasks.json'):
        try:
            with open('tasks.json', 'r', encoding='utf-8') as json_file:
                return json.load(json_file)
        except Exception as e:
            print(f"Ошибка при загрузке задач из файла: {e}")
            return []
    return []

if __name__ == '__main__':
    created_tasks = import_tasks_from_json()
    task_manager = TaskManager()
    task_manager.set_tasks(created_tasks)

    task_manager.add_task("Сделать ДЗ по школе", "Сделать дз по алгебре и русскому")

    save_tasks_in_json(task_manager.get_tasks())
