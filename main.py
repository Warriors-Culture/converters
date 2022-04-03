import converters

print("Press 1: Temp \n"
      "Press 2: Length\n"
      "Press 3: Speed\n"
      "Press 4: Time")
type = input("Type:")

if type == "1":
    print("1st Converter, \n"
          "c: Celsius\n"
          "f: Fahrenheit\n"
          "k: Kelvin")
    tempFirst = input("Type:")
    print("2nd Converter\n"
          "c: Celsius\n"
          "f: Fahrenheit\n"
          "k: Kelvin")
    tempSecond = input("Type:")
    tempNum = int(input("Number:"))
    result = converters.temp(tempFirst, tempSecond, tempNum, True)
    print(f"Result: {result}")


elif type == "2":
    print("1st Converter\n"
          "km: Kilometer\n"
          "m: Meter\n"
          "cm: Centimeter\n"
          "mm: Millimeter\n"
          "nm: Nanometer\n"
          "mi: Mile \n"
          "yd: Yard\n"
          "ft: Foot\n"
          "in: Inch")
    lengthFirst = input("Type:")
    print("1st Converter\n"
          "km: Kilometer\n"
          "m: Meter\n"
          "cm: Centimeter\n"
          "mm: Millimeter\n"
          "nm: Nanometer\n"
          "mi: Mile \n"
          "yd: Yard\n"
          "ft: Foot\n"
          "in: Inch")
    lengthSecond = input("Type:")
    lengthNum = int(input("Number:"))
    result = converters.length(lengthFirst, lengthSecond, lengthNum, True)
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
    result = converters.speed(speedFirst, speedSecond, speedNum, True)
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