#!/usr/bin/python

# GiftExchange for a group of people
# This code has hardcoded the number of people in a list
# Additional persons can be added by 'addUser()' API
# The program could be modified to provide output for as many years 
# of giftexchange by modifying the following two params:
#    numy =  6  #Gifts can be repeated after numy years 
#    yrs = 6    #show results for this number of years

# The program could be automated further to add more persons via command line
# arguments, but due to time constraint it is not implemented below.

# Constraints: Any person should not receive a gift from the same person 
# for 3 years in a row. A person should not gift him/herself


List=["Bob", "Tom", "Dick", "James"] 
def addUser(name):
  List.append(name)

def rotate(l, n):
    newlist = l[n:] + l[:n]
    List = newlist.copy()
    return List

rlists =[]
numy =  6  #Gifts can be repeated after numy years
yrs = 6    #show results for this number of years
def main():
  addUser("Sam")
  addUser("Harry")
  L0=List[:]
  le = len(List)
  numy = le

  for i in range(le-1):
    rlists.append(rotate(L0,i+1))
 
  for year in range(yrs):
      print("      Year= ",year)
      for i in range(le):
        srchlistno = year % (numy-1)

        if i != le-1:
          #print("i, year%numy=", i, year%(numy))
          print ("{} gifts to {}".format( L0[i], rlists[srchlistno][i]))
        else:
          print( "{} gifts to {} ".format(L0[-1], rlists[srchlistno][-1]))
      print(" ")

if __name__ == '__main__':
    main()

