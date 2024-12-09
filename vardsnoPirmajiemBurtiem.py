# Take input from the user
vardi = input("Ievadiet četrus vārdus: ")

# Split the input into a list and filter out non-string items
lst = [burts for burts in vardi.split() if burts.isalpha()]

# Initialize an empty result string
iznakums = ""

# Loop through each word and take the first letter
for burts in lst:
    i = burts[0]
    print(i, end='')
