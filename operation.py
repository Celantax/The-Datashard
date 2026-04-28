import statistics

def calculate_range(x):
    return max(x) - min(x)
def calculate_mode(z):
    mode = statistics.mode(z)
    return mode
       
    
def calculate_mean(y):
    s = 0 
    for i in y:
        s += i
    return s//len(y)