# hashlib - 模块

`hashlib` 模块定义了用于访问不同加密散列算法的 API。<br />要使用特定的哈希算法，需要先用适当的构造函数或`new()`创建哈希对象。<br />然后，无论使用何种算法，对象都使用相同的 API。

##### md5 示例
```python
import hashlib

from hashlib_data import lorem

h = hashlib.md5()
h.update(lorem.encode('utf-8'))
print(h.hexdigest())	# 3f2fd2c9e25d60fb0fa5d593b802b7a8

```

##### SHA1 示例

```python
import hashlib

from hashlib_data import lorem

h = hashlib.sha1()
h.update(lorem.encode('utf-8'))
print(h.hexdigest())	# ea360b288b3dd178fe2625f55b2959bf1dba6eef

```

