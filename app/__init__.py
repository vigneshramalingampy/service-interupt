from fastapi import FastAPI
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse


def create_app():
    fast_app = FastAPI(
        title="Service Interrupt Framework",
        description="A framework for building service interrupt applications",
        version="1.0.0",
    )
    fast_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return fast_app


app: FastAPI = create_app()

@app.get("/")
async def root():
    return JSONResponse(
        content={
            "message": "Welcome to service interrupt framework!",
            "status": "ok",
        },
        status_code=status.HTTP_200_OK,
    )


@app.get("/health")
async def health():
    return JSONResponse(
        content={
            "message": "Service is healthy!",
            "status": "ok",
        },
        status_code=status.HTTP_200_OK,
    )
