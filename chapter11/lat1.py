#menghitung selisih dalam satuan hari
from datetime import*

def diffDate(i):
    now = datetime.date(datetime.now())
    i= datetime.strptime(i, '%Y-%m-%d').date()
    return abs(i-now)
    
print(format(diffDate('2022-01-31').days))
