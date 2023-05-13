class MealyError(Exception):
    # def __init__(self, method):
    # print(method)

    pass


def raiserr(func):
    try:
        func()
    except MealyError:
        pass


class Mealy:
    def __init__(self):
        self.currentPosition = 'A'

    def tread(self):
        if self.currentPosition == 'A':
            self.currentPosition = 'B'
            return 0
        elif self.currentPosition == 'B':
            self.currentPosition = 'C'
            return 2
        elif self.currentPosition == 'C':
            self.currentPosition = 'D'
            return 3
        elif self.currentPosition == 'E':
            self.currentPosition = 'B'
            return 7
        elif self.currentPosition == 'F':
            self.currentPosition = 'C'
            return 8
        else:
            raise MealyError('tread')

    def hurry(self):
        if self.currentPosition == 'A':
            self.currentPosition = 'D'
            return 1
        elif self.currentPosition == 'C':
            self.currentPosition = 'C'
            return 4
        elif self.currentPosition == 'D':
            self.currentPosition = 'E'
            return 5
        elif self.currentPosition == 'E':
            self.currentPosition = 'F'
            return 6
        else:
            raise MealyError('hurry')


def test():
    o = main()  # A
    assert o.hurry() == 1  # D,1
    assert o.hurry() == 5  # E,5
    assert o.tread() == 7  # B,7
    assert o.tread() == 2  # C,2
    assert o.hurry() == 4  # C,4
    assert o.tread() == 3  # D,3
    raiserr(o.tread)
    assert o.hurry() == 5  # E,5
    assert o.hurry() == 6  # F,6
    assert o.tread() == 8  # C,8
    o = main()
    assert o.tread() == 0  # B,0
    raiserr(o.hurry)


def main():
    return Mealy()
