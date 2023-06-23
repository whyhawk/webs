from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']  # 获取文本框中的输入内容
        processed_text = process_input(input_text)  # 处理输入内容
        return render_template('index.html', result=processed_text)
    return render_template('index.html')

def process_input(input_text):
    # 在这里进行处理输入内容的逻辑
    processed_text = input_text
    return processed_text

if __name__ == '__main__':
    app.run(debug=True,port=os.getenv("PORT", default=5000),host='0.0.0.0')
