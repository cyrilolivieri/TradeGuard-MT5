from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="TradeGuard MT5 API",
    description="API pour TradeGuard MT5 - SaaS de trade management et prop firm compliance",
    version="0.1.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "ok", "version": "0.1.0"}

@app.get("/")
async def root():
    return {
        "message": "TradeGuard MT5 API",
        "docs": "/docs",
        "health": "/health"
    }
