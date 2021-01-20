import random as rnd
from string import ascii_letters
import pandas as pd
import csv
from datetime import datetime, timedelta


pais_nombre=[]
pais_abrev=[]
actividades=['Empresario', 'Estudiante', 'Docente','Profesional']
with open('paises.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        pais_nombre.append(row[0])
        pais_abrev.append(row[2])
pais_nombre.__delitem__(0)
pais_abrev.__delitem__(0)
letters=ascii_letters[:26]
numbers=[ x for x in range(0,10) ] 
users=[]
for i in range(rnd.randint(1237,3571)):
    num_letters=rnd.randint(4,8)
    bool_numbers=bool(rnd.getrandbits(1))
    user=''
    for j in range(num_letters):
        user+=letters[rnd.randint(0,len(letters)-1)]
    if bool_numbers:
        user+=str(numbers[rnd.randint(0,len(numbers)-1)])
        user+=str(numbers[rnd.randint(0,len(numbers)-1)])
    if user not in users:
        users.append(user)
tot_user=len(users)-1
dict_global=[]
for i in users:
    d={}
    d['usuario']=i
    d['visitas']=rnd.randint(23,223)
    d['taza_rebote']=rnd.randint(17,47)
    d['tiempo_de_visita']=str(rnd.randint(23,223))
    bool_act=bool(rnd.getrandbits(1))
    if bool_act:
        d['actividad_ocupacional']=actividades[0]
    else:
        d['actividad_ocupacional']=actividades[rnd.randint(0,len(actividades)-1)]
    d['pais']=pais_abrev[rnd.randint(0,len(pais_abrev)-1)]
    dict_global.append(d)
pd.DataFrame(dict_global).to_csv('out1.csv', index=False)

info=[]
dict_global2=[]
for i in range(rnd.randint(97,223)):
    info.append("Infoproducto_"+str(i))
for i in range(rnd.randint(4000,6000)):
    d={}
    d['usuario']=users[rnd.randint(0,tot_user)]
    d['info_producto']=rnd.randint(0,len(info)-1)
    dict_global2.append(d)
pd.DataFrame(dict_global2).to_csv('out2.csv', index=False)

info2=[]
dict_global3=[]
for i in range(len(info)):
    d={}
    d['info_producto']=i
    d['descripcion']=info[i]
    d['precio']=rnd.randint(1,49)+(rnd.randint(1,100)/100)
    d['autor']=users[rnd.randint(0,tot_user)]
    dict_global3.append(d)
pd.DataFrame(dict_global3).to_csv('out4.csv', index=False)

conexiones=[]

for i in dict_global:
    dia=rnd.randint(1,28)
    hora=rnd.randint(0,23)
    minuto=rnd.randint(0,59)
    new_date = datetime(2020, rnd.randint(1,12), dia, hora, minuto, 00, 00000)
    tomorrow=new_date
    for j in range(i['visitas']):
        d={}
        dia=rnd.randint(1,5)
        hora=rnd.randint(0,23)
        minuto=rnd.randint(0,59)
        tomorrow = tomorrow + timedelta(days=dia)
        tomorrow=tomorrow+timedelta(hours=hora)
        tomorrow=tomorrow+timedelta(minutes=minuto)
        d['usuario']=i['usuario']
        d['conexion']=tomorrow
        d['anio']=tomorrow.year
        d['mes']=tomorrow.month
        d['hora']=tomorrow.hour
        d['dia']=tomorrow.day
        d['minute']=tomorrow.minute
        
        conexiones.append(d)
pd.DataFrame(conexiones).to_csv('out3.csv', index=False)


