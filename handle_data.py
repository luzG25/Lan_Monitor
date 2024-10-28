from json import dump, load
from os import listdir
from time import localtime
from textFormat import Centralizar, centralizar, timeStyle

def obterDados(dir):
    file = open(dir, "r", encoding='utf-8')
    data = load(file)
    file.close()

    return data

def saveDados(dados, dir):
    file = open(dir, 'w')
    dump(dados, file)
    file.close()

def criarArq(dir):
    dir = dir.split("/")
    Dir = ''
    d = len(dir)
    for c in range(0, d-1):
       Dir +=  dir[c] + "/"

    name = dir[d-1]
    #print(name, " ", Dir)

    if name not in listdir(Dir):
        file = open(Dir + "/" + name, 'w')
        d = { }
        dump(d, file)
        file.close()

def showRes(dados, config):
    def convMinutosHora(min):
        return f'{int(min/60):03d} Horas'
    file = open(config['dirShow'], 'w')

    file.writelines(centralizar("DISPOSITIVOS CONECTADOS AGORA", 80))
    file.writelines('\n')
      
    # nome do dis.    mac     ip     timeconnected
    spc = [25, 20, 20, 15]
    frs = ['Dispositivo', 'Mac Adress', 'Endereço IP', 'Tempo Conectado']
    file.writelines(f' {Centralizar(frs, spc)}')

    for disp in dados.keys():
        if dados[disp]['online']:
            file.writelines('\n') 
            dado = dados[disp]
            # tab ... 25 nome ...tab ... 20 mac ... tab... 15 ip... tab ... 15timeconected
            
            frs = [dado['nome'], dado['mac'], dado['ip'], convMinutosHora(dado['timeconected'])]
            file.writelines(f'-{Centralizar(frs, spc)}')

    file.writelines('\n')
    file.writelines('-' * 100)

    #TODOS DISPOSITIVOS
    file.writelines('\n\n')
    file.writelines(centralizar("TODOS DISPOSITIVOS", 100))
    file.writelines('\n')
    
    # nome do dis.    mac     ip     online    lasttimeconected   timeconected
    spc = [25, 20, 15, 10, 20, 10]
    frs = ['Dispositivo', 'Mac Adress', 'Endereço IP', 'Estado', 'Ultima conexão', 'Tempo Conectado']
    file.writelines(f' {Centralizar(frs, spc)}')

    for disp in dados.keys():
        dado = dados[disp]
        file.writelines('\n')

        if dado['online']:
            online = 'Online'
        else:
            online = 'Offline'


        # 25nome do dis.    20mac     15ip     10online    20lasttimeconected   10timeconected
        spc = [25, 20, 15, 10, 20, 10]
        frs = [dado['nome'], dado['mac'], dado['ip'], online, timeStyle(dado['lasttime'], '/', 'dd/mm/aaaa hr:mn') , convMinutosHora(dado['timeconected'])]
        file.writelines(f'-{Centralizar(frs, spc)}')        



def saveData(cont, configs, timer):
    # cont = {"mac": "nome":, "ip":}
    
    dados = obterDados(configs["dirData"])
    #dados = {"mac": {nome, ip, online, lastime, timeconected}}

    ks = dados.keys()
    for c in cont.keys():
        if c in ks:
            dados[c]['ip'] =  cont[c]['ip']
            if '*' not in dados[c]['nome']:
                dados[c]['nome'] = cont[c]['nome']

            dados[c]['online'] =  True
            dados[c]['lasttime'] = localtime()
            
            dados[c]['timeconected'] += timer

        else:
            dados[c] = {}
            
            dados[c]['nome'] = cont[c]['nome']

            dados[c]['ip'] =  cont[c]['ip']
            dados[c]['mac'] = c

            dados[c]['online'] =  True
            dados[c]['lasttime'] = localtime()
            dados[c]['timeconected'] = timer

    for c in ks:
        if c not in cont.keys():
            dados[c]["online"] = False

    saveDados(dados, configs["dirData"])
    showRes(dados, configs)
    print('\nDADOS GUARDADOS COM SUCESSO!\n')
    