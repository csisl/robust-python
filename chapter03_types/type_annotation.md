# Type Annotation

As mentioned in [types.md](types.md), Python is a dynamically typed language.
Since types won't be known until runtime, it's important to annotate the types 
with **type hints**. Python won't throw errors based on these hints, but it's
helpful for developers to know what they are dealing with. 

For the following two functions declarations, which one is more clear and easy to work with?

```python
def do_thing(address, age, name): 
```

```python
def do_thing(address: str, age: int, name: list) -> Person:
```

In the first method declaration, it's unclear if `do_thing` will return something
and what the types of the arguments are. Did you know, from a first pass, that name
was supposed to be a `list`?

## Typing module

```python
from typing import Dict, List, Optional
```

The typing module is super useful to extend what type hints we can use.
Just using a return type of `list` or `dict` might not always be enough.
However, `Dict[str, list]` or `List[str]` thanks to the **typing module**
helps a ton.

More will be discussed in [Constraing Types - chapter 4](../chapter04_constraining_types/constraining_types.md).
