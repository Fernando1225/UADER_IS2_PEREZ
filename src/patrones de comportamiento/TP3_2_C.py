class StringIterator:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __reversed__(self):
        return StringIterator(self.string[::-1])

    def __next__(self):
        if self.index < len(self.string):
            char = self.string[self.index]
            self.index += 1
            return char
        else:
            raise StopIteration

def main():
    string = "hello world"
    str_iterator = StringIterator(string)

    # Itera hacia adelante
    for char in str_iterator:
        print(char)
        
    print()
    print('-------- Al reves ---------')
    print()

    # Itera hacia atras
    for char in reversed(str_iterator):
        print(char)
    print()
    

if __name__ == "__main__":
    main()