from database.db import find_all_forms
from services.validators import root_validator
from settings import logger


async def check_exists_template(form: dict, db):
    validated_form = {key: root_validator(value) for key, value in form.items()}
    result = await find_all_forms(db)
    logger.debug(f"fetch data from db : {result}")

    for name, fields in result.items():
        if validated_form.items() >= fields.items():
            return {"exists_template": name}
    return validated_form
