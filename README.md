Requesting Data:
To request the currency conversion from the microservice, you need to change the first line of your expenses.txt file from a 0 to a 1. Here is an example call:

request_data():
  if lines[0].strip() == '0':
    lines[0] = '1\n'

  with open('expenses.txt', 'w') as outfile:
      outfile.writelines(lines)

Receiving Data:
The data that you request (conversion from dollar to pound) will be updated on the expenses.txt file that was updated. You can retrieve this data just by reading the expenses.txt file and writing the data to the terminal. Here is an example of retrieving the updated data:

read_data():
  with open('expenses.txt', 'r') as infile:
      lines = infile.readlines()
  
  for line in lines[1:]:
      print(line, end='')


