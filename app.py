from flask import Flask

# 创建一个 Flask 应用实例
app = Flask(__name__)

# 定义一个路由和视图函数
@app.route('/')
def hello_world():
    return 'Hello, World!'

# 当直接运行这个脚本时，启动开发服务器
if __name__ == '__main__':
    app.run(debug=True)