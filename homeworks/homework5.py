import time

# first task

class User:

    def __init__(self, name, role):
        self.name = name
        self.role = role

def is_admin(func):
    def wrapper(user, *args, **kwargs):
        if user.role == "admin":
            return func(user, *args, **kwargs)
        else:
            print("У вас нет доступа")

    return wrapper

@is_admin
def delete_video(user):
    print("Видео удалено")

# second task

def timer(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()  # Время до запуска функции
        result = func(*args, **kwargs)  # Выполнение функции
        end_time = time.time()  # Время после выполнения функции

        execution_time = end_time - start_time
        print(f"Время выполнения: {execution_time:.1f} секунд")
        return result

    return wrapper

@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")

if __name__ == "__main__":
    admin_user = User("Ardager", "admin")
    regular_user = User("Bek", "user")

    print("First task")
    print(f"Попытка от лица {admin_user.name}:")
    delete_video(admin_user)

    print(f"Попытка от лица {regular_user.name}:")
    delete_video(regular_user)

    print("Second task")
    download_video()