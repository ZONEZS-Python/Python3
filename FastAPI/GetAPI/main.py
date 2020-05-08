'''
@Author: _zone
@Date: 2020-05-08 14:11:38
@LastEditTime: 2020-05-08 15:02:07
@FilePath: /FastAPIDemo/GetAPI/main.py
'''

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/test/a={a}/b={b}')
def calculate(a: int = None, b: int = None):
    c = a + b
    res = {'c': c}
    return res


if __name__ == "__main__":
    uvicorn.run(app=app,
                host='0.0.0.0',
                port=8080,
                workers=1)
