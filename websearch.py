import web

render = web.template.render('templates/')  # 设置模板文件夹路径

urls = (
    '/', 'Index',
)

class Index:
    def GET(self):
        return render.index(result=None)

    def POST(self):
        input_text = web.input().text  # 获取表单数据内容
        return render.index(result=input_text)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
