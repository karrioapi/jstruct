import attr
from functools import reduce
from typing import List, Dict


REQUIRED = True


@attr.s(auto_attribs=True)
class _JStruct:
    def __getitem__(self, arguments):
        class_, required_, *kwargs = arguments if isinstance(arguments, tuple) else (arguments, False)

        def build(args) -> class_:
            return class_(**args) if isinstance(args, dict) else args
        default_ = dict(default=attr.NOTHING if required_ else None)
        return attr.ib(
            **default_,
            converter=build,
            **dict(reduce(lambda r, d: r + list(d.items()), kwargs, []))
        )


@attr.s(auto_attribs=True)
class _JList:
    def __getitem__(self, arguments):
        class_, required_, *kwargs = arguments if isinstance(arguments, tuple) else (arguments, False)

        def build(args) -> List[class_]:
            if isinstance(args, list):
                items = args
            else:
                items = [args]
            return [
                (class_(**item) if isinstance(item, dict) else item)
                for item in items
            ]
        default_ = dict(default=attr.NOTHING if required_ else [])
        return attr.ib(
            **default_,
            converter=build,
            **dict(reduce(lambda r, d: r + list(d.items()), kwargs, []))
        )


@attr.s(auto_attribs=True)
class _JDict:
    def __getitem__(self, arguments):
        key_type, value_type, required_, *kwargs = arguments if isinstance(arguments, tuple) else (arguments, False)

        def build(args) -> Dict[key_type, value_type]:
            return {
                key_type(key): (value_type(**value) if isinstance(value, dict) else value)
                for (key, value) in args.items()
            }
        default_ = dict(default=attr.NOTHING if required_ else {})
        return attr.ib(**default_, converter=build, **kwargs)


JStruct = _JStruct()
JList = _JList()
JDict = _JDict()
