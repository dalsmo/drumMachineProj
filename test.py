import requests

#payload = {'drum': 'bob', 'email': 'bob@bob.com'}
#requests.put("http://127.0.0.1:5000/", data=payload)

requests.put("http://127.0.0.1:5000/",data = '{"drum": "./drums/AgeOfEmpires/30 Wololo.mp3"}',headers={'content-type':'text/json'})



