import requests


class ChuckNorris:
    """
    Класс включающий сценарии по отправке запросов,
    с целью получения шуток с Чаком Норрисом по заданной категории.
    """
    def __init__(self):
        self.link_with_all_categories = 'https://api.chucknorris.io/jokes/categories'

    def get_categories(self):
        """Получаем все категории шуток"""
        return requests.get(self.link_with_all_categories).json()

    def get_a_joke_from_certain_category(self):
        """Просим пользователя ввести категорию и проверяем, доступна ли она"""
        counter = 0
        list_with_all_categories = self.get_categories()
        category = input(f"Доступны следующие категории: {', '.join([category for category in list_with_all_categories])}\nНапишите, какую категорию вы выбираете (у вас 5 попыток): ")
        while category not in list_with_all_categories:
            counter += 1
            category = input(f'Введите новую категорию, ранее введенной категории в списке нет (осталось попыток: {5 - counter}): ')
            if counter == 4:
                response = requests.get(f'https://api.chucknorris.io/jokes/random?category={category}')
                print(f"Статус-код: {response.status_code}\nОшибка: категория не найдена")
                break
        else:
            print(requests.get(f'https://api.chucknorris.io/jokes/random?category={category}').json()['value'])
            assert requests.get(f'https://api.chucknorris.io/jokes/random?category={category}').status_code == 200
            print('Статус код 200')

cn = ChuckNorris()
cn.get_a_joke_from_certain_category()