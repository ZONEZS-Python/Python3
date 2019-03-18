# Mac 下启动MySQL 服务器

```bash
// 1、查看MySQL的路径位置（which mysql）
(base) zonezs-macbook-pro:~ _zone$ which mysql
/usr/local/opt/mysql@5.7/bin/mysql  // 这里是我的MySQL 安装路径位置

// 2、启动MySQL 服务器（mysql.server start）
(base) zonezs-macbook-pro:~ _zone$ sudo /usr/local/opt/mysql@5.7/bin/mysql.server start
Password:  // 电脑本机密码
Starting MySQL
 SUCCESS! 
(base) zonezs-macbook-pro:~ _zone$ 2019-03-18T07:50:07.6NZ mysqld_safe A mysqld process already exists

// 备注：mysqld_safe A mysqld process already exists
// 这个问题一直没有搞清楚，通过网上的资料反反复复折腾了大半天都没有处理好，但是不影响MySQL的正常使用，后面有时间了在来看这个问题

// 3、停止MySQL 服务器（mysql.server stop）
(base) zonezs-macbook-pro:~ _zone$ sudo /usr/local/opt/mysql@5.7/bin/mysql.server stop
Shutting down MySQL
.. SUCCESS! 
(base) zonezs-macbook-pro:~ _zone$ 

// 4、重启MySQL 服务器（mysql.server restart）(重启是针对在启动过后的情况下)
(base) zonezs-macbook-pro:~ _zone$ sudo /usr/local/opt/mysql@5.7/bin/mysql.server restart
Shutting down MySQL
.. SUCCESS! 
Starting MySQL
.2019-03-18T07:54:43.6NZ mysqld_safe A mysqld process already exists
 SUCCESS! 
(base) zonezs-macbook-pro:~ _zone$ 
```
> // 上面的2、3、4命令也可以简化为这样：
> 通过1、查看MySQL的路径后：which mysql
> 得到路径：/usr/local/opt/mysql@5.7/bin

```bash
(base) zonezs-macbook-pro:~ _zone$ cd /usr/local/opt/mysql@5.7/bin  // 进入到MySQL目录中

(base) zonezs-macbook-pro:bin _zone$ sudo mysql.server start  // 启动

(base) zonezs-macbook-pro:bin _zone$ sudo mysql.server stop  // 停止

(base) zonezs-macbook-pro:bin _zone$ sudo mysql.server restart  // 重启
```

