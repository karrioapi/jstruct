# jstruct

An eloquent and opinionated python library for nested object models definition offering simple serialization and deserialization into python dictionaries.

[![JStruct](https://github.com/PurplShip/jstruct/workflows/JStruct/badge.svg)](https://github.com/PurplShip/jstruct)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cbe02771e00e42cd882ab48543782b40)](https://www.codacy.com/app/DanH91/jstruct?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=DanH91/jstruct&amp;utm_campaign=Badge_Grade) 	
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Why

The deserialization of JSON or yaml into python data types is a common practice useful in many ways.
  - Configuration file reading and writing
  - REST API message response generation and request processing
  - Object-Document Mapping for a document store
  - Data import parsing or export generation 

## How

`JStruct` leverage [attrs](https://www.attrs.org/en/stable/) the great `Classes without boilerplate` library to define structs without boilerplate.

## What

The result is a simple and intuitive syntax familiar to a pythonista that brings `Validation`, `Deserialization` and `Serialization`.

## Requirements

  - Python 3.6 and +

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

## Contribute

Contributors are welcomed.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/DanH91/jstruct/blob/document-jstruct/LICENSE) file for details
