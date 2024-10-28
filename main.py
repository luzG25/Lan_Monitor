from time import sleep

from scan import scanLan
from handle_data import criarArq, saveData, obterDados

configs = obterDados('configs.json')

criarArq(configs['dirData'])

ip = '192.168.1'

while True:
    content = {}
    scanLan(ip, configs['ip_pool'], content, configs)
    saveData(content, configs, 5)
    sleep(configs['timer'] * 60)
