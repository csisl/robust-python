# Collection Types

**collection**: a grouping of data

## Homogeneous VS Heterogeneous

*Homogeneous* collections have values of the same type.
*Heterogeneous* collections have different types.

Standard collection types such as lists, tuples, dictionaries and a few other are
fine for homogeneous collections. But they don't usually solve the issue of a
heterogeneous collection.

```python
personal_info = ("123 Street", 8675309, ["Ms", "Smith"])
```

Kind of weird to have a tuple with a string, int, and list right?

## TypedDict

TypedDicts are good for when you need to store heterogeneous data in a dictionary.
It makes it clear what data types are in your collection.

```python
class PII(TypedDict):
    address: str
    phone: int
    name = List[str]
```

## Generics 

A type to indicate it doesn't matter what type is being used.

```python
from typing import TypeVar

T = TypeVar('T')
my_list: list[T]
```
