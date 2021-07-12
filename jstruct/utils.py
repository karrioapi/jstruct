import typing
import logging

logger = logging.getLogger(__name__)


def instantiate(class_: typing.Type, args: dict):
    supported_args = {key: val for key, val in args.items() if key in class_.__annotations__}
    unsupported_args = {key: val for key, val in args.items() if key not in class_.__annotations__}

    if any(unsupported_args.items()):
        logger.warning(f"unknown arguments {unsupported_args}")

    return class_(**supported_args)
