'''
@Author: _zone
@Date: 2020-05-22 15:50:45
@LastEditTime: 2020-05-26 14:25:18
@FilePath: /LogApi/main.py
'''


from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/test/a={a}/b={b}')
def get_info_data(a: int = 0, b: int = 0):

    name = 'alex'
    age = 20
    sex = '男'
    height = 175

    msg = 'SUCCESS'
    code = 200

    info = {
        'name': name,
        'age': age,
        'sex': sex,
        'height': height
    }

    data = [info, info, info, info, info]

    json = {
        'code': code,
        'msg': msg,
        'data': data
    }

    return json

    # 访问 0.0.0.0:8080/docs
    # 打印出来的信息
    # {
    #   "code": 200,
    #   "msg": "成功",
    #   "data": {
    #     "name": "alex",
    #     "age": 20,
    #     "sex": "男",
    #     "height": 175
    #   }
    # }


if __name__ == "__main__":
    uvicorn.run(app=app,
                host='0.0.0.0',
                port=8080,
                workers=1)
