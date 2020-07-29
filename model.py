import requests

def theanswer(base, new, themoney):
    
    link  = f"https://api.exchangeratesapi.io/latest?base={base}"
    response = requests.get(link).json()
    ratio = (response['rates'][f"{new}"])
    conversion = float(themoney)*float(ratio)
    conversion = round(conversion,2)
    return(conversion)
    # date = response['date']
    # print('dat')