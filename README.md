Requesting Data:
To request the currency conversion from the microservice, you need to change the first line of your expenses.txt file from a 0 to a 1. Here is an example call:

    # Existing list of expenses that should exist in your program
    expenses = [
        {"Expense": "Car", "Amount": 20000.00},
        {"Expense": "Rent", "Amount": 2000.00}
    ]

    # Function to initialize data to be converted in a text file
    initialize_data(expenses):

      # Open a file in write mode
      with open('expenses.txt', 'w') as file:
        # Write the number 0
        file.write("0\n")
    
      # Write each expense in the specified format
      for expense in expenses:
          file.write(f"Expense: {expense['Expense']}\n")
          file.write(f"Amount: ${expense['Amount']:.2f}\n")

    # Function to communicate with the microservice to start the conversion process
    request_data():

      # Open the file in read mode and read all lines
      with open('expenses.txt', 'r') as file:
          lines = file.readlines()
      
      # Modify the first line
      lines[0] = '1\n'
      
      # Open the file in write mode and write the modified lines back to the file
      with open('expenses.txt', 'w') as file:
          file.writelines(lines)

Receiving Data:
The data that you request (conversion from dollar to pound) will be updated on the expenses.txt file that was updated. You can retrieve this data just by reading the expenses.txt file and writing the data to the terminal. Here is an example of retrieving the updated data:

    read_data():
      with open('expenses.txt', 'r') as infile:
          lines = infile.readlines()
      
      for line in lines[1:]:
          print(line, end='')


