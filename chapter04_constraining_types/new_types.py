#!/usr/bin/env python3

from typing import NewType


class Egg:

    def __init__(self):
        self.cooked = False


Omelet = NewType("Omelet", Egg)


def cook_egg(egg: Egg) -> Omelet:
    assert egg.cooked is False
    egg.cooked = True
    return Omelet(egg)


def main():
    egg = Egg()
    # guarantee that the egg will always be cooked before serving because
    # we will only ever serve a type of `Omelet`
    omelet = cook_egg(egg)
    print("Is the egg cooked? {}".format(omelet.cooked))


if __name__ == "__main__":
    main()
