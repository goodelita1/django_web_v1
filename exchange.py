from abc import ABC
from functools import singledispatchmethod


class ABC:
    def __init__(self, money: float) -> None:
        self.money: float = money


class Dollars(ABC):
    def __init__(self, dollars: float) -> None:
        self.dollars: float = dollars


class Euro(ABC):
    def __init__(self, euro: float) -> None:
        self.euro: float = euro


class Uah(ABC):
    def __init__(self, uah: float) -> None:
        self.uah: float = uah


class InputValues:
    def __init__(self) -> None:
        self.exchange_info: list = []

    def input_exchange(self) -> list:
        print("plz input type of money '" "usd eur uah" "'")
        money_type = input()
        self.exchange_info.append(money_type)
        print("plz input first value")
        first = input()
        self.exchange_info.append(first)
        print("plz input type of money '" "usd eur uah" "'")
        money_type = input()
        self.exchange_info.append(money_type)
        print("plz input second value")
        second = input()
        self.exchange_info.append(second)
        return self.exchange_info


class Convert:
    def __init__(self) -> None:
        pass

    @singledispatchmethod
    def Exchange_to_dollars(self, convert_money: Dollars) -> Dollars:
        result = convert_money
        return result

    @Exchange_to_dollars.register
    def _(self, convert_money: Euro) -> Dollars:
        result = Dollars(float(convert_money.euro) * 1.05)
        return result

    @Exchange_to_dollars.register
    def _(self, convert_money: Uah) -> Dollars:
        result = Dollars(float(convert_money.uah) / 41.8)
        return result


class Exchange_math:
    def __init__(self, value: Dollars) -> None:
        self.value: Dollars = value

    def __add__(self, other):
        return Exchange_math(self.value + other.value)

    def __sub__(self, other):
        return Exchange_math(self.value - other.value)

    def __mul__(self, other):
        return Exchange_math(self.value * other.value)

    def __div__(self, other):
        return Exchange_math(self.value / other.value)


class Check_types(InputValues):
    def __init__(self) -> None:
        pass

    def check_types(self) -> list:
        data = []
        exc = InputValues()
        input_info = exc.input_exchange()
        if input_info[0] == "uah":
            first = Uah(input_info[1])
        elif input_info[0] == "usd":
            first = Dollars(input_info[1])
        elif input_info[0] == "eur":
            first = Euro(input_info[1])
        else:
            print("error")
        data.append(first)
        if input_info[2] == "uah":
            second = Uah(input_info[3])
        elif input_info[2] == "usd":
            second = Dollars(input_info[3])
        elif input_info[2] == "eur":
            second = Euro(input_info[3])
        else:
            print("error")
        data.append(second)
        return data


class CLI:
    def __init__(self) -> None:
        pass

    def call_all(self):
        data = Check_types().check_types()
        converting = Convert()
        first_val = converting.Exchange_to_dollars(data[0])
        second_val = converting.Exchange_to_dollars(data[1])
        sum_of_val_first = Exchange_math(float(first_val.dollars))
        sum_of_val_second = Exchange_math(float(second_val.dollars))
        sum_of_val = sum_of_val_first + sum_of_val_second
        print(sum_of_val.value)


def main():
    call = CLI().call_all()


if __name__ == "__main__":
    main()
