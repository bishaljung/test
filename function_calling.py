
import math
def main():

  display_menu()
  choice = 0
  choice = int(input("enter the valid number from the choose table:"))

  if choice == 1:
      area_circle()

  elif choice == 2:
      area_rectangle()

  elif choice == 3:
      exit()
  else:
      print("invalid choice")



def display_menu():
      print("1) for area of circle \n 2) for area of rectangle \n 3) for exit")
def area_circle():
      radious = int(input("enter the radious of circle"))
      print("the area of circle is: "+ str(math.pi*(radious**2)))
      main()
def area_rectangle():
     length = int(input("enter the length"))
     width= int(input("enter the breadth"))
     print("The area is"+ str((width * length)))
     main()                      

main()







