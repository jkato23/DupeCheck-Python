print("Hello")
numArray = []
for i in range(5):
    numArray.append(int(input("Enter a number to be added to the array to be checked. You will be prompted five times: ")))
uniqueArray = []
dupeCount = 0
for i in numArray:
    if i not in uniqueArray:
        uniqueArray.append(i)
    else:
       dupeCount += 1
if dupeCount == 1:
    print("There is {} duplicate entry in the array.".format(dupeCount))
else:
        print("There are {} duplicate entries in the array.".format(dupeCount))