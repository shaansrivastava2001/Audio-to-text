# Audio-to-text
The project requires SpeechToTextV1 object of ibm_watson module. It is actually a Cloud Service of IBM Cloud.
First we have to provide the unique URL and an API key and then pass the key to IAMAuthenticator function.
Then we have to specify the filename with its path which has to be audio file.
Then we use following command and assign it to a variable s2t.recognize(audio=wav, content_type='audio/mp3')
Then using json normalize we use .result method to get the result of the audio conversion.
To access the exact converted text: response.result['results'][0]["alternatives"][0]["transcript"]
