import requests, os


class GoogleMapAPI:
    """
    Класс включающий сценарии по отправке post запросов -
    создаются 5 локаций и сохраняются их place_id в файл. С помощью
    метода get получаем информацию по сохраненным place_id. С помощью
    метода delete удаляем информацию о 2-й и 4-й локации и записываем в файл
    только те place_id, что остались в системе. Далее, метод get
    проверяет, что оставшиеся локации доступны.
    """
    list_with_status_code_200_after_deleting = []
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path_1 = os.path.join(SCRIPT_DIR, 'place_id_parameters.txt')
    file_path_2 = os.path.join(SCRIPT_DIR, 'id_parameters_after_deleting.txt')

    def do_post_request(self):
        """Отправляем post запросы, сохраняя place_id"""
        json_format = {
            "location": {

                "lat": -38.383494,

                "lng": 33.427362

            }, "accuracy": 50,

            "name": "Frontline house",

            "phone_number": "(+91) 983 893 3937",

            "address": "29, side layout, cohen 09",

            "types": [

                "shoe park",

                "shop"

            ],

            "website": "http://google.com",

            "language": "French-IN"
        }
        url = 'https://rahulshettyacademy.com/maps/api/place/add/json?key=qaclick123'
        list_with_place_ids = []
        for _ in range(5):
            list_with_place_ids.append(requests.post(url, json=json_format).json()['place_id'])
        with open(self.file_path_1, 'w') as file:
            file.write('\n'.join(list_with_place_ids))
        print('Все 5 post запросов выполнены, place_id записаны в файл\nДалее идут get запросы по данным place_id:\n')

    def do_get_request(self):
        """Отправляем get запросы по ранее сохраненным place_id"""
        url = 'https://rahulshettyacademy.com/maps/api/place/get/json?key=qaclick123'
        with open(self.file_path_1, 'r') as file:
            timed_list_with_place_ids = file.readlines()
            for place_id in timed_list_with_place_ids:
                new_url = url + '&place_id=' + place_id.strip('\n')
                response = requests.get(new_url)
                if response.status_code != 404 :
                    assert response.status_code == 200
                    print(new_url, 'Статус код 200\n', sep='\n')

    def do_delete_request(self):
        """Удаляем запросы со 2-м и 4-м place_id"""
        url = 'https://rahulshettyacademy.com/maps/api/place/delete/json?key=qaclick123'
        with open(self.file_path_1, 'r') as file:
            timed_list_with_place_ids = file.readlines()
            for index, place_id in enumerate(timed_list_with_place_ids, 1):
                if index == 2 or index == 4:
                    json_delete_location = {
                        "place_id": place_id.strip()
                    }
                    response = requests.delete(url, json=json_delete_location)
                    assert response.status_code == 200
                    print(f'Удаление по place_id - {place_id.strip()} прошло успешно, статус код 200\n', sep='\n')
                else:
                    self.list_with_status_code_200_after_deleting.append(place_id.strip())

        with open(self.file_path_2, 'w') as file:
            file.write('\n'.join(self.list_with_status_code_200_after_deleting))

gm = GoogleMapAPI()
gm.do_post_request()
gm.do_get_request()
gm.do_delete_request()
gm.do_get_request()