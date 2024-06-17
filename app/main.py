from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def test():
    return f"it's working!"