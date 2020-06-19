# pathlib - 模块

### 构建路径

要创建引用相对于现有路径值的新路径，可以使用 `/` 运算符来扩展路径，运算符的参数可以是字符串或其他路径对象。

```python
import pathlib

usr = pathlib.PurePosixPath('/usr')
print(usr)	# /usr

usr_local = usr / 'local'
print(usr_local)	# /usr/local

usr_share = usr / pathlib.PurePosixPath('share')
print(usr_share)	# /usr/share

```

