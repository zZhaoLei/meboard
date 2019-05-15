# meboard
meboard

# 启动
## 安装相关环境
本项目在Python 3.7下开发，对于Python 2等可能会有写不兼容。

### 安装Flask
安装requirements.txt中的依赖包
`pip install -r requirements.txt`

### 启动flask项目
进入项目的meboard根目录，使用`flask run`启动项目，默认时`development`模式, 可自行修改`meboard/.flaskenv`中的`FLASK_ENV`变量值为`production`。

`注意`：请勿在`生产环境`使用`开发服务器`，请改用`WSGI`生产服务器。
