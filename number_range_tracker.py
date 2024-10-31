#initialize counts for each range (1-10, 11-20, 21-30, 31-40, 41-50)
#start an infinite loop using while loop to get the number input
#ask the user for input
#make a valid instance for the number input (only digits)
#use if statement to check if the number is whithin the valid range
#adjust the count according to the range
#break the loop if the number is out of range
#print error if the number input is invalid
#print the results

def main():
    counts = [0] * 5

    while true:
        number_input = input("enter a number between 1-50 (or a number outside this range to stop): ")

        if number_input.isdigit():
            num = int(number_input)
            if 1 <= num <= 50:
                counts[(num - 1) // 10] += 1
            else:
                break
            
        else:
            print("error: Invalid number. Try again.")
