# 字符串的json 处理 json.loads()

字符串的json 处理：
```python
import json

# html 解析
resp = requests.post(url, params=params, headers=headers).text

resp_json = json.loads(resp)

pageData_resultData = resp_json['pageData']['resultData']
```

