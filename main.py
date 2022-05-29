#Write a program that accepts an integer (n, 0 < n < 10) 
#computes the value of n+nn+nnn. 
#Sample : inpul value n = 5
#Expected Result : 615 (= 5+55+555)

#get User input

while (True):
  number = int(input("Input number (range : 1~9)::"))
  if number>9:
    print ("NUMBER TOO BIG!")
  elif number<=0:
    print("NUMBER TOO SMALL!")
  else:
    answer = number + number*11 + number*111
    print("result is  "+str(answer))
      
  program = input("Continue? Q to quit and Y to continue: ")
  if program=="Q" or program=="q":
    print("goodbye!")
    break
    