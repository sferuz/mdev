#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 17:19:05 2026

@author: dvp
"""

mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
 print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
print("Hurmat bilan, Palonchiyevlar oilasi")

sonlar=list(range(1,11))
for son in sonlar:
    print(f"{son}ning kvadrati {son**2}ga teng.")
print("tamom")


#-------------10 dars
x, y = 25, 50 # x=25 va y=50
print("x>y") if x>y else print("x<y")
#
#----------------------    11        dars 11

# ***


zakaz=['osh','somsa','shashlik','anjir piyoz']
menu=["osh","shashlik",'anjir piyoz', "halim",'norin']
if zakaz:
    for taom in zakaz:
        if taom in menu:
            print(f"Menuda {taom} bor.")
        else:
            print(f"Kechirasiz {taom} menuda yo'q")
else:
    print('savat bo\'sh')
