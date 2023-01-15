from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from application.routers import classify

#Execution Command
#uvicorn main:app --host 0.0.0.0 --port 9797 --reload

#Configure API CORS
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(classify.router)
