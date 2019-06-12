
#    WRITE YOUR CODE HERE...
def biggest_guy(x , y , z):
    if (x > y) and (x > z):
     return x
    elif (y > x) and (y > z):
      return y
    else:
     return z
#DO NOT remove lines below here,
#this is designed to test your code.
def test_biggest_guy():
  try:
    assert biggest_guy(1, 3, 2) == 3
    assert biggest_guy(30, 10, 20) == 30
    assert biggest_guy(20, 10, 30) == 30
    assert biggest_guy(2, 1, 9) == 9
    assert biggest_guy('a', 'a', 'b') == 'b' # 'b' is greater than 'a'
 
  except (AssertionError) as e:
    print(e)
    print("Wrong!!")
    return
  
  print("Correct buddy!!!")
#test your code by un-commenting the line(s) below
test_biggest_guy()