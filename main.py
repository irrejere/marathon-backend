
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from booth_router import router as booth_router

app = FastAPI()

# 프론트엔드의 로컬 개발 주소 허용
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


@app.get("/")
def read_root():
    return {
        "message": "마라톤 부스 소개 API 서버가 정상적으로 작동합니다!"
    }


app.include_router(booth_router)