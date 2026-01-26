import requests, warnings, os


warnings.filterwarnings('ignore')

def characters():
    """
    Получает список всех уникальных персонажей (кроме Дарта Вейдера),
    которые снимались в тех же фильмах, что и Дарт Вейдер.
    Результат сохраняется в файл в алфавитном порядке.
    """
    link = 'https://swapi.dev/api/people/4/'
    list_with_all_characters = []
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(SCRIPT_DIR, 'file_with_all_chars.txt')
    list_with_all_films_of_DV = requests.get(link, verify=False).json()['films']
    # Проходимся циклом по всем фильмам Дарта Вейдера
    for film in list_with_all_films_of_DV:
        list_with_all_characters_in_certain_film = requests.get(film, verify=False).json()['characters']
        # Проходимся циклом по персонажам каждого фильма
        for char in list_with_all_characters_in_certain_film:
            character_name = requests.get(char, verify=False).json()['name']
            if character_name != 'Darth Vader' and character_name not in list_with_all_characters:
                list_with_all_characters.append(character_name)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(sorted(list_with_all_characters)))

characters()