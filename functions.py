from datetime import datetime

def today():
    today = datetime.now()
    return today
    
def verify_date(date):
    try:
        date_format = datetime.strptime(date, "%d-%m-%Y")
        return date_format
    except:
        raise Exception("Entrada inválida! Exemplo sugerido: 01-09-2000")

def verify_due(date_ref):
    data_input = verify_date(date=date_ref)
    if today() > data_input:
        return True
    else:
        return False