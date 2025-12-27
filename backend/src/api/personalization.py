from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_personalization_root():
    return {"message": "Personalization API is running"}