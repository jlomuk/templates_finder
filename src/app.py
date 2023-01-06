from fastapi import FastAPI, Request, Depends

from database.db import connect_db, get_db
from services.search_template import check_exists_template
from settings import logger

app = FastAPI()


@app.on_event("startup")
async def startapp():
    connect_db()


@app.post("/get_form")
async def get_form(request: Request, db=Depends(get_db)):
    form = await request.form()
    logger.debug("Received form %s from %s", dict(form), request.client)

    result = await check_exists_template(dict(form), db)

    if not result:
        logger.debug("form is not found in db")
        return {"detail": "Передана невалидная форма"}
    return result

