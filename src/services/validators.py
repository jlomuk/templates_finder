import re
from datetime import datetime
from typing import Literal, Callable

FieldType = Literal['date', 'email', 'phone', 'text']


def phone_validator(value: str) -> Literal['phone'] | None:
    pattern = re.compile(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$')
    if pattern.match(value):
        return 'phone'


def email_validator(value: str) -> Literal['email'] | None:
    pattern = re.compile(r'^[\w\.]+@[\w]{2,}\.+[\w]{2,4}$')
    if pattern.match(value):
        return 'email'


def date_validator(value: str) -> Literal['date'] | None:
    patterns = ('%Y.%m.%d', '%d.%m.%Y')
    for pattern in patterns:
        try:
            datetime.strptime(value, pattern)
            return 'date'
        except ValueError as e:
            continue


DEFAULT_VALIDATORS = (date_validator, phone_validator, email_validator)


def root_validator(value: str, validators: list[Callable] = DEFAULT_VALIDATORS) -> FieldType:
    for func in validators:
        result = func(value.strip())
        if result is not None:
            return result
    return 'text'
