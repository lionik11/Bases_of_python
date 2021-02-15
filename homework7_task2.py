from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, value, count_kind):
        self.value = value
        self.count_kind = count_kind
        self.volume_per_one_kind = 0

    @abstractmethod
    def volume_per_one(self):
        pass

    @property
    def sum_volume(self):
        return round((self.volume_per_one_kind * self.count_kind), 2)


class Coat(Clothes):
    def __init__(self, value, count_kind):
        super().__init__(value, count_kind)
        self.volume_per_one_kind = Coat.volume_per_one(self)

    def __str__(self):
        return "Coat"

    def volume_per_one(self):
        size = self.value
        return round((size / 6.5 + 0.5), 2)


class Suit(Clothes):
    def __init__(self, value, count_kind):
        super().__init__(value, count_kind)
        self.volume_per_one_kind = Suit.volume_per_one(self)

    def __str__(self):
        return "Suit"

    def volume_per_one(self):
        height = self.value
        return 2 * height + 0.3


suits = Suit(150, 5)
coats = Coat(184, 11)

print(suits.sum_volume + coats.sum_volume)
