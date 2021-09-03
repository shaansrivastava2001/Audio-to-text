#pip install ibm_watson wget

from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_s2t = "https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/71bfe551-7a05-4e81-9e6d-973c80a0ff4d"
iam_apikey_s2t = "oHaWyZbPJnc3CCiMykHvCVI0kwpvTcgdVbelhw8FFoNx"

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
#s2t

filename = "C:/Users/admin/Desktop/python-projects/speech-to-text/regression.mp3"
with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')
    #response.result

from pandas import json_normalize

json_normalize(response.result['results'],"alternatives")

#response

recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
#type(recognized_text)

#recognized_text

print("Recognised text from the audio:\n")
print(recognized_text)