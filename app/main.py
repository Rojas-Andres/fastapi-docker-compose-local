from fastapi import FastAPI

app = FastAPI(
    title="Testing FastAPI with Docker compose debug",
    description="Testing FastApi with Docker compose",
)


@app.get("/")
async def root():
    return {"message": "melo"}

@app.get("/melisismo")
async def melisismo():
    print("masdasdsad")
    return {"message": "melisismo"}