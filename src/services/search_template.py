from database.db import find_all_forms
from services.validators import root_validator
from settings import logger


async def check_exists_template(form: dict, db):
    validated_form = {key: root_validator(value) for key, value in form.items()}
    result = await find_all_forms(db)
    logger.debug(f"fetch data from db : {result}")
    for key, value in result.items():
        if all(k in validated_form and validated_form[k] == v for k, v in value.items()):
            return key
    return validated_form
