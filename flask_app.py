
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath
import pandas as pd
import json

app = Flask(__name__)

# load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        print("STD POST")


    return  render_template('index.html', name=SECRET_KEY)

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        result = []
        data = request.get_json()
        sku=data['sku']
        for ind,row in df.iterrows():
            #update SKU Statement
            print(row[data['date']],row[data['store']],row[data['sku']],row[data['qty']])

        return("Uploaded!")


@app.route('/process_result', methods=['POST', 'GET'])
def process_result():
    if request.method == "POST":
        file = request.files['file']
        print(file.name)
        global df
        df = pd.DataFrame(pd.read_csv(file))
        html=''
        error=''
        html += '<table class="table table-bordered"><tr>'
        # get comumn nuber and name from env file
        i = os.getenv("NO_OF_COL")
        opt = ''
        colname = 'COL_NAME_'
        for number in range(i):
            colname = 'COL_NAME_'+number
            opt+= '<option value="'+os.getenv(colname)+'">'+os.getenv(colname)+'"</option>'

        for column in df:
            html += '<th><select name="set_column_data" class="form-control set_column_data" data-column_number="'+column+'"><option value="">Set Count Data</option>'+opt+'</select></th>'
        html += '</tr>'
        limit = 0
        for ind in df.index:
            limit = limit+1
            if(limit <7):
                html += '<tr>'
                for indc in df:
                    html += '<td>'+str(df[indc][ind])+'</td>'
                    # print(df[indc][ind])
                html += '</tr>'
        html += '</table><br /><div align="right"><button type="button" name="import" id="import" class="btn btn-success" disabled>Import</button></div><br />'

        # print(html)
        return html, 201
        # return(data.to_json("data.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None))


