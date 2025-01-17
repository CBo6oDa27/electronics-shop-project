import csv


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return  self.name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            self.__name = new_name[0:10]
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, file_name):
        cls.all = []
        items = []
        try:
            with open(file_name, 'r', newline='', encoding='windows-1251') as file:
                reader = csv.reader(file)
                # Пропустим первую строчку с заголовками
                next(reader)
                for row in reader:
                    name, price, quantity = row
                    item = cls(name, price, quantity)
                    items.append(item)
            return items

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

        except ValueError:
            raise InstantiateCSVError('Файл item.csv поврежден')



    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    @staticmethod
    def string_to_number(number_as_string):
        return int(float(number_as_string))

