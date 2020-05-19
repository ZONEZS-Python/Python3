<!--
 * @Author: _zone
 * @Date: 2020-05-18 14:20:54
 * @LastEditTime: 2020-05-19 14:05:44
 * @FilePath: /ConnectMySQL/install.md
--> 

# 本篇以安装 Python-3.6.8 版本的 Python依赖库举例

# 准备工作
一般在虚拟环境中使用这种方法，有时候会需要手动添加一些无法自动生成的依赖库
Python项目生成所有依赖包的清单 requirements.txt【pipreqs包】

### 安装pipreqs,并生成requirements.txt清单
pip install pipreqs
### 生成 requirement.txt
pipreqs ./  
### 安装 requirements.txt 依赖包
pip install -r requirements.txt

# 1.0
### 设置基础环境配置
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make

# 1.1
#### 下载
wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tar.xz
### 解压
tar -xvJf  Python-3.6.8.tar.xz
### 切换路径
cd Python-3.6.8
### 安装
./configure prefix=/usr/local/python3
make && make install

# 1.2
### 设置 Python3 名称
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
### 执行命令
python3 -V  # 将会看到 python3 的版本
### 执行命令
python -V  # 将会看到 python2 的版本

# 1.3
### 设置 pip3 名称
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
### 执行命令
pip3 -V  # 将会看到 pip3 的版本
### 更新 pip3
pip3 install --upgrade pip

# 1.4
### 利用宝塔面板的计划任务
### 在服务器的计划任务设置执行方法定时去运行 Python脚本

### 通过宝塔先上传我们要部署的项目文件
上传 ConnectMySQL压缩包，并解压
### 切换到需要部署目录
cd ConnectMySQL
### 安装依赖库 (有可能会有缺失的)
pip3 install -r requirements.txt
### 运行
python3 connectMySQL.py
