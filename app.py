from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']  # 获取文本框中的输入内容
        processed_text = process_input(input_text)  # 处理输入内容
        return render_template('index.html', result=processed_text)
    return render_template('index.html')

def process_input(searchword):
    # 在这里进行处理输入内容的逻辑
    processed_text = searchword

    if len(searchword) <= 3:
        processed_text = '''
please search with those key Parameters：

-p search poi Names
-i search poi Index details
-c search poi CategoryId
-d search road Names
-a search admin Names
-r reverse words
'''
        return processed_text


    if searchword[:3] == '-d ':
        #df = pd.read_csv('Israel_road_name.csv',index_col=0,dtype = pd.StringDtype())
        df = pd.read_pickle('Israel_road_name.pkl.bz2',compression='infer')
        df = df[df['STREET_NAME CHAR(400)'].str.contains(searchword[3:], na=False) | 
        df['STREET_NAME CHAR(1000)'].str.contains(searchword[3:],case=False,regex=False)]
        processed_text = df.to_string()

    if searchword[:3] == '-a ':
        #df = pd.read_csv('rdf_admin_struct_name_Israel.txt',index_col=0,dtype = pd.StringDtype())
        df = pd.read_pickle('rdf_admin_hierarchy.pkl.bz2',compression='infer')
        df = df[df['ADMIN_PLACE_NAME'].str.contains(searchword[3:],case=False,regex=False)]
        processed_text = df.to_string()

    if searchword[:3] == '-p ':
        #df = pd.read_csv('poi.csv',index_col=False,sep='\t',dtype = pd.StringDtype())
        df = pd.read_pickle('poi.pkl.bz2',compression='infer')
        df = df[df['Name'].str.contains(searchword[3:],case=False,regex=False)]
        df = df[['Name','CategoryId','CategoryName']]
        processed_text = df.to_string()

    if searchword[:3] == '-c ':
        #df = pd.read_csv('poi.csv',index_col=False,sep='\t',dtype = pd.StringDtype())
        df = pd.read_pickle('poi.pkl.bz2',compression='infer')
        df = df[df['CategoryId'].str.contains(searchword[3:],regex=False)]
        df = df[['Name','CategoryId','CategoryName']]
        processed_text = df.to_string()

    if searchword[:3] == '-i ':
        #df = pd.read_csv('poi.csv',index_col=False,sep='\t',dtype = pd.StringDtype())
        df = pd.read_pickle('poi.pkl.bz2',compression='infer')
        row = df.iloc[int(searchword[3:])]
        #df = df[df['Name'].str.contains(searchword[3:],case=False,regex=False)]
        processed_text = row.to_string()

    if searchword[:3] == '-r ':
        words = searchword[3:].split()
        words.reverse()
        processed_text = ' '.join(words)


    return processed_text

if __name__ == '__main__':
    app.run(debug=True,port=os.getenv("PORT", default=5050),host='0.0.0.0')
