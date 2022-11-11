import requests
import json
import time


def tokenns():
    Client_ID = '8ncsfbR6c_4LfK6No2EL'
    Client_secret = 'ax0woUWHmrw14_X--QIP98nkHeeZParrKfN7SGJW'
    resp = requests.post(
        'https://openapi.vito.ai/v1/authenticate',
        data={'client_id': Client_ID,
            'client_secret': Client_secret}
    )

    resp.raise_for_status()
    print(resp.json())

    tokenn = resp.json()['access_token']
    return tokenn
    

def file_STT(file_path , tokenn):
    config = {
        "diarization": {
            "use_verification": False
        },
        "use_multi_channel": False
    }
    resp = requests.post(
    'https://openapi.vito.ai/v1/transcribe',
    headers={'Authorization': 'bearer '+tokenn},
    data={'config': json.dumps(config)},
    files={'file': file_path}
    )

    resp.raise_for_status()
    print(resp.json())

    transcribe_id = resp.json()['id']
    print(transcribe_id)
    return transcribe_id

def Gett(transcribe_id , tokenn):
    resp = requests.get(
    'https://openapi.vito.ai/v1/transcribe/'+transcribe_id,
    headers={'Authorization': 'bearer '+ tokenn},
    )
    resp.raise_for_status()
    # print(resp.json())

    try:
        result = resp.json()['results']['utterances'][0]['msg']
    except:
        result = 'sleep 좀 더줘라.'
    return result


def start(file_path, token):
    tokenn = token
    # time.sleep(6)
    transcribe_id = file_STT(file_path , tokenn)
    time.sleep(6)

    result = Gett(transcribe_id , tokenn)

    return result


