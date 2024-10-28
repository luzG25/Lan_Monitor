import subprocess

def cmd_handler(cmd):
    result = subprocess.run( cmd, stdout=subprocess.PIPE)
    return result.stdout.decode()

def scan_ip(ip, lista, config):
    cmd = ['arp', '-g', ip]
    msg = cmd_handler(cmd)
    #print(msg)
    if (msg.strip() == 'No ARP Entries Found.'):
        return 0

    else:
        # obter endereço mac
        msg = msg.split()
        mac = msg[10]

        # obter nome
        cmd = ['ping', '-n', str(config['tents']), '-a', ip]
        msg = cmd_handler(cmd).split()
        name = msg[1]

        #analizar mac

        #guardar no dicionario pelo endereço Mac
        lista[mac] = {'nome': name, 'ip': ip}        

    

def scanLan(ip, ip_pool, lista, config):
    for c in range(ip_pool[0], ip_pool[1]):
        scan_ip(f'{ip}.{c}', lista, config)
        

