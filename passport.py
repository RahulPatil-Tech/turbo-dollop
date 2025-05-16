'''
Input:

Prithviraj Dajisaheb Chavan

output:

Chavan Prithviraj Dajisaheb

 

Input:

Prithviraj D. Chavan

Output:

Chavan Prithviraj D.

 

Input:

Mukesh Sharma

Output:

Sharma Mukesh

 

Input:

Nitin Agarwal

Output:

Nitin Agarwal

 

Input:

Surojit

Output:

Surojit


'''
class Solution():
    # Take user input
    def __init__(self):
        self.names = input("Enter the names: ")
    def sort_names(self, names):
        names = names.split()
        first_name = names[0]
        middle_name = names[1:-1]
        last_name = names[-1]
        return " ".join([last_name] + [first_name] + middle_name)
    def process_names(self, names):
        return self.sort_names(names)
    def display(self):
        names = self.names
        if len(names.split()) == 1:
            print(names)
        else:
            print(self.process_names(names))
if __name__ == "__main__":
    obj = Solution()
    obj.display()

    
