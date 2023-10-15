# Create a Library with no_of_books & books as two instance variables.
# Write a program from Library class to add, show, print all books, no of books.
# Show that after program ends books data is not persistant

class Library:
    def __init__(self):
        self.booklist = [];
        print("Welcome to Library\n");
        print("You can Add books to our library\nSee books available");

    def addBook(self,*book):
        self.booklist.append(list(book));

    def showBooks(self):
        if(not len(self.booklist)<=0):
            print("The books available are: \n");
            print(f"Sr No\t['Name', 'Author', 'Year']");
            for i in range(0,len(self.booklist)):
                print(f"{i+1}\t{self.booklist[i]}");
        else:
            print("\nCurrently no book is available\nAdd a Book Name(author, year etc are optional)");

    def noOfBooks(self):
        print(f"\nThe number of Books available are: {len(self.booklist)}");


obj = Library();
obj.showBooks();
obj.addBook("Glory Of India","Amit","2012");
obj.addBook("Discovery","Prajwal Chavhan","2017");
obj.addBook("Lets go India","Rahul Chaurasiya","2002");
obj.addBook("Gold","Digambar","2006");

obj.showBooks();
obj.noOfBooks();