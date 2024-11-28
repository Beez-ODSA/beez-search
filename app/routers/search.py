from fastapi import APIRouter

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/")
async def search_service():
    return {"message": "This is the search endpoint"}