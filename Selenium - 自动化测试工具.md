# Selenium - 自动化测试工具

支持各种浏览器，包括Chrome，Safari，Firefox等主流界面式浏览器，如果你在这些浏览器里面安装一个Selenium的插件，那么便可以方便地实现Web界面的测试。<br /><br />
```python
from selenium import webdriver
 
browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
```

运行这段代码，会自动打开浏览器，然后访问百度。<br />如果程序执行错误，浏览器没有打开，那么应该是没有装Chrome浏览器或者Chrome驱动器没有配置在环境变量里。下载驱动，然后将驱动文件路径配置在环境变量即可。(安装要注意选择对应版本的驱动文件)<br />
<br />![image.png](https://cdn.nlark.com/yuque/0/2019/png/235650/1553674625339-227ad35c-7577-4366-83f8-11b509d9fa0e.png#align=left&display=inline&height=419&name=image.png&originHeight=838&originWidth=1888&size=94188&status=done&width=944)

