from flask import Flask , Response, request, render_template
from vito import start , tokenns , file_STT
import base64
from base64 import b64decode


app = Flask(__name__)

def signal():
    return 'twice'

#ver2,,insert queue
@app.route('/stt' , methods = ['GET','POST'])
def stt():
    if request.method == 'POST':

        datas = request.get_json()['data']

        datas = base64.b64decode(datas)
        print(type(datas))

        tokena = tokenns()
        result_text = start(datas, tokena)
        
        f = open("C:/Users/HP/Desktop/meta/YAHO/response_flask/response_text.txt" , 'a' , encoding='utf-8')
        f.write(str(result_text) + '\n')
        f.close()
        
        signal()
        

        return Response(response=result_text, status = 200, mimetype='application/json')
    return 'connected!!'

if __name__ == '__main__':
    app.run(host='127.0.0.2',debug=True , port=5001)






##ver1
# @app.route('/stt' , methods = ['GET','POST'])
# def stt():
#     if request.method == 'POST':

#         datas = request.get_json()['data']

#         datas = base64.b64decode(datas)
#         print(type(datas))

#         tokena = tokenns()
#         result_text = start(datas, tokena)


#         return Response(response=result_text, status = 200, mimetype='application/json')
#     return 'connected!!'

# if __name__ == '__main__':
#     app.run(host='127.0.0.2',debug=True , port=5001)