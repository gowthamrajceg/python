def sortAllWord(given_string):
  word_list=given_string.split()
  word_list.sort()
  print("sorted list of words are :") 

  for i in word_list:
    print(i)



str=input("enter a string")
sortAllWord(str)
