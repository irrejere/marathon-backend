
from fastapi import APIRouter, HTTPException
from booth_data import booths
from schemas import Booth

router = APIRouter()


@router.get("/booths", response_model=list[Booth])
def get_booths():
    return [Booth(**booth) for booth in booths]


@router.get("/booths/{booth_id}", response_model=Booth)
def get_booth(booth_id: int):
    for booth in booths:
        if booth["id"] == booth_id:
            return booth

    raise HTTPException(
        status_code=404,
        detail="부스를 찾을 수 없습니다."
    )