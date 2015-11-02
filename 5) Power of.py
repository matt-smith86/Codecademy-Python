# Prompts user to give base and exponent numbers

base = int(raw_input('Enter base number:'))
exponent = int(raw_input('Enter exponent number:'))

# Function that raises base by exponent and outputs result

def power(base, exponent):
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(base,exponent) 
