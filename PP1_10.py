def q1(): 
  #Write Assignment code here
  num1 = float(input("Input a number: "))
  sqrt_result = math.sqrt(num1)
  print("Square root:", sqrt_result)

def q2(): 
  #Write Assignment code here
  num2 = float(input("Input a number: "))
  int_sqrt_result = int(math.sqrt(num2))
  print("Integer square root:", int_sqrt_result)

def q3(): 
  #Write Assignment code here
  num3 = float(input("Input a number: "))
  round_down_result = math.floor(num3)
  print("Rounded down:", round_down_result)

def q4(): 
  #Write Assignment code here
  num4 = float(input("Input a number: "))
  round_up_result = math.ceil(num4)
  print("Rounded up:", round_up_result)

def q5(): 
  #Write Assignment code here
  num5 = float(input("Input a number: "))
  num6 = float(input("Input another number: "))
  result = (num5 * num6) // 3
  print("Final rounded down result:", math.floor(result))


#Do not alter the following code
#Comment out the following code when running your tests

#q1()
#q2()
#q3()
#q4()
#q5()
