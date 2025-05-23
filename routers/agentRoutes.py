from typing import Annotated


from typing import List, Annotated
from fastapi import APIRouter,HTTPException, UploadFile, File, Form

from models import GetArchitectureReq, GetArchitectureZipReq
from pydantic_agents import agents
from utils import file_utils
agent_router = APIRouter()

@agent_router.get("/")
async def create_directory():
    response = await agents.main()
    return response

@agent_router.post("/zip/getarchitecture")
async def get_architecture(files: Annotated[list[UploadFile], File()]):
    path_array = file_utils.extract_zip_files(files)
    response = await agents.main(path_array[0])
    return response
