def check_number(number):
     if number > 0:
          return "Positive"
     elif number < 0:
          return "Negative"
     else:
          return "Zero"
     
# Test cases for check_number function
def test_check_number():
     assert check_number(10) == "Positive", "Test case 1 failed"
     assert check_number(-5) == "Negative", "Test case 2 failed"
     assert check_number(0) == "Zero", "Test case 3 failed"
     assert check_number(100) == "Positive", "Test case 4 failed"
     assert check_number(-50) == "Negative", "Test case 5 failed"
     assert check_number(0.5) == "Positive", "Test case 6 failed"
     assert check_number(-0.5) == "Negative", "Test case 7 failed"
     print("All test cases passed!")
num = int(input("Enter a number: "))
print(check_number(num))
test_check_number()