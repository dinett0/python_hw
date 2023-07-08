class MealyStateMachine:
    def __init__(self):
        self.state = "A"

    def exit(self):
        if self.state == "A":
            self.state = "C"
            return 1
        if self.state == "C":
            self.state = "D"
            return 3
        if self.state == "D":
            self.state = "B"
            return 5
        if self.state == "E":
            self.state = "A"
            return 8
        raise MealyError("exit")

    def march(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "D":
            self.state = "A"
            return 6
        if self.state == "E":
            self.state = "F"
            return 7
        raise MealyError("march")

    def bolt(self):
        if self.state == "B":
            self.state = "C"
            return 2
        if self.state == "D":
            self.state = "E"
            return 4
        if self.state == "F":
            self.state = "G"
            return 9
        raise MealyError("bolt")


class MealyError(Exception):
    pass


def main():
    return MealyStateMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.exit() == 1
    assert o.exit() == 3
    assert o.bolt() == 4
    assert o.march() == 7
    assert o.bolt() == 9
    o = main()
    assert o.march() == 0
    assert o.bolt() == 2
    assert o.exit() == 3
    assert o.exit() == 5
    assert o.bolt() == 2
    assert o.exit() == 3
    assert o.march() == 6
    o = main()
    assert o.exit() == 1
    assert o.exit() == 3
    assert o.bolt() == 4
    assert o.exit() == 8
    o.state = "X"
    raises(lambda: o.exit(), MealyError)
    raises(lambda: o.march(), MealyError)
    raises(lambda: o.bolt(), MealyError)
