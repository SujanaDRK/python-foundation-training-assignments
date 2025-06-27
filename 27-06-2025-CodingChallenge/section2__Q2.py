# Section 2: Data Structures & Algorithms

def eval_postfix(expr):
    stack = []
    for token in expr:
        if token.isdigit():
            
            stack.append(int(token))
        else:
            # pop two operands (b then a)
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
              
                stack.append(a // b)
    
    return stack[0]

# Node class for linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list with append, display, and reverse
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        print(" -> ".join(values))

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

def main():
    # Part a) Evaluate the example '231*+9-'
    expr = "231*+9-"
    result = eval_postfix(expr)
    print(f"Postfix expression {expr} evaluates to: {result}")

    # Part b) Demonstrate linked list
    print("\nCreating linked list with values 1,2,3,4,5")
    ll = LinkedList()
    for i in [1,2,3,4,5]:
        ll.append(i)

    print("Original list:")
    ll.display()

    print("Reversing list...")
    ll.reverse()

    print("Reversed list:")
    ll.display()

if __name__ == "__main__":
    main()
