from typing import Annotated

from fastapi import FastAPI, Path, Query, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from api.api_v1.api import api_router


app = FastAPI(
    title="SowAndSell",
    summary="Get product from Farmer to Factory",
    version="0.0.1",
)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")


@app.get('/{name}')
def home(name: Annotated[str | None, Path(max_length=50)], age: Annotated[int | None, Query(ge=18)]):
    return {'greet': f'Welcome {name} {age}'}


@app.post('/upload')
def get_file(file: UploadFile):
    return {'filename': file.filename}
