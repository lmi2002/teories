import requests

from internal_api import setting


class InternalApi:

    @staticmethod
    def obj_json(data):
        lst = []

        x = 0
        while True:
            obj = {}
            for k, v in data.items():
                for num, i in enumerate(v):
                    if num == x:
                        obj.update({k: v[num]})
                        break
            if obj:
                lst.append(obj)
                x += 1
            else:
                break
        return lst

    @staticmethod
    def get_elem_query(data):
        return {k: v for k, v in data.items() if k.startswith('r_')}

    @staticmethod
    def api_request():
        return requests.get(setting.HOST)


class D():
    i = InternalApi()

    data = {
        'r_idd': (1, 3, 4, 5),
        'r_prag_id': (4, 7, 12, 15),

        'levels': (
            {'map': 'true', 'description': 'level', 'level': 1},
            {'map': 'true', 'description': 'level_2', 'level': 2},
            {'map': 'true', 'description': 'level_3', 'level': 3},
            {'map': 'false', 'description': 'level_4', 'level': 4}
        )
    }

    print(i.obj_json(data))
    response = i.api_request()
    cont = response.json()
    print(cont)
    print(i.get_elem_query(data))
