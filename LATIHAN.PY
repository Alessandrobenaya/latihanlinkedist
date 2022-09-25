class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None

    def add(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 

    def deleteNode(self, jumlah): 
        temp = self.head 

        if (temp is not None): 
            if (temp.data == jumlah): 
                self.head = temp.next
                temp = None
                return

        while(temp is not None): 
            if temp.data == jumlah: 
                break
            prev = temp 
            temp = temp.next
        if(temp == None): 
            return

        prev.next = temp.next

        temp = None

    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data , end = '  ')
            temp = temp.next


    def deleteNode(self, jumlah):

        temp = self.head

        if (temp is not None):
            if (temp.data == jumlah):
                self.head = temp.next
                temp = None
                return

        while(temp is not None):
            if temp.data == jumlah:
                break
            prev = temp
            temp = temp.next

        if(temp == None):
            return

        prev.next = temp.next

        temp = None


    def removeDuplicates(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        return self.head


myll = LinkedList() 

myll.add("a")
myll.add("b")
myll.add("c")
myll.add("d")
myll.add("f")
myll.add("g")
myll.add("h")
myll.add("i")
myll.add("j")
myll.add("k")
myll.add("l")
myll.add("m")
myll.add("n")
myll.add("n")
myll.add("n")
myll.add("o")

myll.printList() 

#memisahkan
print()
# SOAL NO 1 Menghapus Node berdasarkan Value
myll.deleteNode("a")
# SOAL NO 2 Menghapus value yang duplikat
myll.removeDuplicates()
# SOAL NO 3 Tail to head
print()
myll.printList() 