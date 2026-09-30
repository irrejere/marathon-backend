
from pydantic import BaseModel


class Booth(BaseModel):
    id: int
    club_name: str
    booth_name: str
    description: str
    activity: str