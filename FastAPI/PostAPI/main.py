'''
@Author: _zone
@Date: 2020-05-08 14:31:53
@LastEditTime: 2020-05-08 15:33:06
@FilePath: /FastAPIDemo/PostAPI/main.py
'''
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Item(BaseModel):
    a: int = None
    b: int = None


@app.post('/test')
def calculate(request_item: Item):
    a = request_item.a
    b = request_item.b
    c = a + b
    res = {"res": c}
    return res


if __name__ == "__main__":
    uvicorn.run(app=app,
                host='0.0.0.0',
                port=8080,
                workers=1)
