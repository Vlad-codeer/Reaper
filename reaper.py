#<---------------------------->
import os
from alive_progress import alive_bar
from time import sleep
import json
import requests
import urllib.request
from colored import fg, bg, attr
#<---------------------------->

#<---------------------------->
print('''
%s
              ...                            
             ;::::;                           
           ;::::; :;                          
         ;:::::'   :;                         
        ;:::::;     ;.                        
       ,:::::'       ;           OOO\         
       ::::::;       ;          OOOOO\        
       ;:::::;       ;         OOOOOOOO       
      ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`. ,,,;.        /  / DOOOOOO    
  .';:::::::::::::::::;,     /  /     DOOOO   
 ,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:#                  
   ::::::`:::::;'  /  /   `#              
%s
''' % (fg(57), attr(0)))

sleep(1)
print('%s>>>%s Carregando ferramentas...' % (fg(1), attr(0)))
print(' ')

for x in 100, 100, 100:
   with alive_bar(theme='classic') as bar:
       for i in range(100):
           sleep(.005)
           bar()

os.system(['clear', 'cls'][os.name == 'nt'])
#<---------------------------->

#<---------------------------->
def reaper_logo():
    sleep(1)
    print('''
%s
 ______     ______     ______     ______   ______     ______    
/\  == \   /\  ___\   /\  __ \   /\  == \ /\  ___\   /\  == \   
\ \  __<   \ \  __\   \ \  __ \  \ \  _-/ \ \  __\   \ \  __<   
 \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_\    \ \_____\  \ \_\ \_\ 
  \/_/ /_/   \/_____/   \/_/\/_/   \/_/     \/_____/   \/_/ /_/ 

>>> https://github.com/zCodaxy                                                               
%s

Não sei por que o ser humano se esforça para entender o outro. Lembre-se,
as pessoas são incapazes de se entender completamente. O ser humano é 
um animal triste.
''' % (fg(57), attr(0)))

def reaper_menu():
    print('''
╭──── %sCONSULTAS%s
├ 1 » Consultar ip
├ 2 » Consultar cep
├ 3 » Consultar cnpj
╰ 4 » Consultar ddd
''' % (fg(57), attr(0)))
    hint = int(input('''Qual função deseja utilizar? 
%s>>>%s ''' % (fg(57), attr(0))))
    if hint == 1:
        reaper_ip()
    if hint == 2:
        reaper_cep() 
    if hint == 3:
        reaper_cnpj()
    if hint == 4:
        reaper_ddd() 
    if hint != 1 and 2 and 3 and 4:
        print(' ')
        sleep(1)
        print('%sFunção desconhecida!%s' % (fg(1), attr(0)))
        print(' ')
        reaper_return()

def reaper_return():
    voltar = input('''Deseja voltar ao menu? (sim/nao)
%s>>>%s ''' % (fg(57), attr(0)))
    if voltar == 'sim':
        sleep(1)
        os.system(['clear', 'cls'][os.name == 'nt'])
        reaper_logo()
        reaper_menu()
    if voltar == 'nao':
        os.system(['clear', 'cls'][os.name == 'nt'])
        sleep(1)
        exit()
    if voltar != 'sim' and 'nao':
        print(' ')
        sleep(1)
        print('%sNão entendi! Utilize apenas (sim/nao)%s' % (fg(1), attr(0)))
        print(' ')
        reaper_return()

def reaper_ip():
    os.system(['clear', 'cls'][os.name == 'nt'])
    sleep(1)
    print('''
%s
             ___          
            /   \\        
       /\\ | . . \\       
     ////\\|     ||       
   ////   \\ ___//\       
  ///      \\      \      
 ///       |\\      |     
//         | \\  \   \    
/          |  \\  \   \   
           |   \\ /   /   
           |    \/   /    
           |     \\/|     
           |      \\|     
           |       \\     
           |        |     
           |_________\    
%s
''' % (fg(57), attr(0)))
    print(' ')
    ip = input('''Insira o ip: 
%s>>>%s ''' % (fg(57), attr(0)))
    with urllib.request.urlopen('http://ip-api.com/json/{}' .format(ip)) as url:
        data = json.loads(url.read().decode())
    print(' ')
    print(f'%s{data}%s' % (fg(1), attr(0)))
    print(' ')
    reaper_return()

def reaper_cep():
    os.system(['clear', 'cls'][os.name == 'nt'])
    sleep(1)
    print('''
%s
             ___          
            /   \\        
       /\\ | . . \\       
     ////\\|     ||       
   ////   \\ ___//\       
  ///      \\      \      
 ///       |\\      |     
//         | \\  \   \    
/          |  \\  \   \   
           |   \\ /   /   
           |    \/   /    
           |     \\/|     
           |      \\|     
           |       \\     
           |        |     
           |_________\    
%s
''' % (fg(57), attr(0)))
    print(' ')
    cep = input('''Insira o cep: 
%s>>>%s ''' % (fg(57), attr(0)))
    with urllib.request.urlopen('https://viacep.com.br/ws/{}/json' .format(cep)) as url:
        data = json.loads(url.read().decode())
    print(' ')
    print(f'%s{data}%s' % (fg(1), attr(0)))
    print(' ')
    reaper_return()

def reaper_cnpj():
    os.system(['clear', 'cls'][os.name == 'nt'])
    sleep(1)
    print('''
%s
             ___          
            /   \\        
       /\\ | . . \\       
     ////\\|     ||       
   ////   \\ ___//\       
  ///      \\      \      
 ///       |\\      |     
//         | \\  \   \    
/          |  \\  \   \   
           |   \\ /   /   
           |    \/   /    
           |     \\/|     
           |      \\|     
           |       \\     
           |        |     
           |_________\    
%s
''' % (fg(57), attr(0)))
    print(' ')
    cnpj = input('''Insira o cnpj: 
%s>>>%s ''' % (fg(57), attr(0)))
    with urllib.request.urlopen('https://api-publica.speedio.com.br/buscarcnpj?cnpj={}' .format(cnpj)) as url:
        data = json.loads(url.read().decode())
    print(' ')
    print(f'%s{data}%s' % (fg(1), attr(0)))
    print(' ')
    reaper_return()

def reaper_ddd():
    os.system(['clear', 'cls'][os.name == 'nt'])
    sleep(1)
    print('''
%s
             ___          
            /   \\        
       /\\ | . . \\       
     ////\\|     ||       
   ////   \\ ___//\       
  ///      \\      \      
 ///       |\\      |     
//         | \\  \   \    
/          |  \\  \   \   
           |   \\ /   /   
           |    \/   /    
           |     \\/|     
           |      \\|     
           |       \\     
           |        |     
           |_________\    
%s
''' % (fg(57), attr(0)))
    print(' ')
    ddd = input('''Insira o ddd: 
%s>>>%s ''' % (fg(57), attr(0)))
    r = requests.get('https://brasilapi.com.br/api/ddd/v1/{}' .format(ddd))
    data = r.json()
    print(' ')
    print(f'%s{data}%s' % (fg(1), attr(0)))
    print(' ')
    reaper_return()
#<---------------------------->

#<---------------------------->
reaper_logo()
reaper_menu()  
#<---------------------------->
