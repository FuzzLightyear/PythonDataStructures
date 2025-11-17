#Author FuzzLightyear, aka. Fuzzifier, aka. SudoScientist
#Date 12/27/2020
#Linked List with added features. Stack, Queue built off of LinkedList


class llnode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def print(self, count):
        print(count,").",self.value)
        if self.right:
            self.right.print(count+1)

class linkedlist():
    def __init__(self):
        self.root = None
    def print(self):
        print("Current List")
        if self.root:
            self.root.print(1)

    
class stack(linkedlist): #push to front, pop from front
    def __init__(self):
        super().__init__()

    def push(self, newval): #make new node for root, push every other node down stack 1
        if self.root:
            newroot = llnode(newval)
            newroot.right = self.root
            self.root.left = newroot
            self.root = newroot
        else:
            self.root = llnode(newval)

    def pop(self): #move stack left by one, and remove + return root, set previous root.right as new root
        if self.root:
            tmp = self.root
            if self.root.right:
                self.root = self.root.right
            else:
                self.root = None
            return tmp
    
        
class queue(linkedlist): #push to end, pop from front
    def __init__(self):
        super().__init__()
    def push(self, newval): #Go to end of list, make new node, set as right element of last element
        run = False
        if self.root:
            itr = self.root
            run = True
        else:
            self.root = llnode(newval)
        while run:
            if itr.right:
                itr = itr.right
            else:
                run = False
                itr.right = llnode(newval)

    def pop(self): #move queue left by one, and remove + return root, set previous root.right as new root
        if self.root:
            tmp = self.root
            if self.root.right:
                self.root = self.root.right
            else:
                self.root = None
            return tmp
        

class advLinkedList(linkedlist):
    def __init__(self):
        super().__init__()
    def indexOfVal_(self, value, node, count):
            if node.value == value:
                return count
            else:
                if node.right:
                    return self.indexOfVal_(value, node.right, count+1)
                else:
                    return -1
    def indexOfVal(self, value): #returns negative number if doesnt exist. If it does, returns index it is at
            if self.root:
                return self.indexOfVal_(value, self.root, 0)
            else:
                return -1

    def valAtIndex(self, index): #Gets index, if a node exists at this index, return its value
            if self.root:
                itr = self.root
            else:
                return
            count = 0
            while count != index:
                if itr.right:
                    itr = itr.right
                    count = count + 1
                else:
                    return
            return itr.value
                    
    def append(self, newval): #adds new llnode with new value to end of list
            if self.root:
                itr = self.root
                while itr.right:
                    itr = itr.right
                itr.right = llnode(newval)
            else:
                self.root = llnode(newval)
            
    def removeVal(self, value): #Finds node with given value, returns it and removes it from list
        if self.root:
            itr = self.root
            if itr.value == value:
                if itr.right:
                    tmp = itr
                    itr.right.left = None
                    self.root = itr.right
                    return tmp
                else:
                    self.root = None
                    return itr
        tmp = itr
        while itr:
            if itr.right:
                if itr.right.value == value:
                    tmp = itr.right
                    if itr.right.right:
                        itr.right.right.left = itr
                        itr.right = itr.right.right
                    else:
                        itr.right = None
                        tmp.right = None
                        tmp.left = None
                    return tmp
                else:
                    itr = itr.right
            else:
                break


def iface():
    print("0). Exit")
    print("1). Stack")
    print("2). Queue")
    print("3). Linked List")

    ans = int(input())
    if ans == 1:
        l = stack()
    elif ans == 2:
        l = queue()
    elif ans == 3:
        l = advLinkedList()
    
    run = True
    if ans == 1 or ans == 2:
        while run:
            l.print()
            print("0). Exit")
            print("1). Push")
            print("2). Pop")
            ans = int(input())
            if ans == 0:
                run = False
            elif ans == 1:
                print("input new value")
                nval = input()
                l.push(nval)
            elif ans == 2:
                tmp = l.pop()
                print("Popped Node with Value: ", tmp.value)
    if ans == 3:
        while run:
            l.print()
            print("0). Exit")
            print("1). Append")
            print("2). Remove node with value")
            print("3). Index of node with value")
            print("4). Value at index")
            ans = int(input())
            if ans == 0:
                run = False
            elif ans == 1:
                print("Input new value")
                l.append(input())
            elif ans == 2:
                print("Input value of node to be removed")
                print("Removed: ",l.removeVal(input()).value)
            elif ans == 3:
                print("Input Value of node")
                print("Index: ",l.indexOfVal(input()))
            elif ans == 4:
                print("Input Index")
                inp = int(input())
                print("List[",inp,"] has Value: ", l.valAtIndex(inp))


if __name__ == "__main__":
    iface()

