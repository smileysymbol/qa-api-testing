import requests


class ChuckNorris:
    """
    Класс включающий сценарии по отправке запросов,
    с целью получения шуток с Чаком Норрисом по каждой из доступной категории.
    """
    def __init__(self):
        self.link_with_all_categories = 'https://api.chucknorris.io/jokes/categories'

    def get_categories(self):
        """Получаем все категории шуток"""
        return requests.get(self.link_with_all_categories).json()

    def get_a_joke_each_category(self):
        """Проходим циклом по каждой категории, чтобы достать шутку"""
        list_with_all_categories = self.get_categories()
        for category in list_with_all_categories:
            print(requests.get(f'https://api.chucknorris.io/jokes/random?category={category}').json()['value'])
            assert requests.get(f'https://api.chucknorris.io/jokes/random?category={category}').status_code == 200
            print('Статус код 200\n')

cn = ChuckNorris()
cn.get_a_joke_each_category()
