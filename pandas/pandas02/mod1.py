# mod1.py
def sum(a, b):
    return a + b

def safe_sum(a, b): 
    if type(a) != type(b): 
        print("자료형이 달라서 더할 수 없습니다.")
        return 
    else: 
        result = sum(a, b) 
    return result

