# Problem 3
HOURS_IN_DAY = 24
MINS_IN_HOUR = 60
SECS_IN_MINUTE = 60

print(HOURS_IN_DAY * MINS_IN_HOUR * SECS_IN_MINUTE)


# Problem 4
DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINS_IN_HOUR = 60
SECS_IN_MINUTE = 60

print(DAYS_IN_YEAR * HOURS_IN_DAY * MINS_IN_HOUR * SECS_IN_MINUTE)


# Problem 5
newPlanetName = input("Enter the name of the New Planet!")
numberOfDaysOnThatPlanet = int(input("Enter the number of days of that new planet in Earth's days!"))

HOURS_IN_DAY = 24
MINS_IN_HOUR = 60
SECS_IN_MINUTE = 60

print(f"One Year at {newPlanetName} planet equals to {numberOfDaysOnThatPlanet} days on Earth!")
print(f"One Year at {newPlanetName} is {numberOfDaysOnThatPlanet * HOURS_IN_DAY * MINS_IN_HOUR * SECS_IN_MINUTE} seconds!")


# Problem 6
LEGAL_AGE_IN_MONTHS = 216

userAgeInMonths = int(input("Enter your age in months!"))

if userAgeInMonths > LEGAL_AGE_IN_MONTHS:
    print(True)
else:
    print(False)