# A classic stack class
class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

# 3.3.4
def parenChecker(string):
    stack = Stack()
    for i in string:
        if i == "(":
            stack.push(i)
        if i == ")":
            if stack.isEmpty():
                return False
            if stack.peek() == "(":
                stack.pop()
            else:
                return False
    if stack.isEmpty():
        return True
    return False
# Test cases
def parenCheckerTest():
    pass

    
# 3.3.5
def main():
    pass

if __name__ == "__main__":
    main()