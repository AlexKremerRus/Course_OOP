


class ListData:
    @staticmethod
    def proccesing() -> list:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


class ListView:
    @staticmethod
    def get_list(sequence: list) -> list:
        assert type(sequence) is list
        print(sequence)

class DictDate:
    @staticmethod
    def proccesing() -> dict:
        return{
           3:"three",
           1:"one",
           2:"two",
           4:"four",
       }

class Adapter(DictDate):
    @staticmethod
    def proccesing() -> list:
        dict_date = DictDate.proccesing()
        return list(dict_date.keys())

if __name__ == "__main__":
    dict_exm = DictDate.proccesing()
    old = ListData.proccesing()
    adapter = Adapter.proccesing()

    ListView.get_list(adapter)
    ListView.get_list(old)
    ListView.get_list(dict_exm) # тут будет ошибка 
