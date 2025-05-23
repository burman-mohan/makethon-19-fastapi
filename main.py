from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware

load_dotenv()
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends

from routers.agentRoutes import agent_router


# Startup event
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application started..")
    yield
    # Clean up the ML models and release the resources
    print("..Application ended")



app = FastAPI(lifespan=lifespan)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Include routers
app.include_router(agent_router, prefix="/api/llm", tags=["Agents"])





