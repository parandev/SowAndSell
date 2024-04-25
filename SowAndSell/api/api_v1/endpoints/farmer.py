from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.deps import get_db
from farmer.model import Farmer
from farmer.schema import FarmerSchema

router = APIRouter()


@router.get('/')
def greet():
    return {'message': "Welcome Farmer! Let's Sow and Sell"}


@router.post('/all')
def get_farmer(db: Session = Depends(get_db)) -> List[FarmerSchema]:
    return db.query(Farmer).all()
