starting_number = int(input('Enter Number of Organisms: '))
daily_increase = int(input('Enter Daily Increase: ')) / 100
total_days = int(input('Enter Days Left to Multiply: '))
first = True

print('Day Approximate','  ','  Population')
print('------------------------------')

for total_days in range (starting_number, total_days + 1):
    if first:
        print(1 ,'\t\t\t\t\t', starting_number)
        first = False
    add = starting_number * daily_increase
    starting_number = starting_number + add
    print(total_days, '\t\t\t\t\t', starting_number)
