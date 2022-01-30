"""
Speech.py: tasks for SpeechHacks hackathon project
Authors: Jimmy Lu, Liam Seagram
"""

import requests, os, sys
from vault import keys
import ytmp3 as con


def youtubeConvert(link):
    return con.download_video(link)


def fullTranscript(filename):
    url = uploadLocalTranscript(filename)
    fileID = uploadFileForTranscript(url)
    return getTranscription(fileID)


def onlineTransfer(url):
    fileID = uploadFileForTranscript(url)
    return getTranscription(fileID)


def uploadLocalTranscript(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data
    headers = {'authorization': keys.authkey} 
    response = requests.post('https://api.assemblyai.com/v2/upload',
                            headers=headers,
                            data=read_file(filename))
    url = response.json()
    os.remove(filename)
    return url["upload_url"]


def uploadFileForTranscript(url):
    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = { 
        "audio_url": url
        }
    headers = {
        "authorization": keys.authkey,
        "content-type": "application/json"
    }
    response = requests.post(endpoint, json=json, headers=headers)

    dictTest = response.json()

    # print(dictTest)
    # print(response.json("id"))
    # os.system('pause')
    transcriptID = dictTest["id"]
    return transcriptID


def getTranscription(transcriptID):
    endpoint = "https://api.assemblyai.com/v2/transcript/" + transcriptID
    headers = {
        "authorization": keys.authkey
    }
    responsed = requests.get(endpoint, headers=headers)
    responseDict = responsed.json()
    # print(responseDict['status'])
    while (responseDict['status'] == 'processing' or responseDict['status'] == 'queued'):
        responsed = requests.get(endpoint, headers=headers)
        responseDict = responsed.json()
        # print(responseDict['status'])
    # print(responseDict)
    # print(responseDict['text'])
    # print responseDict['iab_categories_result']
    return (responseDict['text'])


def main():
    if len(sys.argv) != 2:
        print("Usage: speech.py [YouTube link]")
        exit(1)
    filename = youtubeConvert(sys.argv[1])
    script = fullTranscript(filename)
    print(script)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
