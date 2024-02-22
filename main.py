import random
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


def generate_data():
    a=random.randint(1,100)
    b=random.randint(1,100)
    c=random.randint(1,100)
    return{
        "cars":a,
        "trucks":b,
        "buses":c
    }
@app.get('/data')
def get_data():
    data=generate_data()
    return JSONResponse(content=data,status_code=200)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
