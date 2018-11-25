
quote = 'Let it be, let it be, let it be'

result = quote.find('let it')
print("Substring 'let it':", result)

result = quote.find('small')
print("Substring 'small ':", result)

# How to use find()
if  (quote.find('be,') != -1):
  print("Contains substring 'be,'")
else:
  print("Doesn't contain substring")
