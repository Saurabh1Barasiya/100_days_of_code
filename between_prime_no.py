# print prime numbers 
'''
n = int(input("how many prime numbers you want to generate."))
num = n
count = 0
for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            # print("Not prime",i)
            break
    else:
        print("prime",i)
        count += 1
        print("count",count)   
        if count == num:
            # print("count",count)
            break
    n = n*10
'''

# range function increment nahi karta h.
'''
n = 5
for i in range(n):
    print(i,end=" ")
    n = n * 10
'''


# str = "keep smiling"
# print(str.replace("$miling",'smilling always'))

# group = [4,5,9,11,12]
# def slicer(list,size):
#     return [group[i:i+size] for i in range(0,len(list),size)]
# print(slicer(group,3))

# city = ["chheni","bang","coggi"]
# for i in city:
#     if (i == "delhi"):
#         city += 1
#         break
#     elif (i == "coggi"):
#         continue
#     print(i)

class Passenger:
    def init(self,passengerid,Name,age):
        self.passengerid=passengerid
        self.Name=Name
        self.age=age   
class Ticket:
    def init(self,ticketDate="2020-12-09",ticketid, ticketType,travelType,trainNo,trainDest,passengerList,TrainTuple,fare):
        self.ticketDate=ticketDate
        self.ticketid=ticketid
        self.ticketType=ticketType
        self.travelType=travelType
        self.trainNo=trainNo
        self.trainDest=trainDest
        self.passengerList=passengerList
        self.TrainTuple=tuple()
        self.fare=0.0
        
    def TrainTuple(self,ticketType,trainList,trainIdList,trainIdPriceGen,trainIdPriceTatkal):
        if ticketType=='general':
            tuple(list(self.TrainTuple).append((trainList,trainIdList,trainIdPriceGen)))
        else if ticketType=='tatkal':
             tuple(list(self.TrainTuple).append((trainList,trainIdList,trainIdPriceTatkal)))
        
    def Calculate(self,trainSrcDest,travelType):
        if travelType=="one way":