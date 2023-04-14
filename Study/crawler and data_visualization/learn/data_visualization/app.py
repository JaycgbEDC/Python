from flask import Flask, render_template, request
import settings
import datetime


app = Flask(__name__)  # Flask是一个类，里面的参数表示本文件的名称app
app.config.from_object(settings)  # 可以打印app.config会显示他的配置信息，里面的参数是将本项目的setting.py中的内容更新到原有配置

@app.route('/')  # 路由
def hello_world():  # 在此路由下的视图（函数）
    return 'Hello World!'


# 给路由传参
@app.route('/<name>')  # 路由
def welcom_name(name):
    return f'Hello {name}!'


# 路由传递的参数默认当做string处理，这里指定int，尖括号中冒号后面的内容是动态的（注意冒号后面不能有空格）
@app.route('/<int:id>')  # 路由
def welcom_id(id):
    return f'Hello {id} 号会员!'


# 渲染模板
@app.route('/tem')  # 路由
def welcom_tem():
    return render_template('index.html')


# 向页面传递变量
@app.route('/tem/var')  # 路由
def welcom_tem_param():
    date = datetime.date.today()
    l = ['mike', 'jim', 'kribe']
    task = {'工作内容':'编程', '时间':'2小时'}
    return render_template('index.html', var = date, l = l, task = task)


# 表单提交
@app.route('/tem/post')  # 路由
def welcom_tem_post():
    return render_template('register.html')


# 接收表单提交的路由，需要指定methods为post
@app.route('/tem/result', methods = ['POST', 'GET'])  # 路由
def welcom_tem_result():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', result = result)


if __name__ == '__main__':
    app.run(host = '127.0.0.2', port = 3)  # # 启动flask内部服务器，主机地址和端口号可自定义