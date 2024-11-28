from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class SearchRequest(BaseModel):
    query: str

@router.post("/search")
async def search_endpoint(request: SearchRequest):
    """
    A POST endpoint for handling search requests.
    """
    if not request.query.strip():  # Check if the query is empty or just whitespace
        raise HTTPException(status_code=422, detail="Query cannot be empty")

    # Mock results for demonstration purposes
    results = [f"Result 1 for {request.query}", f"Result 2 for {request.query}"]
    return {"results": results}