# jstruct

An eloquent and opinionated python library for nested object models definition offering simple serialization and deserialization into python dictionaries.

## Why?

The deserialization of JSON or yaml into python data types is a common practice useful in many ways.
- Configuration file reading and writing
- REST API message response generation and request processing
- Object-Document Mapping for a document store
- Data import parsing or export generation 

## How?

`JStruct` leverage [attrs](https://www.attrs.org/en/stable/) the great `Classes without boilerplate` library to define structs without boilerplate.

## What?

The result is a simple simple and intuitive syntax familiar to a pythonista that brings `Validation`, `Deserialization` and `Serialization`.

## Requirements

 - Python 3.5 and +

## Installation

Install using pip

```shell
pip install jstruct
```

## Usage

```python
import attr
from typing import List
from jstruct import struct, JList

@struct
class Person:
    first_name: str
    last_name: str

@struct
class RoleModels:
    scientists: List[Person] = JList[Person]


payload = {
    "scientists": [{"first_name": "John", "last_name": "Doe"}] 
}

role_models = RoleModels(**payload)

print(role_models)

# RoleModels(scientists=[Person(first_name='John', last_name='Doe')])

print(attr.asdict(role_models))

# {'scientists': [{'first_name': 'John', 'last_name': 'Doe'}]}

```

## Authors

- **Daniel K.** - [@DanHK91](https://twitter.com/DanHK91) | [https://danielk.xyz](https://danielk.xyz/) 

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/DanH91/jstruct/blob/document-jstruct/LICENSE) file for details
