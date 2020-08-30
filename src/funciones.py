import pandas as pd
import re


def filtrowater(a):
    if "surf" in a.lower():
        return "IN WATER"
    elif "padd" in a.lower():
        return "IN WATER"
    elif "swimm" in a.lower():
        return "IN WATER"
    elif "diving" in a.lower():
        return "IN WATER"
    elif "boarding" in a.lower():
        return "IN WATER"
    else:
        return "OTHER"

def edad(x):
    if "teen" in str(x).lower():
        return "15"
    elif "young" in str(x).lower():
        return "20"
    elif "adult" in str(x).lower():
        return "30"
    else:
        return x

def mes(x):
    if "month" in x.lower():
        return x.split(" ")[0]
    else:
        return x

def qs(x):
    if "s" in str(x):
        return x[0:2]
    elif "� " == str(x):
        return "9"
    elif "�" in str(x):
        return x[0]+"0"
    elif ">50" == str(x):
        return "55"
    elif "Both" in str(x):
        return "11"
    else:
        return x

def or_to(x):
    if "or" in str(x):
        a = int(x.split(" or ")[0])
        b = int(x.split(" or ")[-1])
        return str((a+b)//2) 
    elif "to" in str(x):
        a = int(x.split(" to ")[0])
        b = int(x.split(" to ")[-1])
        return str((a+b)//2)
    else:
        return x

def and_esp_str(x):
    pattern = r"\d+"
    res = re.findall(pattern,x) 
    if res:
        if len(res)>1:
            suma = 0
            for j in res:
                j = int(j)
                suma += j
            return str(suma//len(res))
        elif len(res) == 1:
            return res[0]
    else:
        return None