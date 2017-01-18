import requests

#payload = {'drum': 'bob', 'email': 'bob@bob.com'}
#requests.put("http://127.0.0.1:5000/", data=payload)

requests.put("http://127.0.0.1:5000/",data = '{"drum": "./drums/StarCraft_Sound_Pack/Zerg/Units/Advisor/zaderr02.wav"}',headers={'content-type':'text/json'})
requests.put("http://127.0.0.1:5000/",data = '{"drum": "./drums/StarCraft_Sound_Pack/Zerg/Units/Advisor/hamster.wav"}',headers={'content-type':'text/json'})



