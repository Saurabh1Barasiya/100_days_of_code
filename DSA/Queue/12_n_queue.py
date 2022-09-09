# Implement N_queue in a single array.
class N_queue:
    def __init__(self,n,k):
        # n is number of stack elements in array.
        # k is the number of queue.

        self.arr = [0] * n
        self.front = [-1] * k
        self.rare = [-1] * k
        self.next = [i for i in range(1,n+1)]
        self.next[-1] = -1
        self.free_spot = 0

    def en_queue(self,qn,data):
        if self.free_spot == -1:
            print("Queue is full can't insert.")
            return
        else:
            # get a index where you add the data.
            index = self.free_spot

            # update free_spot
            self.free_spot = self.next[index]

            # kya first element h .
            if self.front[qn-1] == -1:
                self.front[qn-1] = index
            else:
                # to make a link.
                # link new element to previous element. 
                self.next[self.rare[qn-1]] = index
            
            # block the position.
            self.next[index] = -1

            # rare ko update kero ,tabhi to push kar paoge.
            self.rare[qn-1] = index

            # data push kar do.
            self.arr[index] = data

    def de_queued(self,qn):
        # check queue is empty or not.
        if self.front[qn-1] == -1:
            print("queue is empty can't delete")
            return
        else:
            # find kero index ko.
            index = self.front[qn-1]

            # front ko aage badha do.
            self.front[qn-1] = self.next[index]

            # free space ko manage kero.

            self.next[index] = self.free_spot
            self.free_spot = index
            ans = self.arr[index]
            self.arr[index] = 0
            return ans

nq = N_queue(6,3)

nq.en_queue(1,10)
nq.en_queue(2,20)
nq.en_queue(1,30)
nq.en_queue(2,40)
nq.en_queue(1,50)
nq.en_queue(2,60)

print(nq.de_queued(1))
print(nq.de_queued(1))
print(nq.de_queued(1))
print(nq.de_queued(2))
print(nq.de_queued(2))
print(nq.de_queued(2))

nq.en_queue(1,100)
nq.en_queue(1,200)
nq.en_queue(1,300)
nq.en_queue(2,400)
nq.en_queue(2,500)
nq.en_queue(2,600)


print(nq.de_queued(1))
print(nq.de_queued(1))
print(nq.de_queued(1))
print(nq.de_queued(2))
print(nq.de_queued(2))
print(nq.de_queued(2))
