dictionary = {
  "name":"John",
  "age":30,
  "cars": [
    { "name":"Ford", "models":[ "Fiesta", "Focus", "Mustang" ] },
    { "name":"BMW", "models":[ "320", "X3", "X5" ] },
    { "name":"Fiat", "models":[ "500", "Panda" ] }
  ]
 }

models = dictionary['cars'][2]['models']
models.remove('Panda')
try:
    print(dictionary['cars'][2]['name']+ ' : ' + dictionary['cars'][2]['models'][1])
except IndexError as identifier:
    print(f"FATAL ERROR: {identifier}")

print(dictionary['cars'][2])

