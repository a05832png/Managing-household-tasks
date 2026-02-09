import datetime

class HomeManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, priority="Normal"):
        task = {
            "id": len(self.tasks) + 1,
            "name": task_name,
            "priority": priority,
            "date": datetime.date.today().strftime("%d/%m/%Y")
        }
        self.tasks.append(task)
        return f"משימה חדשה נוספה: {task_name}"

    def show_tasks(self):
        if not self.tasks:
            return "אין משימות פתוחות כרגע."
        return "\n".join([f"{t['id']}. {t['name']} ({t['priority']}) - {t['date']}" for t in self.tasks])

# דוגמה לשימוש
if __name__ == "__main__":
    manager = HomeManager()
    print("--- מערכת ניהול ביתית ---")
    print(manager.add_task("לקנות דברים לשבת", "High"))
    print(manager.show_tasks())
