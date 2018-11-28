# This Python file uses the following encoding: utf-8

class Envio():
    #Possui uma lista de atividades
    #Possui infos sobre autor = descartar
    pass
class Atividade():
    #Possui uma string          Sport
    #Possui um  formato hora    ID
    #Possui um  ????            Note        -formato desconhecido
    #Possui um  Lap             Volta
    pass

class Lap():
    #Possui um  formato hora            StartTime
    #Possui uma lista de Trackpoint     Track
    #Possui um  float                   DistanciaTotal
    #Possui um  float                   TempoTotal
    #Possui um  float                   Calorias
    #Possui um  ????                    Intensity
    #Possui um  ????                    TriggerMethod

    pass

class Trackpoint():
    #Possui um  float           Distancia (em metros)
    #Possui um  formato hora    Tempo
    #Possui um posicao          Descartar
    #Possui um float            Altitude


filein = open("2018-11-27T16_25_39-02_00_PT57M3S_Corrida.tcx", "r")

linha = filein.readline()
while(linha):
    linha = linha.replace(" ", "")

#    print(linha, end='')
    if "garmin" in linha:
        linha = filein.readline()
        pass

    if "<Activity" in linha:
        linha = linha.replace(" ", "")
        print(linha, end='')



    linha = filein.readline()
