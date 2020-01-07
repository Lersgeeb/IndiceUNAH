import pandas as pd
import numpy as np


def prom(data):
    uvs = data["UV"].values
    rate = data["CALIFICACION"].values
    prom = (rate @ uvs.T) / np.sum(uvs)
    return prom

def addClass(data):
    code = input("CODIGO: ")
    subject = input("ASIGNATURA: ")
    uv = int(input("UV: "))
    section = input("SECCION: ")
    year = int(input("AÑO: "))
    period = int(input("PERIODO: "))
    rate = int(input("CALIFICACION: "))
    obs = input("OBS: ")       
    
    #dataRow = pd.DataFrame([[code, subject, uv, section, year, period, rate, obs]],columns = ["CODIGO", "ASIGNATURA", 
    #                                                                                       "UV", "SECCION", "AÑO", "PERIODO", 
    #                                                                                      "CALIFICACION", "OBS"])
    
    data = data.append({"CODIGO":code, "ASIGNATURA":subject, 
                        "UV":uv, "SECCION":section, "AÑO":year, "PERIODO":period, 
                        "CALIFICACION":rate , "OBS":obs}, ignore_index=True)
    
    return data

def addClassShort(data):
    subject = input("ASIGNATURA: ")
    uv = int(input("UV: "))
    #section = input("SECCION: ")
    year = int(input("AÑO: "))
    period = int(input("PERIODO: "))
    rate = int(input("CALIFICACION: "))
    
    data = data.append({"ASIGNATURA":subject, 
                        "UV":uv, "AÑO":year, "PERIODO":period, 
                        "CALIFICACION":rate}, ignore_index=True)
    return data


def readData(name):
    if(name):
        data = pd.read_csv(name, sep = '\t', names =  ["CODIGO", "ASIGNATURA", "UV", "SECCION", "AÑO", "PERIODO", 
                                                       "CALIFICACION", "OBS"])
    else:
        data = pd.DataFrame(columns=["CODIGO", "ASIGNATURA", "UV", "SECCION", "AÑO", "PERIODO", 
                                                       "CALIFICACION", "OBS"])
    return data

