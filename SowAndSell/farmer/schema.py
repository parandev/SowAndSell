from pydantic import BaseModel


class FarmerSchema(BaseModel):
    id: int
    name: str
    total_land_in_acres: int
    address: str
