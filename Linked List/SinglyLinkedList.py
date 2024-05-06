""" Singly Linked List"""


class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            # self.insert_at_start(data)
            self.start = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next.item != data:
                    temp = temp.next
                temp.next = temp.next.next

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
        print()

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


# driver Code
mylist = SLL()
mylist.insert_at_start(25)
mylist.insert_at_start(10)
mylist.insert_at_last(40)
mylist.insert_at_last(50)
mylist.print_list()  # 10 25 40 50

mylist.insert_after(mylist.search(40), 45)
mylist.print_list()  # 10 25 40 45 50
mylist.delete_first()  # 25 40 45 50
mylist.delete_last()  # 25 40 45

mylist.delete_item(45)  # 25 40
# mylist.print_list()
print("printing using iterator ....")
for x in mylist:
    print(x)
