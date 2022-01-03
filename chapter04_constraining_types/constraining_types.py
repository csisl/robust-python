#!/usr/bin/env python3

from typing import Optional, Union, Literal, Final, Dict
import random
from dataclasses import dataclass


MIN: Final = 0
MAX: Final = 1


@dataclass
class Person:
    name: Literal[str]


def get_random() -> int:
    return random.randint(MIN, MAX)


def get_dict() -> Dict[str, int]:
    return {"one": 1}


def get_list_or_tuple() -> Union[list, tuple]:
    if get_random() == 0:
        return [0, 1]
    else:
        return 0, 1


def get_possible_none() -> Optional[int]:
    if get_random() == 0:
        return 0
    else:
        return None


def print_vals_and_types(return_vals: list) -> None:
    for return_val in return_vals:
        print("Got <{}> of type {}".format(return_val, type(return_val)))


def main():
    return_vals = [get_possible_none(),
                   get_list_or_tuple(),
                   get_dict()]

    print_vals_and_types(return_vals)


if __name__ == "__main__":
    main()
