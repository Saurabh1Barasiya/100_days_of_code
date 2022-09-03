# Circular tour .

class petrolPump:
    def __init__(self,a, b):
        self.petrol = a
        self.distance = b


def printTour(arr,n):
    balence = start = deficiat =0
    # deficiat -->  kami.
    
    i = 0
    while i < n:
        balence = balence + arr[i].petrol - arr[i].distance
        if balence < 0:
            deficiat += balence
            start = i+1
            balence = 0
        i += 1
    if (deficiat + balence) >= 0:
        return start
    else:
        return -1

# Driver code
if __name__ == '__main__':
    arr = [petrolPump(6, 4),petrolPump(3, 6),petrolPump(7, 3)] 
    arr = [petrolPump(6, 5),petrolPump(7, 6),petrolPump(4, 7),petrolPump(10, 8),petrolPump(6, 6),petrolPump(5, 4)] 
 
    n = len(arr);
    start = printTour(arr, n);
 
    if (start == -1):
        print("No solution");
    else:
        print("Start = " , start);
 