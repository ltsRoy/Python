import pickle

def create_file():
    with open("Book.dat", "wb") as fh:
        lst = [["hi", "bro"], ["JK", "here"]]
        pickle.dump(lst, fh)

def count_rec(author):
    count = 0
    with open("Book.dat", "rb") as fh:
        try:
            while True:
                data = pickle.load(fh)
                for sublist in data:
                    if sublist[1] == author:
                        count += 1
        except EOFError:
            pass
    print(count)

create_file()
count_rec("JK Rowling")
