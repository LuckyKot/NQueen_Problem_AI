num_of_queens=22

#Class to have the board as a variable and some helper methods
class Table:
    def __init__(self, n):
        self.table=[]
        for i in range (n):
            self.table.append([])
            for j in range (n):
                self.table[i].append(0)
    
    def print_table(self): 
        for i in range(len(self.table)):
            print(self.table[i])
    
    def to_string(self):
        temp=''
        for i in self.table:
            for j in i:
                temp = temp+str(j)
        return temp
    

#Constraints checking function, takes the board and coordinates to check
def check_position(table, qX, qY):
    for i in range(len(table.table)):
        if table.table[i][qY] == 1:
            return False
    
    i=qX
    j=qY
    while(i>=0 and j>=0):
        if table.table[i][j]==1:
            return False
        i=i-1
        j=j-1
    
    i=qX
    j=qY
    while(i>=0 and j<=len(table.table)-1):
        if table.table[i][j]==1:
            return False
        i=i-1
        j=j+1
    
    i=qX
    j=qY
    while(i<=len(table.table)-1 and j<=len(table.table)-1):
        if table.table[i][j]==1:
            return False
        i=i+1
        j=j+1
    
    i=qX
    j=qY
    while(i<=(len(table.table)-1) and j>=0):
        if table.table[i][j]==1:
            return False
        i=i+1
        j=j-1
    
    return True

unique_solutions = []

#backtracking search function that calls recrsive function
#Most of the following code is basically translated pseudocode provided in the assignment
def backtracking_search(table):
    return recursive_backtracking(0,table)

def recursive_backtracking(n,table):
    #base case checking solution
    if n == len(table.table):
        #translate to 1d string for easier comparisson with previous and future solutions
        temp=table.to_string()
        #checking if solution is unique
        if temp not in unique_solutions:
            #if unique -> add it to the list in form of 1d string
            unique_solutions.append(temp)
            #print this unique solution
            table.print_table()
            for i in range(len(table.table)):
                for j in range(len(table.table)):
                    if table.table[i][j]==1:
                        print('(',str(i),',',str(j),')',end='',sep='')
            print('\n')
        #if we have required 4 solution - exit the function
        if len(unique_solutions)==4:
            return True
    
    #the main recursive part just like in pseudocode
    #takes n as row and places one queen on every row checking the constraints
    #then recursively calls recursivebacktracking
    #if solution fails sets 0 back
    for i in range(len(table.table)):
        if check_position(table,n,i):
            table.table[n][i]=1
            if recursive_backtracking(n+1,table):
                return True
            table.table[n][i]=0

    return False


def print_result(n):
    #initializing table
    table = Table(n)
    #plugging it in the search
    backtracking_search(table)


print_result(num_of_queens)
