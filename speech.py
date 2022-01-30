"""
Speech.py: tasks for SpeechHacks hackathon project
mostly done by Jimmy
"""

import requests
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
    #filename = "male.wav"
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
    #print(response.json())
    url = response.json()
    return url["upload_url"]


def uploadFileForTranscript(url):
    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = { "audio_url": url}
    headers = {
        "authorization": keys.authkey,
        "content-type": "application/json"
    }
    response = requests.post(endpoint, json=json, headers=headers)

    dictTest = response.json()

    print(dictTest)
    #print(response.json("id"))
    #os.system('pause')
    transcriptID = dictTest["id"]
    return transcriptID


def getTranscription(transcriptID):
    endpoint = "https://api.assemblyai.com/v2/transcript/" + transcriptID
    print(endpoint)
    headers = {
        "authorization": keys.authkey,
    }
    responsed = requests.get(endpoint, headers=headers)
    #print(responsed.json())
    responseDict = responsed.json()
    #print(responseDict['status'])

    while (responseDict['status'] == 'processing' or responseDict['status'] == 'queued'):
        #print('did this run')
        responsed = requests.get(endpoint, headers=headers)
        #print(responsed.json())
        responseDict = responsed.json()
        print(responseDict['status'])
    # print("   ")
    # print(responseDict)
    # print("    ")
    # print(responseDict['text'])
    return responseDict['text']


def countWords(stringg):
    dict = {}
    currentWord = ''

    for currentLetter in range(len(stringg)):
        if stringg[currentLetter].isalpha() or stringg[currentLetter] == "'":
            currentWord += stringg[currentLetter]
        else:
            if len(currentWord) > 0:
                "".join(currentWord)
                print(currentWord)
                if currentWord in dict:
                    dict[currentWord] += 1
                else:
                    dict[currentWord] = 1
                currentWord = ''
    if len(currentWord) > 0:
        "".join(currentWord)
        print(currentWord)
        if currentWord in dict:
            dict[currentWord] += 1
        else:
            dict[currentWord] = 1
            
    return dict   


if __name__ == "__main__":
    filename = youtubeConvert("https://www.youtube.com/watch?v=oP6x1Bd8t-Q")
    print(filename)
    script = fullTranscript(filename)
    print(script)
    countWords(script)