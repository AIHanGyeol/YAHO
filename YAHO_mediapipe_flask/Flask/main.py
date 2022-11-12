import model_ as md
from flask import Flask , Response
from flask import request
from flask import render_template
import requests
import json
import one_graph as og
import summarize
import jsonpickle


## GET : 자료를 요청할 때 사용.
## POST : 자료를 생성을 요청할 때 사용.
## PUT : 자료의 수정을 요청할 때 사용.
## DELETE : 자료의 삭제를 요청할 때 사용.


app = Flask(__name__)


model_name = 'alaggung/bart-r3f'
# model_name = 'ainize/kobart-news'

summarizer = summarize.summarize(model_name , model_name )

@app.route('/', methods=['POST'])
def render_file():
    if request.method == 'POST': 
        try:
            # print(request.form)
            datas = request.get_json()
            # date = datas['date']

            pe_count = {}

            for i in datas:
                if i['name'] not in pe_count.keys():
                    pe_count[i['name']] = 1
                else:
                    pe_count[i['name']] += 1 
                    

            print(pe_count)               

            og.one_graph(pe_count.values() , pe_count.keys())

            return '연결성공'
            
        except Exception as e:
            print(e)
            return '연결실패'


        return '연결성공'#Response(response=response , status = 200 , mimetype='application/json')
    return 'haha' 


# #ver2,,insert queue
# @app.route('/uploader')
# def uploader():        
#     response = requests.post()
#     return 'connected!!'
    

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0' , port = 9090)

