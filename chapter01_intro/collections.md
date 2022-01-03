## Python Collections

It's important to use the right collection to clearly express your intents.
Do you want a list of items with no duplicates? What about a mapping from 
a string to an integer? 

## Terms

**Static indexing**: using a constant literal to index into a collection such as `my_list[1]`
**Mutable**: when something can be changed
**Immutable**: when something cannot be changed

### List

  * A collection to be iterated over
  * Mutable
  * Can have duplicate elements 
  * Rarely use static indexes

### String

  * Collection of characters
  * Immutable

### Generator

  * Collection to be iterated over
  * Never indexed
  * Access is lazy because it uses loops, so takes time/resources
  * Good for computationally expensive or infinite collections

### Tuple

  * Immutable collection
  * Use of indices to retrieve items 
  * Rarely iterated over
  * Set order

### Set

  * Iterable collection
  * No duplicates
  * No ordering of elements

### Dictionary

  * Mapping of key value pairs
  * Keys are unique
  * Iterated over or indexed with keys

### frozenset

  * A `set` that is immutable

### OrderedDict

  * A dictionary that preserves the order of elements based on the time they were
    added to the dictionary
    
### defaultdict

  * A dictionary that provides default values for missing keys

### Counter

  * Counts how many times an element appears


