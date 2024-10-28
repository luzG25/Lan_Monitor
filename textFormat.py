def centralizar(fraze, espaco):
    spc = espaco - len(fraze)
    spc = int(spc/2) 
    return ' ' * spc + fraze


def Centralizar(frazes, espaco, equal=False):
    #frazes[]
    #espaço[]
    comp = len(frazes)
    out = ''
    if equal:
        spc = int(espaco / comp) 
        for fras in frazes:
            comp1 = len(fras)
            num = spc - comp1
            while num < 0:
                comp1 -= 1
                num = spc - comp1
            
            num = int(num / 2)
            out += ' '*num + fras[:comp1] + ' '*num

        return out 

    if len(espaco) != comp:
        return 'error: espaço diferente de frazes'

    for c in range(0, comp):
        fras = frazes[c]
        spc = espaco[c]

        comp1 = len(fras)
        num = spc - comp1
        
        while num < 0:
            comp1 -= 1
            num = spc - comp1 
         
        while True:
            num = int(num/2)
            out1 = ' '*num + fras[:comp1] + ' '*num

            if len(out1) > spc:
                comp1 -= 1
                num = spc - comp1

            else:
                break 

        out += out1

    return out

def timeStyle(data, style= '/', mod='dd/mm/aaaa'):
    #data[]
    if mod == 'dd/mm/aaaa hr:mn':
        if len(data) == 9:
            return f'{data[2]:02d}{style}{data[1]:02d}{style}{data[0]:04d}  {data[3]:02d}:{data[4]:02d}'
            
        else:
            #data[dd, mm, aaaa, hr, mn]
            return f'{data[0]:02d}{style}{data[1]:02d}{style}{data[2]:04d}  {data[3]:02d}:{data[4]:02d}'

    elif mod == 'dd/mm/aa':
        if len(data) == 9:
            return f'{data[2]:02d}{style}{data[1]:02d}{style}{data[0]:04d}'

        else:
            #data[dd, mm, aaaa, hr, mn]
            return f'{data[0]:02d}{style}{data[1]:02d}{style}{data[2]:04d}'


