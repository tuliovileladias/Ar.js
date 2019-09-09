# _*_ coding: utf-8 _*_

__author__ = "Tulio Dias"
__copyright__ = "Copyright 2019, Inatel Competence Center"
__credits__ = "Inatel"
__license__ = "MIT"
__maintainer__ = "Tulio Dias"
__email__ = "tuliodias@inatel.br"

import json
import requests
import time

email = "tuliodias@inatel.br" #ALTERAR
password = "tulio@Tulio" #ALTERAR

local_host = "https://smartcampus.inatel.br:4433" #ALETRAR
app_id_local = "5d70f8c153b2d6003024a0a6" #ALTERAR
device_ids = ["5d70fa5d53b2d6003024a0a9","",""] #ALTERAR
device_tokens = ["","",""] #MANTER

app_id_Global = "5d70f8c153b2d6003024a0a6" #MANTER
device_idGlobal = "5d70fa5d53b2d6003024a0a9" #MANTER
device_tokenGlobal = "I04vFjj-q3ori3HYHZHcJifP" #MANTER

time.sleep(20)

data = json.dumps({
    "email": email,
    "password": password
})

headers = {
    "Content-Type": "application/json",
    "x-access-token":""
}

r = requests.post(local_host+"/api/user/login", headers=headers, data=data)
resposta = ""
try:
    resposta = r.json()
except:
    print("Erro na requisição")

if("token" in resposta):
    device_tokens = [str(resposta["token"]),str(resposta["token"]),str(resposta["token"])]

device_meas = [0,0,0]

device_meas = [0,0,0]
i_index =0
for device_id in device_ids:
    headers = {
        "Content-Type": "application/json",
        "x-access-token": str(device_tokens[i_index])
    }
    r = requests.get(local_host+"/api/userapps/"+str(app_id_local)+"/devices/"+str(device_id), headers=headers)
    resposta = ""
    try:
        resposta = r.json()
    except:
        print("Erro na requisição")
    print(resposta)
    i_index = i_index+1
    if("meas" in resposta):
        if("consumo" in resposta["meas"]):
            device_meas[i_index]= int(resposta["meas"]["consumo"])

#POST MEDIDAS
headers = {
    "Content-Type": "application/json",
    "x-access-token":device_tokenGlobal
}

data = json.dumps({
    "device1": device_meas[0],
    "device2": device_meas[1],
    "device3": device_meas[2]
})

print(data)

r = requests.post("https://smartcampus.inatel.br:4433/api/userapps/"+app_id_Global+"/devices/"+device_idGlobal+"/meas", headers=headers, data=data)
resposta = ""
