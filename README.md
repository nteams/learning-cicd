# learning-cicd
边学Python，边写CICD系统

## 技术栈
* Python 3.7.5
* Django 2.2.6

## 开发环境
### 工具
* Pycharm Community Edition
* virtualenv
### 启动
* 启动virtualenv虚拟环境
* 切换到外层的cicdsite目录，运行：
>* python manage.py runserver  (默认情况下，runserver 命令会将服务器设置为监听本机内部 IP 的 8000 端口。)
>* python manage.py runserver 8080  (如果你想更换服务器的监听端口，请使用命令行参数。举个例子，下面的命令会使服务器监听 8080 端口)
>* python manage.py runserver 0:8000  (如果你想要修改服务器监听的IP，在端口之前输入新的。比如，为了监听所有服务器的公开IP（这你运行 Vagrant 或想要向网络上的其它电脑展示你的成果时很有用）,0 是 0.0.0.0 的简写)

## 创建一个管理员账号
* python manage.py createsuperuser    admin/123456
* python manage.py runserver
* http://127.0.0.1:8000/admin/


