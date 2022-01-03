#!/usr/bin/env python3

from typing import List


def send_dog_home(dog: str, dogs: list) -> List[str]:
    dogs.remove(dog)
    return dogs


def walk_dogs(dogs: list):
    for dog in dogs:
        print("Walking dog {}".format(dog))


def main():
    dogs = ["Suzie", "Tom", "Bork"]
    walk_dogs(dogs)
    dogs = send_dog_home("Suzie", dogs)
    walk_dogs(dogs)


if __name__ == "__main__":
    main()
