#!/usr/bin/env python3

from typing import TypedDict, List


class PII(TypedDict):
    address: str
    phone: int
    name: List[str]


def main():
    rando: PII = {"address": "123 Street",
                  "phone": 8675309,
                  "name": ["Ms", "Smith"]}
    print(rando["phone"])


if __name__ == "__main__":
    main()
