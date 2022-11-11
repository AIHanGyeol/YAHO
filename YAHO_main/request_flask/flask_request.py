from flask import Flask
from flask import request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from flask import render_template
import json
import requests
from vito import start , tokenns , file_STT
from base64 import b64decode , b64encode , encodebytes
import base64
from vito import start , tokenns , file_STT
# from models import Stores



app = Flask(__name__)

app.secret_key = "1234"
# app.config['UPLOAD_FOLDER'] = "C:/Users/HP/Desktop/meta/YAHO/flask/upload_folder"


@app.route('/upload')
def render_file():
    return render_template('upload.html')

## GET : 자료를 요청할 때 사용.
## POST : 자료를 생성을 요청할 때 사용.
## PUT : 자료의 수정을 요청할 때 사용.
## DELETE : 자료의 삭제를 요청할 때 사용.



#ver2,,insert queue
@app.route('/uploader' , methods = ['GET','POST'])
def uploader():        

    if request.method == 'POST':
        print('-' * 150)
        content_type = 'application/json'
        # content_type = 'multipart/form-data'
        headers = {'content-type': content_type, 'charset':'utf-8'}

        file = request.files['data']
        print(type(file))
        print(file)

        wav_file = b64encode(file.stream.read()).decode('utf-8')

        data = {"data":wav_file}
        data = json.dumps(data)

        # requests.post('http://127.0.0.3:5002/queue_res',data = data, headers=headers) #files = upload


        response = requests.post('http://127.0.0.2:5001/stt',data = data, headers=headers)
        
        if response.text == '0':
            result = ''
        else:
            result = response.text
            
        return result
    return 'connected!!'

if __name__ == '__main__':
    app.run(debug=True)

















##원래 flaks 임. ver1
# @app.route('/uploader' , methods = ['GET','POST'])
# def uploader():        

#     if request.method == 'POST':
#         print('-' * 150)
#         content_type = 'application/json'
#         # content_type = 'multipart/form-data'
#         headers = {'content-type': content_type, 'charset':'utf-8'}

#         file = request.files['data']
#         print(type(file))
#         print(file)


#         wav_file = b64encode(file.stream.read()).decode('utf-8')

#         data = {"data":wav_file}
#         data = json.dumps(data)


#         response = requests.post('http://127.0.0.2:5001/uploader',data = data, headers=headers) #files = upload
        
#         result = response.text
#         return result
#     return 'connected!!'

# if __name__ == '__main__':
#     app.run(debug=True)

