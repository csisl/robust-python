# Constraining Types

Advanced type annotations can be used with the **typing** module.

```python
from typing import Optional, Union, Literal, Annotated, NewType, Final, Dict, List
```

### Optional

  * When an object can have a value of `None`
  * `Optional[Object]`

### Union
  
  * When there are multiple possible types
  * Union[str, list]

### Literal
  
  * To restrict developers to specific values

### Annotated

  * Provides additional description of the type

### NewType

  * Restricts a type to a specific context

### Final

  * Prevents variables from being rebound to a new value


