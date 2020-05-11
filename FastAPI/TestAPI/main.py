
'''
@Author: _zone
@Date: 2020-05-11 15:52:00
@LastEditTime: 2020-05-11 17:17:51
@FilePath: /FastAPIDemo/TestAPI/main.py
'''


from fastapi import FastAPI
# import json
import uvicorn

app = FastAPI()

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


if __name__ == "__main__":
    uvicorn.run(app=app,
                host='0.0.0.0',
                port=8080,
                workers=1)
