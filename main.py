# design a program that lets the user enter the total rainfall for each of 12 months into a list

# the program should calculate and display the total rainfall for the year, an the average monthly rainfall, the months with the highest and lowest amounts.

# create a list of months of the year
monthsOfTheYear = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# create an empty list, which will hold each month's amount of rainfall
rainfallByMonth = []

# ask the user to input the amount of rainfall for each month
for month in monthsOfTheYear:
  
    amountOfRainfall = float(input(f"How many inches of rain did we get in California in {month}? "))

    # append the amount entered to the rainfallByMonth list
    rainfallByMonth.append(amountOfRainfall)

# display results
print(f"\nRainfall amounts by month: {rainfallByMonth}")

# create a variable to help us keep track of total yearly rainfall and initialize it to 0
totalYearlyRainfall = 0

# iterate through the rainfallByMonth list and calculate the total rainfall for the year
for amount in rainfallByMonth:
    totalYearlyRainfall = totalYearlyRainfall + amount

# display results
print(f"\nTotal yearly rainfall is {totalYearlyRainfall:,.1f} inches")

# calculate average monthly rainfall and display results
avgMonthlyRainfall = totalYearlyRainfall / len(monthsOfTheYear)
print(f"\nAverage monthly rainfall is {avgMonthlyRainfall:,.1f} inches")

# identify the highest and lowest amounts of rainfall
lowestAmountRainfall = min(rainfallByMonth)
highestAmountRainfall = max(rainfallByMonth)

# identify the indices of the months with the highest and lowest amounts of rainfall
indexHighestAmountRainfall = rainfallByMonth.index(highestAmountRainfall)
indexLowestAmountRainfall = rainfallByMonth.index(lowestAmountRainfall)

# identify the months with the highest and lowest amounts of rainfall
monthHighestAmountRainfall = monthsOfTheYear[indexHighestAmountRainfall]
monthLowestAmountRainfall = monthsOfTheYear[indexLowestAmountRainfall]

# display results
print(f"\nMonth with highest amount of rain: {monthHighestAmountRainfall}")
print(f"Month with lowest amount of rain: {monthLowestAmountRainfall}")