# reverse  words in a string .

def convert(s):
    st_arr = s.split(" ")
    for index,value in enumerate(st_arr):
        st_arr[index] = value[::-1]
    return " ".join(st_arr)
    
if __name__ == '__main__':
    s = "my name is love"
    ans = convert(s)
    print(ans)