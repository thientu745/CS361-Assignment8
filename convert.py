import time
import re

def convert_dollars_to_pounds(text):
    conversion_rate = 0.8
    def replace_dollars(match):
        amount = float(match.group(1))
        pounds = amount * conversion_rate
        return f"£{pounds:.2f}"
    return re.sub(r'\$(\d+\.?\d*)', replace_dollars, text)

def read_request():
    while True:
        time.sleep(1)
        with open('expenses.txt', 'r') as file:
            lines = file.readlines()
        
        
        if lines[0].strip() == '1':
            
            lines = [convert_dollars_to_pounds(line) for line in lines]
            lines[0] = '0\n'
            with open('expenses.txt', 'w') as file:
                file.writelines(lines)
    
def main():
    read_request()

if __name__ == "__main__":
    main()