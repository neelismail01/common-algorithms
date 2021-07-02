class Element():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            counter += 1
            current = current.next
        return None

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter <= position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                counter += 1
                current = current.next
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        current = self.head
        prev = None
        while current:
            if value == current.value and prev == None:
                self.head = current.next
                break
            elif value == current.value:
                prev.next = current.next
                break
            else:
                prev = current
                current = current.next
