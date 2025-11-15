from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from app.database import engine
from app.models import Base
from app.routes import auth, users, products, orders

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce API",
    description="A production-ready e-commerce backend API",
    version="1.0.0"
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]   # or ["fastapi-e-commerce.onrender.com"]
)

# 🔥 Correct CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://e-commerce-front-ebon.vercel.app",  # Vercel frontend
        "http://localhost:5173",                     # Local dev (vite)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)


@app.get("/")
def read_root():
    return {"message": "E-Commerce API is running!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
