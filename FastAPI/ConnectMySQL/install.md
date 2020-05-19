<!--
 * @Author: _zone
 * @Date: 2020-05-18 14:20:54
 * @LastEditTime: 2020-05-19 10:00:10
 * @FilePath: /ConnectMySQL/install.md
--> 

# 本篇以安装 Python-3.6.8 版本的 Python依赖库举例


# 1.0
# 设置基础环境配置
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make

# 1.1
# 下载
wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tar.xz
# 解压
tar -xvJf  Python-3.6.8.tar.xz
# 切换路径
cd Python-3.6.8
# 安装
./configure prefix=/usr/local/python3
make && make install

# 1.2
# 设置 Python3 名称
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
# 执行命令
python3 -V  # 将会看到 python3 的版本
# 执行命令
python -V  # 将会看到 python2 的版本

# 1.3
# 设置 pip3 名称
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
# 执行命令
pip3 -V  # 将会看到 pip3 的版本
# 更新 pip3
pip3 install --upgrade pip

# 利用宝塔面板的计划任务
# 在服务器的计划任务设置执行方法定时去运行 Python脚本
