from flask import Flask, render_template, redirect, url_for
from flask import request
import requests, json

app = Flask(__name__)

# 重定向
@app.route('/')
def index():
    return redirect(url_for('Person'))

@app.route("/Meta", methods = ['GET'])
def Origin():
    # 获取 IP ---> 决定中英文页面
    # 默认英文展示
    ip = request.remote_addr
    Language = "EN"
    # response = requests.get("http://ip-api.com/json/" + ip).text
    # response = json.loads(response) # 将网页的 json 格式的字符串数据转成字典
    # print(response)
    return render_template("Meta.html", Language = Language)

@app.route("/Person", methods = ['GET'])
def Person():
    # 获取 IP ---> 决定中英文页面
    # 默认英文展示
    ip = request.remote_addr
    Language = "EN"
    # response = requests.get("http://ip-api.com/json/" + ip).text
    # response = json.loads(response) # 将网页的 json 格式的字符串数据转成字典
    # print(response)
    return render_template("Person/Person.html", Language = Language)


# Ajax 请求
@app.route("/test", methods=["GET", "POST"])
# 前端请求该地址
def test():
    # 获取请求参数                                                   
    requestArgs = request.values
    print(requestArgs)
    # request.values.get("key") 获取所有参数
    # 获取请求方法 request.method
    #不存在时返回None
    num = requestArgs.get("num")
    print("num")
    return num

if __name__ =="__main__":
    app.run(debug = True)