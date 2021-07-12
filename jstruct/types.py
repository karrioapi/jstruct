import attr
import logging
from functools import reduce
from typing import List, Dict, Union, Tuple, Optional

import jstruct.utils as utils

logger = logging.getLogger(__name__)
REQUIRED = True


struct = attr.s(auto_attribs=True)


class _JStruct:
    """A typing definition wrapper used to defined nested struct.

        @struct
        class Child:
            child_prop1: int

        @struct
        class Parent:
            parent_prop: str
            child: Child = JStruct[Child]
    """

    def __getitem__(
        self, arguments: Union[type, Tuple[type, Optional[bool], Optional[dict]]]
    ):
        """Override the `[]` operator to offer a typing wrapper syntactic sugar.

        :arguments is either a `type` or a `tuple`
            - type: the nested struct type (or class)
            - tuple: ( type, REQUIRED, {dictionary of extra attr.ib arguments} )

        :return a property initializer from attrs (attr.ib)
        """

        class_, required_, *kwargs = (
            arguments if isinstance(arguments, tuple) else (arguments, False)
        )

        def converter(args) -> class_:
            return utils.instantiate(class_, args) if isinstance(args, dict) else args

        default_ = dict(default=attr.NOTHING if required_ else None)
        return attr.ib(
            **default_,
            converter=converter,
            **dict(reduce(lambda r, d: r + list(d.items()), kwargs, []))
        )


class _JList:
    """A typing definition wrapper used to defined nested collection (list) of struct.

        @struct
        class Child:
            child_prop1: int

        @struct
        class Parent:
            parent_prop: str
            children: List[Child] = JList[Child]
    """

    def __getitem__(
        self, arguments: Union[type, Tuple[type, Optional[bool], Optional[dict]]]
    ):
        """Override the `[]` operator to offer a typing wrapper syntactic sugar.

        :arguments is either a `type` or a `tuple`
            - type: the nested struct type (or class)
            - tuple: ( type, REQUIRED, {dictionary of extra attr.ib arguments} )

        :return a property initializer from attrs (attr.ib)
        """

        class_, required_, *kwargs = (
            arguments if isinstance(arguments, tuple) else (arguments, False)
        )

        def converter(args) -> List[class_]:
            if isinstance(args, list):
                items = args
            else:
                items = [args]

            return [
                (utils.instantiate(class_, item) if isinstance(item, dict) else item) for item in items
            ]

        default_ = dict(default=attr.NOTHING if required_ else [])

        return attr.ib(
            **default_,
            converter=converter,
            **dict(reduce(lambda r, d: r + list(d.items()), kwargs, []))
        )


class _JDict:
    """A typing definition wrapper used to defined nested dictionary struct typing.

        from jstruct import struct
        from jstruct.type import _JDict

        JDict = _JDict()

        @struct
        class Child:
            child_prop1: int

        @struct
        class Parent:
            parent_prop: str
            children: Dict[str, Child] = JDict[str, Child]
    """

    def __getitem__(self, arguments: Tuple[type, type, Optional[bool], Optional[dict]]):
        """Override the `[]` operator to offer a typing wrapper syntactic sugar.

        :arguments is a `tuple`
            ( key_type, value_type, REQUIRED, {dictionary of extra attr.ib arguments} )

        :return a property initializer from attrs (attr.ib)
        """

        key_type, value_type, required_, *kwargs = (
            arguments + (False,) if len(arguments) > 3 else arguments
        )

        def converter(args) -> Dict[key_type, value_type]:
            return {
                key_type(key): (
                    utils.instantiate(value_type, value)
                    if isinstance(value, dict) else value
                )
                for (key, value) in args.items()
            }

        default_ = dict(default=attr.NOTHING if required_ else {})
        return attr.ib(
            **default_,
            converter=converter,
            **dict(reduce(lambda r, d: r + list(d.items()), kwargs, []))
        )


# Instance of _JStruct
JStruct = _JStruct()

# Instance of _JList
JList = _JList()

# Instance of _JDict
JDict = _JDict()
