from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from booth_router import router as booth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# 부스 데이터 API 등록
app.include_router(booth_router)

# 프론트엔드 파일 경로
FRONTEND_DIR = Path(__file__).parent / "frontend"

# HTML, CSS, JavaScript, 이미지 파일 제공
app.mount(
    "/",
    StaticFiles(directory=FRONTEND_DIR, html=True),
    name="frontend",
)