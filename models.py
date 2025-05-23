from enum import Enum
from typing import List, Optional, Any

from pydantic import BaseModel

class RepoDetails(BaseModel):
    repo_url: str
    repo_type: str
    language: str
    description: Optional[str]


class GetArchitectureReq(BaseModel):
    data: List[RepoDetails]

class GetArchitectureZipReq(BaseModel):
    files: str
    languages: str

