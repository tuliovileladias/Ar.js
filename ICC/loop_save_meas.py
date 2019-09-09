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

#POST MEDIDAS
headers = {
    "Content-Type": "application/json",
    "x-access-token":device_tokenGlobal
}
y1=0
y2=5
y3=10
while(True):
    data = json.dumps({
        "device1": y1,
        "device2": y2,
        "device3": y3
    })

    print(data)

    r = requests.post("https://smartcampus.inatel.br:4433/api/userapps/"+app_id_Global+"/devices/"+device_idGlobal+"/meas", headers=headers, data=data)
    resposta = ""
    y1 = y1+0.2
    y2 = y2+0.4
    y3 = y3-0.6
    if(y1>10):
        y1=0
    if(y2>10):
        y2=0
    if(y3<0):
        y3=10

