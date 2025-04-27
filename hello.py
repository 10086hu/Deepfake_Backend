from flask import Flask

#创建应用程序实例
app = Flask(__name__)

#定义路由和视图函数
@app.route('/')
def hello():
    return 'Hello Deepfake!'


if __name__ == '__main__':
    app.run()