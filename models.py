class TaskManager:
    def __init__(self):
        self.__tasks = []

    def add_task(self, title, description):  # Добавить задачу
        self.__tasks.append({"title": title, "description": description, "done": False})

    def remove_task(self, title=None, done=None):  # Удалить задачу по названию или статусу
        if title:
            self.__tasks = [task for task in self.__tasks if task['title'] != title]
        elif done is not None:
            self.__tasks = [task for task in self.__tasks if task['done'] != done]

    def mark_as_done(self, title):  # Сделать задачу выполненной
        for task in self.__tasks:
            if task['title'] == title:
                task['done'] = True
                break

    def edit_task(self, title, new_description):  # Редактировать описание задачи
        for task in self.__tasks:
            if task['title'] == title:
                task['description'] = new_description
                break

    def show_tasks(self):  # Показать все задачи
        if not self.__tasks:
            print("Задач для выполнения нет")
        else:
            for task in self.__tasks:
                status = "Выполнено" if task['done'] else "Не выполнено"
                print(f"Задача: {task['title']} \nОписание: {task['description']} \nСтатус: {status}\n")

    def __str__(self):  # Вывод количества задач
        done_count = sum(1 for task in self.__tasks if task['done'])
        not_done_count = len(self.__tasks) - done_count
        return f"Количество задач: {len(self.__tasks)}, Выполнено: {done_count}, Не выполнено: {not_done_count}"

if __name__ == '__main__':
    task_manager = TaskManager()
    task_manager.add_task("Сделать ДЗ по школе", "Сделать дз по алгебре и русскому")
    task_manager.add_task("Сделать ДЗ по айти школе", "Сделать проект и загрузить в майстат")

    task_manager.mark_as_done("Сделать ДЗ по школе")
    task_manager.show_tasks()

    task_manager.edit_task("Сделать ДЗ по айти школе", "Сделать проект и выложить его на GitHub")
    task_manager.remove_task(done=True)  # Удаляем все выполненные задачи
    task_manager.show_tasks()

    print(f"{task_manager}\nСПАСИБО ЗА ВНИМАНИЕ К МОЕМУ ТВОРЕНИЮ:)")
