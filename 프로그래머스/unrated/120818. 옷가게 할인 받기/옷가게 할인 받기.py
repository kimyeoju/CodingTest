def solution(price):
    if price >= 500000:
        a = price * 0.2
        price -= a
        
    elif price >= 300000:
        a = price * 0.1
        price -= a
        
    elif price >= 100000:
        a = price * 0.05
        price -= a
    
    return int(price)