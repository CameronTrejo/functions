# Get information from the user about conversion
# TODO User input validation
userInput = input('What is the number: ')
print('Your number is:', userInput) # TODO remove for prod
userNumber = float(userInput) 

# Perform the conversion
# Convert in to mm 25.4 in every 1 in

# Convert from in to mm (userNumber * 25.4) (1 * 25.4) = 25.4 mm
userAnswer = userNumber * 25.4

# Convert from mm to in (userNumber/ 25.4 ) 1/25.4 = 0.394
userAnswer = userNumber/ 25.4

# Print that information out. The answer
print('The answer is:', userAnswer)