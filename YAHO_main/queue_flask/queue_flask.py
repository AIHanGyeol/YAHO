from flask import Flask , Response , request
import requests
import json




app = Flask(__name__)

queues = []


#queue pop
def queue_pop():
    try:
        data = queues.pop(0)
    except:
        data = 'end'
    return data


@app.route('/queue_res' , methods = ['GET' , 'POST'])
def queue_res():
    if request.method == 'POST':
        datas = request.get_json()['data']
        queues.append(datas)
        
    if len(queues) > 0:
        result = queue()
        return result
    return '0'


def queue():

    content_type = 'application/json'
    headers = {'content-type': content_type, 'charset':'utf-8'}

    data = {"data":queue_pop()}
    data = json.dumps(data)  ##python 객체를 json문자열로 변환.
    result_text = requests.post('http://127.0.0.2:5001/stt',data = data, headers=headers)
    
    return Response(response=result_text, status = 200, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='127.0.0.3' , port = 5002 , debug= True)







#mark2
# @app.route('/queue_res' , methods = ['GET' , 'POST'])
# def queue_res():
#     if request.method == 'POST':
#         datas = request.get_json()['data']
#         queues.append(datas)

        


# @app.route('/queue' , methods = ['GET' , 'POST'])
# def queue():
#     if request.method == 'POST':
#         content_type = 'application/json'
#         headers = {'content-type': content_type, 'charset':'utf-8'}

#         # datas = request.get_json()['data']
#         # queues.append(datas)
#         # print(len(queues))

#         data = {"data":queues[0]}
#         data = json.dumps(data)  ##python 객체를 json문자열로 변환.
        
#         result_text = requests.post('http://127.0.0.2:5001/stt',data = data, headers=headers)
        



#         return Response(response=result_text, status = 200, mimetype='application/json')





# if __name__ == '__main__':
#     app.run(host='127.0.0.3' , port = 5002 , debug= True)