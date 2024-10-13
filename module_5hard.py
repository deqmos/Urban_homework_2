from time import sleep


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname: str, password: str):
        data_curr_user = ([i.nickname for i in self.users], [j.password for j in self.users])
        # data about user [0] - nickname, [1] - password
        if nickname in data_curr_user[0] and hash(password) in data_curr_user[1]:
            self.current_user = nickname
        else:
            print("Неверно ведён логин или пароль")

    def register(self, nickname: str, password: str, age: int):
        if nickname not in [i.nickname for i in self.users]:
            self.users.append(User(nickname, password, age))
            self.current_user = self.users[-1].nickname
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_out(self):
        self.current_user = None

    def add(self, *add_video):
        for i in add_video:
            self.videos.append(i)

    def get_videos(self, search: str):
        all_videos_in_search = [video.title for video in self.videos if search.lower() in video.title.lower()]
        return all_videos_in_search

    def watch_video(self, name_video):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for video in self.videos:
                if name_video == video.title:
                    age_current_user = [user.age for user in self.users if user.nickname == self.current_user][0]
                    if video.adult_mode and age_current_user > 18:
                        for j in range(1, video.duration + 1):
                            print(j, end=' ')
                            sleep(1)
                        else:
                            print("Конец видео")
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        break


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
ur.log_out()
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.log_out()
ur.log_in('vasya_pupkin', 'F8098FM8fjm9jmi')

