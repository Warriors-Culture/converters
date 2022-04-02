import converters

print("Press 1: Temp \n"
      "Press 2: Length\n"
      "Press 3: Speed\n"
      "Press 4: Time")
type = input("Type:")

if type == "1":
    print("1st Converter, \n"
          "Press 1: Celsius\n"
          "Press 2: Fahrenheit\n"
          "Press 3: Kelvin")
    tempFirst = input("Type:")
    print("2nd Converter\n"
          "Press 1: Celsius\n"
          "Press 2: Fahrenheit\n"
          "Press 3: Kelvin")
    tempSecond = input("Type:")
    tempNum = int(input("Number:"))
    result = converters.temp(tempFirst, tempSecond, tempNum)
    print(f"Result: {result}")


elif type == "2":
    print("1st Converter\n"
          "Press 1: Kilometer\n"
          "Press 2: Meter\n"
          "Press 3: Centimeter\n"
          "Press 4: Millimeter\n"
          "Press 5: Nanometer\n"
          "Press 6: Mile \n"
          "Press 7: Yard\n"
          "Press 8: Foot\n"
          "Press 9: Inch")
    lengthFirst = input("Type:")
    print("2nd Converter\n"
          "Press 1: Kilometer\n"
          "Press 2: Meter\n"
          "Press 3: Centimeter\n"
          "Press 4: Millimeter\n"
          "Press 5: Nanometer\n"
          "Press 6: Mile \n"
          "Press 7: Yard\n"
          "Press 8: Foot\n"
          "Press 9: Inch")
    lengthSecond = input("Type:")
    lengthNum = int(input("Number:"))
    result = converters.length(lengthFirst, lengthSecond, lengthNum)
    print(f"Result: {result}")
elif type == "3":
    print("1st Converter\n"
          "Press 1: Miles Per Hour\n"
          "Press 2: Foot Per Second\n"
          "Press 3: Meter Per Second\n"
          "Press 4: Kilometer Per Hour\n"
          "Press 5: Knots")
    speedFirst = input("Type:")
    print("2nd Converter\n"
          "Press 1: Miles Per Hour\n"
          "Press 2: Foot Per Second\n"
          "Press 3: Meter Per Second\n"
          "Press 4: Kilometer Per Hour\n"
          "Press 5: Knots")
    speedSecond = input("Type:")
    speedNum = int(input("Number:"))
    result = converters.temp(speedFirst, speedSecond, speedNum)
    print(f"Result: {result}")
elif type == "4":
    print("1st Converter\n"
          "Press 1: Nanosecond\n"
          "Press 2: Microsecond\n"
          "Press 3: Millisecond\n"
          "Press 4: Second\n"
          "Press 5: Minute\n"
          "Press 6: Hour\n"
          "Press 7: Day\n"
          "Press 8: Week\n"
          "Press 9: Month\n"
          "Press 10: Year\n"
          "Press 11: Decade\n")
    timeFirst = input("Type:")
    print("2nd Converter\n"
          "Press 1: Nanosecond\n"
          "Press 2: Microsecond\n"
          "Press 3: Millisecond\n"
          "Press 4: Second\n"
          "Press 5: Minute\n"
          "Press 6: Hour\n"
          "Press 7: Day\n"
          "Press 8: Week\n"
          "Press 9: Month\n"
          "Press 10: Year\n"
          "Press 11: Decade\n")
    secondFirst = input("Type:")
else:
    print("Error Invalid")