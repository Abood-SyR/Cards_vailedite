from fastapi import APIRouter, status , Body , Header
from models.models import card
from schemas.schema import list_serial 
from fastapi.responses import JSONResponse
from bson import ObjectId
from config.database import list_cards


router = APIRouter()
@router.get("/")
async def read_cards():
    cards = list_serial(list_cards.find())
    return cards



@router.post("/")
async def create_card(c: card):
    list_cards.insert_one(dict(c))
    return JSONResponse({
        "success": True
    }, status.HTTP_201_CREATED)


@router.put("/")
async def edit_card(id: str, c: card):
    list_cards.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(c)})
    return JSONResponse({
        "success": True,
        "state": "card was purchase"
    }, status.HTTP_200_OK)
    

@router.delete("/{id}")
async def delete_user(id: str):
    list_cards.find_one_and_delete({"_id": ObjectId(id)})
    return JSONResponse({
        "success": True,
        "state": "card was deleted"
    }, status.HTTP_200_OK)
