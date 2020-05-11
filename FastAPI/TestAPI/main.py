'''
@Author: _zone
@Date: 2020-05-11 15:52:00
@LastEditTime: 2020-05-11 18:37:47
@FilePath: /FastAPIDemo/TestAPI/main.py
'''


from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()


# 学生用户信息 model
class StudentModel(BaseModel):
    name: str
    student_id: int
    age: int
    height: int
    weight: int
    sex: str


name = "Jack Ma"
student_id = 15703
age = 22
height = 180
sex = "男"
weight = "150"


@app.get("/test/a={a}&b={b}")
def recive():

    res = {"name": name,
           "student_id": student_id,
           "age": age,
           "height": height,
           "sex": sex,
           "weight": weight}

    resArray = [res, res, res, res, res]

    return resArray


@app.get("/test/student_data")
def get_student_data():

    res = {"name": name,
           "student_id": student_id,
           "age": age,
           "height": height,
           "sex": sex,
           "weight": weight}

    resArray = [res, res, res, res, res]

    resJson = {"sam": resArray, "hero": resArray, "lucky": resArray}

    return resJson


# 公共调用方法
def user_data(model: StudentModel):

    res = {"name": model.name,
           "student_id": model.student_id,
           "age": model.age,
           "height": model.height,
           "sex": model.sex,
           "weight": model.weight}

    resArray = [res, res, res, res, res]
    return resArray


# post 接收参数用户信息录入
@app.post("/test/send_student_data/")
def send_student_data(model: StudentModel):

    resArray = user_data(model)
    resJson = {"sam": resArray, "hero": resArray, "lucky": resArray}
    return resJson


if __name__ == "__main__":
    uvicorn.run(app=app,
                host='0.0.0.0',
                port=8080,
                workers=1)
