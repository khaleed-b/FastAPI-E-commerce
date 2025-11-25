from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import Base

from app.routes.auth import router as auth_router
from app.routes.users import router as users_router
from app.routes.products import router as products_router
from app.routes.orders import router as orders_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce API",
    description="A production-ready e-commerce backend API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://e-commerce-front-ebon.vercel.app",
        "http://localhost:8000",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(products_router)
app.include_router(orders_router)

@app.get("/")
def read_root():
    return {"message": "E-Commerce API is running!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
