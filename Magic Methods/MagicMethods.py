class Book:
    def __init__(self, title, author, num_of_pages):
        self.title=title
        self.author=author
        self.num_of_pages=num_of_pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    # to compare the objects 
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self,other):
        return self.num_of_pages < other.num_of_pages

    def __add__(self,other):
        return self.num_of_pages+other.num_of_pages
    
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self,key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_of_pages':
            return self.num_of_pages
        return None
    

book1 = Book("The Habbit","J.R.R Tolkien",310)
book2 = Book("The Habbit","J.R.R Tolkien",320)
# book2 = Book("C++ Programming","James chedwick",400)
book3 = Book("Java Programming","C.S Lewis",350)

print(book1)
print(book2)
print(book3)

print(book1 == book2)  #after defining the __eq__ method now it returns true.
print(book2 < book3)   #after defining the __lt__ method now it returns true.
print(book1 + book2)   #after defining the __add__ method now it returns the sum of pages of book1 and book2

print("Habbit" in book1) #after defining the __contains__ method now it prints True
print(book1['title'])    #after defining the __getitem__ method now it returns corresponding value of key.
