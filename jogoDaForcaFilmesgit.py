# -*- encoding: utf-8 -*-
import random
import time
import tmdbsimple as tmdb
tmdb.API_KEY = 'SUA SENHA DA API AQUI'
import pygame
from pygame import mixer
from unidecode import unidecode
#################### INICIO DISPLAY################
def displayBoneco(roundes,global_score,campoDePreenchimento,letrasAdivinhadas,tentativas,filme,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12):
    palavra=unidecode(filme)
    frase_1=F1
    frase_2=F2
    frase_3=F3
    frase_4=F4
    frase_5=F5
    frase_6=F6
    frase_7=F7
    frase_8=F8
    frase_9=F9
    frase_10=F10
    frase_11=F11
    frase_12=F12    
    #####
    letrasdicio={'A':'0','B':'1','C':'2','D':'3','E':'4','F':'5','G':'6','H':'7','I':'8','J':'9','K':'10','L':'11','M':'12','N':'13','O':'14','P':'15','Q':'16','R':'17','S':'18','T':'19','U':'20','V':'21','W':'22','X':'23','Y':'24','Z':'25',' ':'26','&':'27',':':'28','-':'29','1':'30','2':'31','3':'32','4':'33','5':'34','6':'35','7':'36','8':'37','9':'38','0':'39','ç':'40'}
    #####

    #####
    Mascara=[['┌───┐░','│┌─┐│░','││░││░','│└─┘│░','│┌─┐│░','└┘░└┘░','░░░░░░'],
    ['┌──┐░░','│┌┐│░░','│└┘└┐░','│┌─┐│░','│└─┘│░','└───┘░','░░░░░░'],
    ['┌───┐░','│┌─┐│░','││░└┘░','││░┌┐░','│└─┘│░','└───┘░','░░░░░░'],
    ['┌───┐░','└┐┌┐│░','░││││░','░││││░','┌┘└┘│░','└───┘░','░░░░░░'],
    ['┌───┐░','│┌──┘░','│└──┐░','│┌──┘░','│└──┐░','└───┘░','░░░░░░'],
    ['┌───┐░','│┌──┘░','│└──┐░','│┌──┘░','││░░░░','└┘░░░░','░░░░░░'],
    ['┌───┐░','│┌─┐│░','││░└┘░','││┌─┐░','│└┴─│░','└───┘░','░░░░░░'],
    ['┌┐░┌┐░','││░││░','│└─┘│░','│┌─┐│░','││░││░','└┘░└┘░','░░░░░░'],
    ['┌──┐░░','└┤├┘░░','░││░░░','░││░░░','┌┤├┐░░','└──┘░░','░░░░░░'],
    ['░░░┌┐░','░░░││░','░░░││░','░┌┐││░','░│└┘│░','░└──┘░','░░░░░░'],
    ['┌┐┌─┐░','│││┌┘░','│└┘┘░░','│┌┐│░░','│││└┐░','└┘└─┘░','░░░░░░'],
    ['┌┐░░░░','││░░░░','││░░░░','││░┌┐░','│└─┘│░','└───┘░','░░░░░░'],
    ['┌─┐┌─┐','││└┘││','│┌┐┌┐│','││││││','││││││','└┘└┘└┘','░░░░░░'],
    ['┌─┐░┌┐','││└┐││','│┌┐└┘│','││└┐││','││░│││','└┘░└─┘','░░░░░░'],
    ['┌───┐░','│┌─┐│░','││░││░','││░││░','│└─┘│░','└───┘░','░░░░░░'],
    ['┌───┐░','│┌─┐│░','│└─┘│░','│┌──┘░','││░░░░','└┘░░░░','░░░░░░'],
    ['┌───┐░','│┌─┐│░','││░││░','││░││░','│└─┘│░','└──┐│░','░░░└┘░'],
    ['┌───┐░','│┌─┐│░','│└─┘│░','│┌┐┌┘░','│││└┐░','└┘└─┘░','░░░░░░'],
    ['┌───┐░','│┌─┐│░','│└──┐░','└──┐│░','│└─┘│░','└───┘░','░░░░░░'],
    ['┌────┐','│┌┐┌┐│','└┘││└┘','░░││░░','░░││░░','░░└┘░░','░░░░░░'],
    ['┌┐░┌┐░','││░││░','││░││░','││░││░','│└─┘│░','└───┘░','░░░░░░'],
    ['┌┐░░┌┐','│└┐┌┘│','└┐││┌┘','░│└┘│░','░└┐┌┘░','░░└┘░░','░░░░░░'],
    ['┌┐┌┐┌┐','││││││','││││││','│└┘└┘│','└┐┌┐┌┘','░└┘└┘░','░░░░░░'],
    ['┌─┐┌─┐','└┐└┘┌┘','░└┐┌┘░','░┌┘└┐░','┌┘┌┐└┐','└─┘└─┘','░░░░░░'],
    ['┌┐░░┌┐','│└┐┌┘│','└┐└┘┌┘','░└┐┌┘░','░░││░░','░░└┘░░','░░░░░░'],
    ['┌────┐','└──┐─│','░░┌┘┌┘','░┌┘┌┘░','┌┘─└─┐','└────┘','░░░░░░'],
    ['░░░░░░','░░░░░░','░░░░░░','░░░░░░','░░░░░░','░░░░░░','░░░░░░'],
    ['░░░░░░','░░░░░░','░╔══╗░','░║║═╣░','░║║═╣░','░╚══╝░','░░░░░░'],
    ['░░░░░░','░░░░░░','░░╔╗░░','░░╚╝░░','░░╔╗░░','░░╚╝░░','░░░░░░'],
    ['░░░░░░','░░░░░░','░░░░░░','░╔══╗░','░╚══╝░','░░░░░░','░░░░░░'],
    ['░╔╗░░░','╔╝║░░░','╚╗║░░░','░║║░░░','╔╝╚╗░░','╚══╝░░','░░░░░░'],
    ['╔═══╗░','║╔═╗║░','╚╝╔╝║░','╔═╝╔╝░','║║╚═╗░','╚═══╝░','░░░░░░'],
    ['╔═══╗░','║╔═╗║░','╚╝╔╝║░','╔╗╚╗║░','║╚═╝║░','╚═══╝░','░░░░░░'],
    ['╔╗░╔╗░','║║░║║░','║╚═╝║░','╚══╗║░','░░░║║░','░░░╚╝░','░░░░░░'],
    ['╔═══╗░','║╔══╝░','║╚══╗░','╚══╗║░','╔══╝║░','╚═══╝░','░░░░░░'],
    ['╔═══╗░','║╔══╝░','║╚══╗░','║╔═╗║░','║╚═╝║░','╚═══╝░','░░░░░░'],
    ['╔═══╗░','║╔═╗║░','╚╝╔╝║░','░░║╔╝░','░░║║░░','░░╚╝░░','░░░░░░'],
    ['╔═══╗░','║╔═╗║░','║╚═╝║░','║╔═╗║░','║╚═╝║░','╚═══╝░','░░░░░░'],
    ['╔═══╗░','║╔═╗║░','║╚═╝║░','╚══╗║░','╔══╝║░','╚═══╝░','░░░░░░'],
    ['╔═══╗░','║╔═╗║░','║║║║║░','║║║║║░','║╚═╝║░','╚═══╝░','░░░░░░'],
    ['┌───┐░','│┌─┐│░','││░└┘░','││░┌┐░','│└─┘│░','└─┐┌┘░','░░└┘░░']]
    Linhas=[Mascara[i] for i in range(26)]
####
    Letras=[['░'*6 for i in range(7)] for j in range(38)]
    for j in range(len(campoDePreenchimento)):
        if campoDePreenchimento[j]=='_':
            Letras[j]=[' '*6,' '*6,' '*6,' '*6,' '*6,' '*6,'░░░░░░']
    for j in range(len(campoDePreenchimento)):    
        if campoDePreenchimento[j] in [' ','-',':','1','2','3','4','5','6','7','8','9','10','&']:
          Letras[j]=Mascara[int(letrasdicio[campoDePreenchimento[j].upper()])]
####
    # contador=0
    # for i in palavra:
    #     if i == ' ':
    #         Letras[contador]=Mascara[int(letrasdicio[i])]
    #         contador+=1
    #     elif i == '&':
    #         Letras[contador]=Mascara[int(letrasdicio[i])]
    #         contador+=1
    #     elif i == ':':
    #         Letras[contador]=Mascara[int(letrasdicio[i])]
    #         contador+=1
    #     elif i == '1':
    #         Letras[contador]=Mascara[int(letrasdicio[i])]
    #         contador+=1
    #     elif str(i) == '2':
    #         Letras[contador]=Mascara[int(letrasdicio[i])]
    #         contador+=1
    #     elif i == '3':
    #         Letras[contador]=Mascara[int(letrasdicio[i])]
    #         contador+=1
    #     elif i == '4':
    #         Letras[contador]=Mascara[int(letrasdicio[i])]
    #         contador+=1
    #     elif i == '5':
    #         Letras[contador]=Mascara[int(letrasdicio[i])]
    #         contador+=1
    #     elif i == '6':
    #         Letras[contador]=Mascara[int(letrasdicio[i])]
    #         contador+=1
    #     elif i == '7':
    #         Letras[contador]=Mascara[int(letrasdicio[i])]
    #         contador+=1
    #     elif i == '8':
    #         Letras[contador]=Mascara[int(letrasdicio[i])]
    #         contador+=1
    #     elif i == '9':
    #         Letras[contador]=Mascara[int(letrasdicio[i])]
    #         contador+=1
    #     elif i == '0':
    #         Letras[contador]=Mascara[int(letrasdicio[i])]
    #         contador+=1
    #     elif i == '-':
    #         Letras[contador]=Mascara[int(letrasdicio[i])]
    #         contador+=1
    contador=0
    for i in campoDePreenchimento:
        if i in letrasAdivinhadas and i.isalpha():
            Letras[contador]=Mascara[int(letrasdicio[i.upper()])]
            contador+=1
        else:
            contador+=1
    contador=0
    for i in letrasAdivinhadas:
        if i in campoDePreenchimento:
            contador+=1
        else:
            Linhas[int(letrasdicio[i.upper()])]=['x    x',' x  x ','  xx  ','  xx  ',' x  x ','x    x','░░░░░░']
            contador+=1
    if tentativas==7:
        f='░'
        f0='█'
        c='░'
        b='░'
        ad='░'
        ae='░'
        s='░'
        pd='░'
        pe='░'
    elif tentativas==6:
        f='█'
        f0='█'
        c='░'
        b='░'
        ad='░'
        ae='░'
        s='░'
        pd='░'
        pe='░'
    elif tentativas==5:
        f='█'
        f0='█'
        c='█'
        b='░'
        ad='░'
        ae='░'
        s='░'
        pd='░'
        pe='░'
    elif tentativas==4:
        f='█'
        f0='█'
        c='█'
        b='█'
        ad='░'
        ae='░'
        s='─'
        pd='░'
        pe='░'      
    elif tentativas==3:
        f='█'
        f0='█'
        c='█'
        b='█'
        ad='█'
        ae='░'
        s='─'
        pd='░'
        pe='░'             
    elif tentativas==2:
        f='█'
        f0='█'
        c='█'
        b='█'
        ad='█'
        ae='█'
        s='─'
        pd='░'
        pe='░'
    elif tentativas==1:
        f='█'
        f0='█'
        c='█'
        b='█'
        ad='█'
        ae='█'
        s='─'
        pd='█'
        pe='░'            
    elif tentativas==0:
        f='█'
        f0='█'
        c='█'
        b='█'
        ad='█'
        ae='█'
        s='─'
        pd='█'
        pe='█'
    TELA=f'░░░░░░SCORE:{global_score:<{6}}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░Round={roundes:<{4}}░░░░░░░░░░░░░░░░░░░░░░░░░{Linhas[0][0]}░{Linhas[1][0]}░{Linhas[2][0]}░{Linhas[3][0]}░{Linhas[4][0]}░{Linhas[5][0]}░{Linhas[6][0]}░{Linhas[7][0]}░{Linhas[8][0]}░\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{Linhas[0][1]}░{Linhas[1][1]}░{Linhas[2][1]}░{Linhas[3][1]}░{Linhas[4][1]}░{Linhas[5][1]}░{Linhas[6][1]}░{Linhas[7][1]}░{Linhas[8][1]}░\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{Linhas[0][2]}░{Linhas[1][2]}░{Linhas[2][2]}░{Linhas[3][2]}░{Linhas[4][2]}░{Linhas[5][2]}░{Linhas[6][2]}░{Linhas[7][2]}░{Linhas[8][2]}░\n░░░░░░{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}░░░░░░░░░░░░░░░░░░░░░{frase_1:<{35}}░░░░░░░░░░░░░░{Linhas[0][3]}░{Linhas[1][3]}░{Linhas[2][3]}░{Linhas[3][3]}░{Linhas[4][3]}░{Linhas[5][3]}░{Linhas[6][3]}░{Linhas[7][3]}░{Linhas[8][3]}░\n░░░░░░{f}{f}░░░░░░░░░░░{f}{f}░░░░░░░░░░░░░░░░░░░░░{frase_2:<{35}}░░░░░░░░░░░░░░{Linhas[0][4]}░{Linhas[1][4]}░{Linhas[2][4]}░{Linhas[3][4]}░{Linhas[4][4]}░{Linhas[5][4]}░{Linhas[6][4]}░{Linhas[7][4]}░{Linhas[8][4]}░\n░░░░░░{f}{f}░░░░░░░░░░{c}{c}{c}{c}░░░░░░░░░░░░░░░░░░░░{frase_3:<{35}}░░░░░░░░░░░░░░{Linhas[0][5]}░{Linhas[1][5]}░{Linhas[2][5]}░{Linhas[3][5]}░{Linhas[4][5]}░{Linhas[5][5]}░{Linhas[6][5]}░{Linhas[7][5]}░{Linhas[8][5]}░\n░░░░░░{f}{f}░░░░░░░░░{c}{c}{c}{c}{c}{c}░░░░░░░░░░░░░░░░░░░{frase_4:<{35}}░░░░░░░░░░░░░░{Linhas[0][6]}░{Linhas[1][6]}░{Linhas[2][6]}░{Linhas[3][6]}░{Linhas[4][6]}░{Linhas[5][6]}░{Linhas[7][6]}░{Linhas[7][6]}░{Linhas[8][6]}░\n░░░░░░{f}{f}░░░░░░░░░░{c}{c}{c}{c}░░░░░░░░░░░░░░░░░░░░{frase_5:<{35}}░░░░░░░░░░░░░░░░░{Linhas[9][0]}░{Linhas[10][0]}░{Linhas[11][0]}░{Linhas[12][0]}░{Linhas[13][0]}░{Linhas[14][0]}░{Linhas[15][0]}░{Linhas[16][0]}░░░░░\n░░░░░░{f}{f}░░░░░░░░░░░{c}{c}░░░░░░░░░░░░░░░░░░░░░{frase_6:<{35}}░░░░░░░░░░░░░░░░░{Linhas[9][1]}░{Linhas[10][1]}░{Linhas[11][1]}░{Linhas[12][1]}░{Linhas[13][1]}░{Linhas[14][1]}░{Linhas[15][1]}░{Linhas[16][1]}░░░░░\n░░░░░░{f}{f}░░░░░░░{ad}{b}{b}{b}{b}{b}{b}{b}{b}{ae}░░░░░░░░░░░░░░░░░{frase_7:<{35}}░░░░░░░░░░░░░░░░░{Linhas[9][2]}░{Linhas[10][2]}░{Linhas[11][2]}░{Linhas[12][2]}░{Linhas[13][2]}░{Linhas[14][2]}░{Linhas[15][2]}░{Linhas[16][2]}░░░░░\n░░░░░░{f}{f}░░░░░░░{ad}░{b}{b}{b}{b}{b}{b}░{ae}░░░░░░░░░░░░░░░░░{frase_8:<{35}}░░░░░░░░░░░░░░░░░{Linhas[9][3]}░{Linhas[10][3]}░{Linhas[11][3]}░{Linhas[12][3]}░{Linhas[13][3]}░{Linhas[14][3]}░{Linhas[15][3]}░{Linhas[16][3]}░░░░░\n░░░░░░{f}{f}░░░░░░{ad}░░░{b}{b}{b}{b}░░░{ae}░░░░░░░░░░░░░░░░{frase_9:<{35}}░░░░░░░░░░░░░░░░░{Linhas[9][4]}░{Linhas[10][4]}░{Linhas[11][4]}░{Linhas[12][4]}░{Linhas[13][4]}░{Linhas[14][4]}░{Linhas[15][4]}░{Linhas[16][4]}░░░░░\n░░░░░░{f}{f}░░░░░░{ad}░░░{s}{s}{s}{s}░░░{ae}░░░░░░░░░░░░░░░░{frase_10:<{35}}░░░░░░░░░░░░░░░░░{Linhas[9][5]}░{Linhas[10][5]}░{Linhas[11][5]}░{Linhas[12][5]}░{Linhas[13][5]}░{Linhas[14][5]}░{Linhas[15][5]}░{Linhas[16][5]}░░░░░\n░░░░░░{f}{f}░░░░░░░░░░{pd}{pd}{pe}{pe}░░░░░░░░░░░░░░░░░░░░{frase_11:<{35}}░░░░░░░░░░░░░░░░░{Linhas[9][6]}░{Linhas[10][6]}░{Linhas[11][6]}░{Linhas[12][6]}░{Linhas[13][6]}░{Linhas[14][6]}░{Linhas[15][6]}░{Linhas[16][6]}░░░░░\n░░░░░░{f}{f}░░░░░░░░░{pd}{pd}░░{pe}{pe}░░░░░░░░░░░░░░░░░░░{frase_12:<{35}}░░░░░░░░░░░░░░{Linhas[17][0]}░{Linhas[18][0]}░{Linhas[19][0]}░{Linhas[20][0]}░{Linhas[21][0]}░{Linhas[22][0]}░{Linhas[23][0]}░{Linhas[24][0]}░{Linhas[25][0]}░\n░░░░░░{f}{f}░░░░░░░░{pd}{pd}░░░░{pe}{pe}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{Linhas[17][1]}░{Linhas[18][1]}░{Linhas[19][1]}░{Linhas[20][1]}░{Linhas[21][1]}░{Linhas[22][1]}░{Linhas[23][1]}░{Linhas[24][1]}░{Linhas[25][1]}░\n░░░░░░{f}{f}░░░░░░░{pd}{pd}░░░░░░{pe}{pe}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{Linhas[17][2]}░{Linhas[18][2]}░{Linhas[19][2]}░{Linhas[20][2]}░{Linhas[21][2]}░{Linhas[22][2]}░{Linhas[23][2]}░{Linhas[24][2]}░{Linhas[25][2]}░\n░░░░░░{f}{f}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{Linhas[17][3]}░{Linhas[18][3]}░{Linhas[19][3]}░{Linhas[20][3]}░{Linhas[21][3]}░{Linhas[22][3]}░{Linhas[23][3]}░{Linhas[24][3]}░{Linhas[25][3]}░\n░░░░░░{f0}{f0}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{Linhas[17][4]}░{Linhas[18][4]}░{Linhas[19][4]}░{Linhas[20][4]}░{Linhas[21][4]}░{Linhas[22][4]}░{Linhas[23][4]}░{Linhas[24][4]}░{Linhas[25][4]}░\n░░░░░░{f0}{f0}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{Linhas[17][5]}░{Linhas[18][5]}░{Linhas[19][5]}░{Linhas[20][5]}░{Linhas[21][5]}░{Linhas[22][5]}░{Linhas[23][5]}░{Linhas[24][5]}░{Linhas[25][5]}░\n░░░░░░{f0}{f0}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{Linhas[17][6]}░{Linhas[18][6]}░{Linhas[19][6]}░{Linhas[20][6]}░{Linhas[21][6]}░{Linhas[22][6]}░{Linhas[23][6]}░{Linhas[24][6]}░{Linhas[25][6]}░\n░░░░░░{f0}{f0}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░{f0}{f0}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░{f0}{f0}░░░░░░░░░{Letras[0][0]}░{Letras[1][0]}░{Letras[2][0]}░{Letras[3][0]}░{Letras[4][0]}░{Letras[5][0]}░{Letras[6][0]}░{Letras[7][0]}░{Letras[8][0]}░{Letras[9][0]}░{Letras[10][0]}░{Letras[11][0]}░{Letras[12][0]}░{Letras[13][0]}░{Letras[14][0]}░{Letras[15][0]}░{Letras[16][0]}░{Letras[17][0]}░{Letras[18][0]}░░░░░\n░░░░░░{f0}{f0}░░░░░░░░░{Letras[0][1]}░{Letras[1][1]}░{Letras[2][1]}░{Letras[3][1]}░{Letras[4][1]}░{Letras[5][1]}░{Letras[6][1]}░{Letras[7][1]}░{Letras[8][1]}░{Letras[9][1]}░{Letras[10][1]}░{Letras[11][1]}░{Letras[12][1]}░{Letras[13][1]}░{Letras[14][1]}░{Letras[15][1]}░{Letras[16][1]}░{Letras[17][1]}░{Letras[18][1]}░░░░░\n░░░░░{f0}{f0}{f0}{f0}░░░░░░░░{Letras[0][2]}░{Letras[1][2]}░{Letras[2][2]}░{Letras[3][2]}░{Letras[4][2]}░{Letras[5][2]}░{Letras[6][2]}░{Letras[7][2]}░{Letras[8][2]}░{Letras[9][2]}░{Letras[10][2]}░{Letras[11][2]}░{Letras[12][2]}░{Letras[13][2]}░{Letras[14][2]}░{Letras[15][2]}░{Letras[16][2]}░{Letras[17][2]}░{Letras[18][2]}░░░░░\n░░░{f0}{f0}{f0}{f0}{f0}{f0}{f0}{f0}░░░░░░{Letras[0][3]}░{Letras[1][3]}░{Letras[2][3]}░{Letras[3][3]}░{Letras[4][3]}░{Letras[5][3]}░{Letras[6][3]}░{Letras[7][3]}░{Letras[8][3]}░{Letras[9][3]}░{Letras[10][3]}░{Letras[11][3]}░{Letras[12][3]}░{Letras[13][3]}░{Letras[14][3]}░{Letras[15][3]}░{Letras[16][3]}░{Letras[17][3]}░{Letras[18][3]}░░░░░\n░░{f0}{f0}{f0}{f0}{f0}{f0}{f0}{f0}{f0}{f0}░░░░░{Letras[0][4]}░{Letras[1][4]}░{Letras[2][4]}░{Letras[3][4]}░{Letras[4][4]}░{Letras[5][4]}░{Letras[6][4]}░{Letras[7][4]}░{Letras[8][4]}░{Letras[9][4]}░{Letras[10][4]}░{Letras[11][4]}░{Letras[12][4]}░{Letras[13][4]}░{Letras[14][4]}░{Letras[15][4]}░{Letras[16][4]}░{Letras[17][4]}░{Letras[18][4]}░░░░░\n░{f0}{f0}{f0}{f0}{f0}{f0}{f0}{f0}{f0}{f0}{f0}{f0}░░░░{Letras[0][5]}░{Letras[1][5]}░{Letras[2][5]}░{Letras[3][5]}░{Letras[4][5]}░{Letras[5][5]}░{Letras[6][5]}░{Letras[7][5]}░{Letras[8][5]}░{Letras[9][5]}░{Letras[10][5]}░{Letras[11][5]}░{Letras[12][5]}░{Letras[13][5]}░{Letras[14][5]}░{Letras[15][5]}░{Letras[16][5]}░{Letras[17][5]}░{Letras[18][5]}░░░░░\n{f0}{f0}{f0}{f0}{f0}{f0}{f0}{f0}{f0}{f0}{f0}{f0}{f0}{f0}░░░{Letras[0][6]}░{Letras[1][6]}░{Letras[2][6]}░{Letras[3][6]}░{Letras[4][6]}░{Letras[5][6]}░{Letras[6][6]}░{Letras[7][6]}░{Letras[8][6]}░{Letras[9][6]}░{Letras[10][6]}░{Letras[11][6]}░{Letras[12][6]}░{Letras[13][6]}░{Letras[14][6]}░{Letras[15][6]}░{Letras[16][6]}░{Letras[17][6]}░{Letras[18][6]}░░░░░\n░░░░░░░░░░░░░░░░░{ Letras[19][0]}░{ Letras[20][0]}░{ Letras[21][0]}░{ Letras[22][0]}░{ Letras[23][0]}░{ Letras[24][0]}░{ Letras[25][0]}░{ Letras[26][0]}░{ Letras[27][0]}░{ Letras[28][0]}░{ Letras[29][0]}░{ Letras[30][0]}░{ Letras[31][0]}░{ Letras[32][0]}░{ Letras[33][0]}░{ Letras[34][0]}░{ Letras[35][0]}░{ Letras[36][0]}░{ Letras[37][0]}░░░░░\n░░░░░░░░░░░░░░░░░{ Letras[19][1]}░{ Letras[20][1]}░{ Letras[21][1]}░{ Letras[22][1]}░{ Letras[23][1]}░{ Letras[24][1]}░{ Letras[25][1]}░{ Letras[26][1]}░{ Letras[27][1]}░{ Letras[28][1]}░{ Letras[29][1]}░{ Letras[30][1]}░{ Letras[31][1]}░{ Letras[32][1]}░{ Letras[33][1]}░{ Letras[34][1]}░{ Letras[35][1]}░{ Letras[36][1]}░{ Letras[37][1]}░░░░░\n░░░░░░░░░░░░░░░░░{ Letras[19][2]}░{ Letras[20][2]}░{ Letras[21][2]}░{ Letras[22][2]}░{ Letras[23][2]}░{ Letras[24][2]}░{ Letras[25][2]}░{ Letras[26][2]}░{ Letras[27][2]}░{ Letras[28][2]}░{ Letras[29][2]}░{ Letras[30][2]}░{ Letras[31][2]}░{ Letras[32][2]}░{ Letras[33][2]}░{ Letras[34][2]}░{ Letras[35][2]}░{ Letras[36][2]}░{ Letras[37][2]}░░░░░\n░░░░░░░░░░░░░░░░░{ Letras[19][3]}░{ Letras[20][3]}░{ Letras[21][3]}░{ Letras[22][3]}░{ Letras[23][3]}░{ Letras[24][3]}░{ Letras[25][3]}░{ Letras[26][3]}░{ Letras[27][3]}░{ Letras[28][3]}░{ Letras[29][3]}░{ Letras[30][3]}░{ Letras[31][3]}░{ Letras[32][3]}░{ Letras[33][3]}░{ Letras[34][3]}░{ Letras[35][3]}░{ Letras[36][3]}░{ Letras[37][3]}░░░░░\n░░░░░░░░░░░░░░░░░{ Letras[19][4]}░{ Letras[20][4]}░{ Letras[21][4]}░{ Letras[22][4]}░{ Letras[23][4]}░{ Letras[24][4]}░{ Letras[25][4]}░{ Letras[26][4]}░{ Letras[27][4]}░{ Letras[28][4]}░{ Letras[29][4]}░{ Letras[30][4]}░{ Letras[31][4]}░{ Letras[32][4]}░{ Letras[33][4]}░{ Letras[34][4]}░{ Letras[35][4]}░{ Letras[36][4]}░{ Letras[37][4]}░░░░░\n░░░░░░░░░░░░░░░░░{ Letras[19][5]}░{ Letras[20][5]}░{ Letras[21][5]}░{ Letras[22][5]}░{ Letras[23][5]}░{ Letras[24][5]}░{ Letras[25][5]}░{ Letras[26][5]}░{ Letras[27][5]}░{ Letras[28][5]}░{ Letras[29][5]}░{ Letras[30][5]}░{ Letras[31][5]}░{ Letras[32][5]}░{ Letras[33][5]}░{ Letras[34][5]}░{ Letras[35][5]}░{ Letras[36][5]}░{ Letras[37][5]}░░░░░\n░░░░░░░░░░░░░░░░░{ Letras[19][6]}░{ Letras[20][6]}░{ Letras[21][6]}░{ Letras[22][6]}░{ Letras[23][6]}░{ Letras[24][6]}░{ Letras[25][6]}░{ Letras[26][6]}░{ Letras[27][6]}░{ Letras[28][6]}░{ Letras[29][6]}░{ Letras[30][6]}░{ Letras[31][6]}░{ Letras[32][6]}░{ Letras[33][6]}░{ Letras[34][6]}░{ Letras[35][6]}░{ Letras[36][6]}░{ Letras[37][6]}░░░░░' 
    return [TELA,tentativas]
################### FIM DISPLAY ###################

pygame.init()

mixer.music.load('jogoDaForcaFilmes/backMusic.mp3')
mixer.music.set_volume(0.1)
mixer.music.play(-1)

def sortearID():
    id = random.randint(1,10000)
    return id

def dificuldade():
    nivel = input('Selecione o nível de dificuldade do jogo:\n 1 - Fácil\n 2 - Médio\n 3 - Dificil\n')
    while nivel not in ['1','2','3']:
        nivel = input('Entrada inválida, selecione novamente o nível de dificuldade do jogo:\n 1 - Fácil\n 2 - Médio\n 3 - Dificil\n')
    if nivel == '1':
        return (100000000,10000000000000000000) # filtro de filmes com bilheteria maior que $100M.
    elif nivel == '2':
        return (20000000,100000000)             # filtro de filmes com bilheteria maior que $20M.
    else:
        return (1000000,20000000)               # filtro de filmes com bilheteria maior que $10M.

def checarDificuldade(id, lv):
    movie = tmdb.Movies(id)
    response = movie.info(language = 'pt-BR')
    popularidade = movie.popularity
    if lv[0] < popularidade <= lv[1]:
        return True
    else:
        return False

def pegarFilme(id):
    movie = tmdb.Movies(id)
    response = movie.info(language = 'pt-BR')
    titulo = movie.title
    pop = movie.popularity
    #print(f'tag: {movie.tagline}, tamanho: {len(movie.tagline)}')
    #print(id)
    #print(titulo)
    #rint(movie)
    return movie

def gerarDica(id):
    movie = tmdb.Movies(id)
    response = movie.info(language = 'pt-BR')
    if len(movie.tagline) != 0:
        dica = movie.tagline
    elif len(movie.overview) != 0:
        dica = movie.overview     
    else:    
        dica = 'Sem dica :(' 
    return dica


def jogo(filme, id,score=0,roundes=1):
    F1='░'*35
    F2='░'*35
    F3='░'*35
    F4='░'*35
    F5='░'*35
    F6='░'*35
    F7='░'*35
    F8='░'*35
    F9='░'*35
    F10='░'*35
    F11='░'*35
    F12='░'*35
    campoDePreenchimento = ''
    for i in unidecode(filme):
        if i.isalpha():
            campoDePreenchimento += '_'
        else:
            campoDePreenchimento += i
    acertou = False
    letrasAdivinhadas = []
    filmesAdivinhados = []
    tentativas = 7 #mudei aqui pra incluir a forca
    F1='Bem Vindo ao Jogo da Forca!'
    F2=f'Tentativas restantes: {tentativas}'
    
    print(displayBoneco(roundes,score,campoDePreenchimento,letrasAdivinhadas,tentativas,filme,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12)[0])
    #print(campoDePreenchimento, '\n')
    while not acertou and tentativas > 0:
        if tentativas == 2:
            dica=gerarDica(id)
            F7=f'A dica é: {dica}'[0:34]
            F8=f'A dica é: {dica}'[34:69]
            F9=f'A dica é: {dica}'[69:104]
            F10=f'A dica é: {dica}'[104:134]+'...'
        palpite = unidecode(input('Adivinhe uma letra ou filme: ').upper())
        if len(palpite) == 1 and palpite.isalpha():
            if palpite in letrasAdivinhadas:
                F2=f'Tentativas restantes: {tentativas}'
                F3=f'Você já tentou a letra: {palpite}!'
            elif palpite not in unidecode(filme):
                F2=f'Tentativas restantes: {tentativas}'
                F3=f'O filme não tem a letra: {palpite}'
                somErro = mixer.Sound('jogoDaForcaFilmes/letraErrada.wav')
                somErro.play()
                tentativas -= 1
                letrasAdivinhadas.append(palpite)
            else:
                F2=f'Tentativas restantes: {tentativas}'
                F3=f'Quase lá, o título tem a letra: {palpite}'
                somAcerto = mixer.Sound('jogoDaForcaFilmes/letraCerta.wav')
                somAcerto.play()
                letrasAdivinhadas.append(palpite)
                palavraComoLista = list(campoDePreenchimento)
                indices = [i for i, letra in enumerate(unidecode(filme)) if letra == palpite]
                for index in indices:
                    palavraComoLista[index] = filme[index]
                campoDePreenchimento = ''.join(palavraComoLista)
                if '_' not in campoDePreenchimento:
                    acertou =  True
        elif len(palpite) == len(filme):
            if palpite in filmesAdivinhados:
                F2=f'Tentativas restantes: {tentativas}'
                F3=f'Você já tentou o filme: {palpite}!'
            elif palpite not in filmesAdivinhados and palpite != filme:
                F2=f'Tentativas restantes: {tentativas}'
                F3=f'O filme não é: {palpite}'
                tentativas -= 1
                filmesAdivinhados.append(palpite)
            else:
                acertou =  True
                campoDePreenchimento = unidecode(filme)
                print(displayBoneco(roundes,score,campoDePreenchimento,campoDePreenchimento,tentativas,filme,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12)[0])
                time.sleep(2)
        else:
            F3=f'Palpite inválido.'
        print(displayBoneco(roundes,score,campoDePreenchimento,letrasAdivinhadas,tentativas,filme,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12)[0])
        #print(campoDePreenchimento, '\n')
        print('\n')
    if acertou:
        score+=tentativas
        F3='░'*35 #apaga a lista de feedback
        F4=f'Parabéns, acertou o filme!' #escreve mensagem final na linha 4
        somAcertouFilme = mixer.Sound('jogoDaForcaFilmes/filmeCerto.wav')
        somAcertouFilme.play()
        venceu=True
        print(displayBoneco(roundes,score,campoDePreenchimento,letrasAdivinhadas,tentativas,filme,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12)[0])
        time.sleep(2)
    else:
        #vamos dividir a mensagem final em tres linhas
        F2='░'*35
        F6='░'*35
        F7='░'*35
        F8='░'*35
        F9='░'*35
        F10='░'*35
        F11='░'*35
        F12='░'*35
        F3=f'Lamento, acabaram as tentativas.'
        F4=f'O título do filme era:'
        F5=f'{filme.replace("*", " ")}.'[0:34]
        F6=f'Não desanime... Tente novamente!'
        venceu=False
        print(displayBoneco(roundes,score,'FIM DE JOGO','FIM DE JOGO',tentativas,filme,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12)[0])
        time.sleep(2)
        #print(f'Acabaram as tentativas. O filme era: {filme.replace("*", " ")}')
    return [score,tentativas]



def iniciarJogo(score=0,roundes=1):
    onlystring=False
    while onlystring==False:
        id = sortearID()
        urlInvalida = True
        popularity = 0
        dif = dificuldade()
        checkPop = True
        print("Escolhendo seu filme...")        # As vezes demora para escolher o filme.
        while urlInvalida or checkPop:
            try:
                filme = pegarFilme(id).title.upper()
                movie = pegarFilme(id)
                urlInvalida = False
                popularity = movie.revenue
                if not (dif[0] < popularity < dif[1]) :
                    id = sortearID()
                    checkPop = True
                else:
                    checkPop = False
                    id = id
            except:
                id = sortearID()
                urlInvalida = True
        aux=0
        for i in filme:
            if len(filme)>36:
                aux+=1
            elif i.isalpha()==True or i in [' ','-',':','1','2','3','4','5','6','7','8','9','10','&']:
                aux+=0
            else:
                aux+=1
        if aux==0:
            onlystring=True

    #print(unidecode(filme))
    return jogo(unidecode(filme), id, score, roundes)
    #print(filme)

def main():
    rodada=1  
    info=iniciarJogo(score=0,roundes=1)
    placar=info[0]
    if info[1]==False: #se ele perdeu a partida zera o placar
        rodada=0
        placar=0
    replay=True
    while replay==True:
        pergunta=unidecode(input('Jogar novamente? (S/N) ').upper())
        if pergunta == 'S':
            rodada+=1
            info=iniciarJogo(score=placar,roundes=rodada)
            if info[1]==False: #se ele perdeu a partida zera o placar os rounds
                rodada=0
                placar=0
        elif pergunta =='N':
            replay=False

        else:
            print('Entrada Inválida!')
            time.sleep(2)

if __name__ == "__main__":
    main()