# 1 Matrix
class Matrix:
    values: list

    def __init__(self, values: list):
        self.values = values

    def __add__(self, other):
        new_matrix = []
        ind1 = 0
        while ind1 < len(self.values):
            ind2 = 0
            part_matrix = []
            while ind2 < len(self.values[ind1]):
                part_matrix.append(self.values[ind1][ind2] + other.values[ind1][ind2])
                ind2 += 1
            new_matrix.append(part_matrix)
            ind1 += 1
        return new_matrix

    def __str__(self):
        return f"{self.values}"


my_matrix1 = Matrix([[1, 2], [3, 4], [5, 6]])
my_matrix2 = Matrix([[2.5, 3], [4, 5], [-5, -7]])
print("Первая матрица: ", my_matrix1.__str__())
print("Вторая матрица: ", my_matrix2.__str__())
print("Сумма матриц: ", my_matrix1 + my_matrix2)

# 2 Clothes

from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def coast(self):
        pass

    @staticmethod
    def summa(*args):
        cnt = 0
        for j in args:
            cnt += j.coast
        return f'Общий расход ткани составляет {cnt} метров'


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def coast(self):
        return int(self.v / 6.5 + 0.5)


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def coast(self):
        return int(2 * self.h + 0.3)


my_coat = Coat(42)
my_suit = Suit(1.8)
print(my_suit.coast)
print(my_coat.coast)
print(f'Расход ткани на пальто составляет {my_coat.coast} метров')
print(f'Расход ткани на костюм составляет {my_suit.coast} метров')
print(Clothes.summa(my_suit, my_coat))


# 3. Cells


class Cell:
    def __init__(self, num: int):
        self.num = num

    def make_order(self, num: int):
        ind = 1
        cell_string = ""
        if num != "\nНевозможно выполнить вычитание: уменьшаемое число меньше вычитаемого":
            if num != "\nНевозможно выполнить деление клеток, делитель равен 0":
                if num != 0:
                    while ind <= num:
                        if ind % 5 != 0:
                            cell_string = cell_string + "*"
                        else:
                            cell_string = cell_string + "*\n"
                        ind += 1
        return cell_string

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num >= other.num:
            return self.num - other.num
        else:
            return "\nНевозможно выполнить вычитание: уменьшаемое число меньше вычитаемого"

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        if other.num == 0:
            return "\nНевозможно выполнить деление клеток, делитель равен 0"
        else:
            return self.num // other.num


cell1 = Cell(8)
cell2 = Cell(6)
cell3 = Cell(9)
cell4 = Cell(0)
print(f"Складываем {cell1.num} и {cell2.num}: ", cell1 + cell2)
print(Cell(cell1 + cell2).make_order(cell1 + cell2))
print(f"Вычитаем {cell1.num} и {cell2.num}: ", cell1 - cell2)
print(Cell(cell1 - cell2).make_order(cell1 - cell2))
print(f"Вычитаем {cell1.num} и {cell1.num}: ", cell1 - cell1)
print(Cell(cell1 - cell1).make_order(cell1 - cell1))
print(f"Вычитаем {cell1.num} и {cell3.num}: ", cell1 - cell3)
print(Cell(cell1 - cell3).make_order(cell1 - cell3))
print(f"Умножаем {cell1.num} на {cell2.num}: ", cell1 * cell2)
print(Cell(cell1 * cell2).make_order(cell1 * cell2))
print(f"Делим {cell1.num} на {cell2.num}: ", cell1 / cell2)
print(Cell(cell1 / cell2).make_order(cell1 / cell2))
print(f"Делим {cell1.num} на {cell4.num}: ", cell1 / cell4)
print(Cell(cell1 / cell4).make_order(cell1 / cell4))



