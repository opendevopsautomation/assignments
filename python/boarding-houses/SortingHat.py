import sys
from sys import stdin
class SortingHat:
    def __init__(self,limit):
        self.limit=limit
        self.dict={'BV':[],
              'AV':[],
              'BNV':[],
              'ANV':[],
              'NA':[]
            }
    def reg(self):
        while True:
            line=input() #Taking input of registered user line by line
            if line=='fin':  # End the registration
                break
            reg=line.split(' ') #Spliting the input for further operations
            bh=''.join(reg[2:]) #Getting the Boaring House & food preference 
            if len(reg[1]) <= 4: #Roll number should be under 4 digits
                roll=int(reg[1]) 
            else:
                print('Enter 4 digit rollnumber')
                continue
            if roll in self.dict[bh]: #Ignore duplicate student registration
                continue
            if len(self.dict[bh])< self.limit: #Add student to Boarding House if it has vacancy
                self.dict[bh].append(roll)
            else:
                self.dict['NA'].append(roll) #If Boarding House fully occupied

    def show(self):
        for i in self.dict.keys():  #Print the detail of Boarding House
            print(i, ":" , self.dict[i])
    


if __name__ == '__main__':
    n=input()
    n=int(n.split(' ')[1])
    limit=n//4 if n > 4 else n #Creating the limit per boarding house
    Hat=SortingHat(limit)
    Hat.reg()
    Hat.show()

