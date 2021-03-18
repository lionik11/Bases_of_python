class Data:
    def __init__(self, value):
        self.value = value

    @classmethod
    def extract_values(cls, data_extract):
        return [int(el) for el in data_extract.split("-")]

    @staticmethod
    def values_validation(data):
        if Data.extract_values(data)[0] > 31:
            raise ValueError("Ошибка в числе месяца")
        if 1 <= Data.extract_values(data)[1] > 12:
            raise ValueError("Ошибка в месяце")
        if Data.extract_values(data)[0] > 31:
            raise ValueError("Ошибка в числе месяца")
        return "Все числе верны"


my_data = "21-12-2021"
k = Data.extract_values(my_data)
print(k)
lm = Data.values_validation(my_data)
print(lm)
