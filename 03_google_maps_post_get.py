import requests, os


class GoogleMapAPI:
    """
    Класс включающий сценарии по отправке post запросов -
    создаются 5 локаций и сохраняются их place_id в файл. С помощью
    метода get получаем информацию по сохраненным place_id.
    """
    base_url = 'https://rahulshettyacademy.com'
    resource = '/maps/api/place/add/json'
    parameter = '?key=qaclick123'
    url = base_url + resource + parameter
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(SCRIPT_DIR, 'post_id_parameters.txt')
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

    def do_post_request(self):
        """Отправляем 5 post запросов, сохраняя place_id"""
        list_with_place_ids = []
        for _ in range(5):
            list_with_place_ids.append(requests.post(self.url, json=self.json_format).json()['place_id'])
        with open(self.file_path, 'w') as file:
            file.write('\n'.join(list_with_place_ids))
        print('Все 5 post запросов выполнены, place_id записаны в файл\nДалее идут get запросы по данным place_id:\n')

    def do_get_request(self):
        """Отправляем get запросы по ранее сохраненным place_id"""
        list_with_place_ids = []
        with open(self.file_path, 'r') as file:
            timed_list_with_place_ids = file.readlines()
            for place_id in timed_list_with_place_ids:
                list_with_place_ids.append(place_id.strip('\n'))

        for place_id in list_with_place_ids:
            url = self.url + '&place_id=' + place_id
            assert requests.get(url).status_code == 200
            print(url, 'Статус код 200\n', sep='\n')

gm = GoogleMapAPI()
gm.do_post_request()
gm.do_get_request()