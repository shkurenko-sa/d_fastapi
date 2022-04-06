from fastapi import APIRouter


router = APIRouter()


@router.put('/create')
async def create_user():
    pass
