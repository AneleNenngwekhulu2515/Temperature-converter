
def converter():
    for temp in temperature:
        if temp.isdigit():
            if 'C' in temperature:
                fahrenheit = (temp * 9/5) + 32
                print(f"Celsius converted to Fahrenheight is : {fahrenheit} F")
            if 'F' in temperature :
                celsius = (temp- 32) * 5/9 
                print(f'Fahrenheit converted to Celsius is : {celsius} C')
            
        elif temp != temp.isdigit:
            print('Cannot convert non numeric numbers')

temperature = input('What is the tempertaure?, either in celsius or fahrenheit ' )
print(converter())