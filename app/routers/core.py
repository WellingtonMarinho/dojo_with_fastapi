import logging
from typing import Annotated, Union

from fastapi import APIRouter, BackgroundTasks, Depends
from sqlmodel import Session

from app.models.customer import Customer
from app.database import get_session


logger = logging.getLogger("dojo_application")

SessionDep = Annotated[Session, Depends(get_session)]
router = APIRouter()


def task_to_background_process():
    logger.info('Start task')
    logger.info("Must be execute after request has been made response successfully")
    # process_anything()
    logger.info('End task')


@router.get("/")
def read_root(to_process_background: BackgroundTasks):
    logger.info('Start request ')

    to_process_background.add_task(task_to_background_process)

    logger.info('End request')
    return {"Hello": "World 232 "}


@router.post("/customer/")
def create_hero(customer: Customer, session: SessionDep) -> Customer:
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
