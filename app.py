from flask import Flask, render_template

# 创建一个 Flask 应用实例
app = Flask(__name__)

# 定义一个路由和视图函数
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# 当直接运行这个脚本时，启动开发服务器
if __name__ == '__main__':
    app.run(debug=True)