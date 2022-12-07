from fastapi import FastAPI

app = FASTAPI()

test = "Hello World"
@app.get('/')
async def test():
    return test

