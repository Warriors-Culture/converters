def length(type1, type2, num, symbol):
    if type1 == "km" and type2 == "km":
        return str(f"{num}km")
    if type1 == "km" and type2 == "m":
        result = num / 1000
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "km" and type2 == "cm":
        result = num/100000
        if symbol == True:
            return str(f"{result}cm")
        else:
            return str(f"{result}")
    if type1 == "km" and type2 == "mm":
        result = num/1000000
        if symbol == True:
            return str(f"{result}mm")
        else:
            return str(f"{result}")
    if type1 == "km" and type2 == "nm":
        result = num/1000000000000
        if symbol == True:
            return str(f"{result}nm")
        else:
            return str(f"{result}")
    if type1 == "km" and type2 == "mi":
        result = num * 0.6214
        if symbol == True:
            return str(f"{result}mi")
        else:
            return str(f"{result}")
    if type1 == "km" and type2 == "yd":
        result = num * 1093.613298
        if symbol == True:
            return str(f"{result}yd")
        else:
            return str(f"{result}")
    if type1 == "km" and type2 == "ft":
        result = num * 3280.83989
        if symbol == True:
            return str(f"{result}ft")
        else:
            return str(f"{result}")
    if type1 == "km" and type2 == "in":
        result = num * 39370.07874
        if symbol == True:
            return str(f"{result}in")
        else:
            return str(f"{result}")

    # Meter
    if type1 == "m" and type2 == "km":
        result = num * 1000
        if symbol == True:
            return str(f"{result}km")
        else:
            return str(f"{result}")
    if type1 == "m" and type2 == "m":
        result = num
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "m" and type2 == "cm":
        result = num * 100
        if symbol == True:
            return str(f"{result}cm")
        else:
            return str(f"{result}")
    if type1 == "m" and type2 == "mm":
        result = num * 1000
        if symbol == True:
            return str(f"{result}mm")
        else:
            return str(f"{result}")
    if type1 == "m" and type2 == "nm":
        result = num * 1000000000
        if symbol == True:
            return str(f"{result}nm")
        else:
            return str(f"{result}")
    if type1 == "m" and type2 == "mi":
        result = num * 0.00062137
        if symbol == True:
            return str(f"{result}mi")
        else:
            return str(f"{result}")
    if type1 == "m" and type2 == "yd":
        result = num * 1.09361
        if symbol == True:
            return str(f"{result}yd")
        else:
            return str(f"{result}")
    if type1 == "m" and type2 == "ft":
        result = num * 3.28084
        if symbol == True:
            return str(f"{result}ft")
        else:
            return str(f"{result}")
    if type1 == "m" and type2 == "in":
        result = num * 39.37
        if symbol == True:
            return str(f"{result}in")
        else:
            return str(f"{result}")
    # Centimeter
    if type1 == "cm" and type2 == "km":
        result = num / 100000
        if symbol == True:
            return str(f"{result}km")
        else:
            return str(f"{result}")
    if type1 == "cm" and type2 == "m":
        result = num / 100
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "cm" and type2 == "cm":
        result = num
        if symbol == True:
            return str(f"{result}cm")
        else:
            return str(f"{result}")
    if type1 == "cm" and type2 == "mm":
        result = num * 10
        if symbol == True:
            return str(f"{result}mm")
        else:
            return str(f"{result}")
    if type1 == "cm" and type2 == "nm":
        result = num * 10000000
        if symbol == True:
            return str(f"{result}nm")
        else:
            return str(f"{result}")
    if type1 == "cm" and type2 == "mi":
        result = num / 160934
        if symbol == True:
            return str(f"{result}mi")
        else:
            return str(f"{result}")
    if type1 == "cm" and type2 == "yd":
        result = num / 91.44
        if symbol == True:
            return str(f"{result}yd")
        else:
            return str(f"{result}")
    if type1 == "cm" and type2 == "ft":
        result = num / 30.48
        if symbol == True:
            return str(f"{result}ft")
        else:
            return str(f"{result}")
    if type1 == "cm" and type2 == "in":
        result = num / 2.54
        if symbol == True:
            return str(f"{result}in")
        else:
            return str(f"{result}")
    # Millimeter
    if type1 == "mm" and type2 == "km":
        result = num/1000000
        if symbol == True:
            return str(f"{result}km")
        else:
            return str(f"{result}")
    if type1 == "mm" and type2 == "m":
        result = num/1000
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "mm" and type2 == "cm":
        result = num / 10
        if symbol == True:
            return str(f"{result}cm")
        else:
            return str(f"{result}")
    if type1 == "mm" and type2 == "mm":
        result = num
        if symbol == True:
            return str(f"{result}mm")
        else:
            return str(f"{result}")
    if type1 == "mm" and type2 == "nm":
        result = num * 1000000
        if symbol == True:
            return str(f"{result}nm")
        else:
            return str(f"{result}")
    if type1 == "mm" and type2 == "mi":
        result = num / 1609000
        if symbol == True:
            return str(f"{result}mi")
        else:
            return str(f"{result}")
    if type1 == "mm" and type2 == "yd":
        result = num / 914
        if symbol == True:
            return str(f"{result}yd")
        else:
            return str(f"{result}")
    if type1 == "mm" and type2 == "ft":
        result = num / 305
        if symbol == True:
            return str(f"{result}ft")
        else:
            return str(f"{result}")
    if type1 == "mm" and type2 == "in":
        result = num / 25.4
        if symbol == True:
            return str(f"{result}in")
        else:
            return str(f"{result}")
    # Nanometer
    if type1 == "nm" and type2 == "km":
        result = num/1000000000000
        if symbol == True:
            return str(f"{result}km")
        else:
            return str(f"{result}")
    if type1 == "nm" and type2 == "m":
        result = num/1000000000
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "nm" and type2 == "cm":
        result = num / 10000000
        if symbol == True:
            return str(f"{result}cm")
        else:
            return str(f"{result}")
    if type1 == "nm" and type2 == "mm":
        result = num / 1000000
        if symbol == True:
            return str(f"{result}mm")
        else:
            return str(f"{result}")
    if type1 == "nm" and type2 == "nm":
        result = num
        if symbol == True:
            return str(f"{result}nm")
        else:
            return str(f"{result}")
    if type1 == "nm" and type2 == "mi":
        result = num / 1609000000000
        if symbol == True:
            return str(f"{result}mi")
        else:
            return str(f"{result}")
    if type1 == "nm" and type2 == "yd":
        result = num / 914400000
        if symbol == True:
            return str(f"{result}yd")
        else:
            return str(f"{result}")
    if type1 == "nm" and type2 == "ft":
        result = num / 304800000
        if symbol == True:
            return str(f"{result}ft")
        else:
            return str(f"{result}")
    if type1 == "nm" and type2 == "in":
        result = num / 25400000
        if symbol == True:
            return str(f"{result}in")
        else:
            return str(f"{result}")
    # Mile
    if type1 == "mi" and type2 == "km":
        result = num*1.609
        if symbol == True:
            return str(f"{result}km")
        else:
            return str(f"{result}")
    if type1 == "mi" and type2 == "m":
        result = num*1609
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "mi" and type2 == "cm":
        result = num * 160934
        if symbol == True:
            return str(f"{result}cm")
        else:
            return str(f"{result}")
    if type1 == "mi" and type2 == "mm":
        result = num * 1609000
        if symbol == True:
            return str(f"{result}mm")
        else:
            return str(f"{result}")
    if type1 == "mi" and type2 == "nm":
        result = num * 1609000000000
        if symbol == True:
            return str(f"{result}nm")
        else:
            return str(f"{result}")
    if type1 == "mi" and type2 == "mi":
        result = num
        if symbol == True:
            return str(f"{result}mi")
        else:
            return str(f"{result}")
    if type1 == "mi" and type2 == "yd":
        result = num * 1764
        if symbol == True:
            return str(f"{result}yd")
        else:
            return str(f"{result}")
    if type1 == "mi" and type2 == "ft":
        result = num * 5280
        if symbol == True:
            return str(f"{result}ft")
        else:
            return str(f"{result}")
    if type1 == "mi" and type2 == "in":
        result = num * 63360
        if symbol == True:
            return str(f"{result}in")
        else:
            return str(f"{result}")
    # Yard
    if type1 == "yd" and type2 == "km":
        result = num/1094
        if symbol == True:
            return str(f"{result}km")
        else:
            return str(f"{result}")
    if type1 == "yd" and type2 == "m":
        result = num/1.094
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "yd" and type2 == "cm":
        result = num * 91.44
        if symbol == True:
            return str(f"{result}cm")
        else:
            return str(f"{result}")
    if type1 == "yd" and type2 == "mm":
        result = num * 914
        if symbol == True:
            return str(f"{result}mm")
        else:
            return str(f"{result}")
    if type1 == "yd" and type2 == "nm":
        result = num * 914400000
        if symbol == True:
            return str(f"{result}nm")
        else:
            return str(f"{result}")
    if type1 == "yd" and type2 == "mi":
        result = num / 1760
        if symbol == True:
            return str(f"{result}mi")
        else:
            return str(f"{result}")
    if type1 == "yd" and type2 == "yd":
        result = num
        if symbol == True:
            return str(f"{result}yd")
        else:
            return str(f"{result}")
    if type1 == "yd" and type2 == "ft":
        result = num * 3
        if symbol == True:
            return str(f"{result}ft")
        else:
            return str(f"{result}")
    if type1 == "yd" and type2 == "in":
        result = num * 36
        if symbol == True:
            return str(f"{result}in")
        else:
            return str(f"{result}")
        # Foot
    if type1 == "ft" and type2 == "km":
        result = num / 3281
        if symbol == True:
            return str(f"{result}km")
        else:
            return str(f"{result}")
    if type1 == "ft" and type2 == "m":
        result = num / 3.281
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "ft" and type2 == "cm":
        result = num * 30.48
        if symbol == True:
            return str(f"{result}cm")
        else:
            return str(f"{result}")
    if type1 == "ft" and type2 == "mm":
        result = num * 305
        if symbol == True:
            return str(f"{result}mm")
        else:
            return str(f"{result}")
    if type1 == "ft" and type2 == "nm":
        result = num * 304800000
        if symbol == True:
            return str(f"{result}nm")
        else:
            return str(f"{result}")
    if type1 == "ft" and type2 == "mi":
        result = num / 5280
        if symbol == True:
            return str(f"{result}mi")
        else:
            return str(f"{result}")
    if type1 == "ft" and type2 == "yd":
        result = num / 3
        if symbol == True:
            return str(f"{result}yd")
        else:
            return str(f"{result}")
    if type1 == "ft" and type2 == "ft":
        result = num
        if symbol == True:
            return str(f"{result}ft")
        else:
            return str(f"{result}")
    if type1 == "ft" and type2 == "in":
        result = num * 12
        if symbol == True:
            return str(f"{result}in")
        else:
            return str(f"{result}")
        # Inch
    if type1 == "in" and type2 == "km":
        result = num / 39370
        if symbol == True:
            return str(f"{result}km")
        else:
            return str(f"{result}")
    if type1 == "in" and type2 == "m":
        result = num / 39.37
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "in" and type2 == "cm":
        result = num * 2.54
        if symbol == True:
            return str(f"{result}cm")
        else:
            return str(f"{result}")
    if type1 == "in" and type2 == "mm":
        result = num * 25.4
        if symbol == True:
            return str(f"{result}mm")
        else:
            return str(f"{result}")
    if type1 == "in" and type2 == "nm":
        result = num * 25400000
        if symbol == True:
            return str(f"{result}nm")
        else:
            return str(f"{result}")
    if type1 == "in" and type2 == "mi":
        result = num / 63360
        if symbol == True:
            return str(f"{result}mi")
        else:
            return str(f"{result}")
    if type1 == "in" and type2 == "yd":
        result = num / 36
        if symbol == True:
            return str(f"{result}yd")
        else:
            return str(f"{result}")
    if type1 == "in" and type2 == "ft":
        result = num / 12
        if symbol == True:
            return str(f"{result}ft")
        else:
            return str(f"{result}")
    if type1 == "in" and type2 == "in":
        result = num
        if symbol == True:
            return str(f"{result}in")
        else:
            return str(f"{result}")


def temp(type1, type2, num, symbol):
    if type1 == "c" and type2 == "c":
        result = num
        if symbol == True:
            return str(f"{result}°C")
        else:
            return str(f"{result}")
    if type1 == "c" and type2 == "f":
        result = (num*9/5) + 32
        if symbol == True:
            return str(f"{num}°F")
        else:
            return str(f"{num}")
    if type1 == "c" and type2 == "k":
        result = num + 273.15
        if symbol == True:
            return str(f"{num}°K")
        else:
            return str(f"{num}")
    if type1 == "f" and type2 == "f":
        result = num
        if symbol == True:
            return str(f"{num}°F")
        else:
            return str(f"{num}")
    if type1 == "f" and type2 == "c":
        result = (num-32)*5/9
        if symbol == True:
            return str(f"{num}°C")
        else:
            return str(f"{num}")
    if type1 == "f" and type2 == "k":
        result = (num - 32)*5 / 9 + 273.15
        if symbol == True:
            return str(f"{num}°K")
        else:
            return str(f"{num}")
    if type1 == "k" and type2 == "k":
        result = num
        if symbol == True:
            return str(f"{num}°K")
        else:
            return str(f"{num}")
    if type1 == "k" and type2 == "f":
        result = (num + 32) / 5 * 9 - 273.15
        if symbol == True:
            return str(f"{num}°F")
        else:
            return str(f"{num}")
    if type1 == "k" and type2 == "c":
        result = num - 273.15
        if symbol == True:
            return str(f"{num}°C")
        else:
            return str(f"{num}")

def speed(type1,type2,num, symbol):
    if type1 == "mph" and type2 == "mph":
        result = num
        if symbol == True:
            return str(f"{result}mph")
        else:
            return str(f"{result}")
    if type1 == "mph" and type2 == "fts":
        result = num * 1.467
        if symbol == True:
            return str(f"{result}ft/s")
        else:
            return str(f"{result}")
    if type1 == "mph" and type2 == "ms":
        result = num / 2.237
        if symbol == True:
            return str(f"{result}m/s")
        else:
            return str(f"{result}")
    if type1 == "mph" and type2 == "kmh":
        result = num * 1.609
        if symbol == True:
            return str(f"{result}km/h")
        else:
            return str(f"{result}")
    if type1 == "mph" and type2 == "kn":
        result = num / 1.151
        if symbol == True:
            return str(f"{result}kn")
        else:
            return str(f"{result}")
    # FPS
    if type1 == "fts" and type2 == "mph":
        result = num / 1.467
        if symbol == True:
            return str(f"{result}mph")
        else:
            return str(f"{result}")
    if type1 == "fts" and type2 == "fts":
        result = num
        if symbol == True:
            return str(f"{result}ft/s")
        else:
            return str(f"{result}")
    if type1 == "fts" and type2 == "ms":
        result = num / 3.281
        if symbol == True:
            return str(f"{result}m/s")
        else:
            return str(f"{result}")
    if type1 == "fts" and type2 == "kmh":
        result = num * 1.097
        if symbol == True:
            return str(f"{result}km/h")
        else:
            return str(f"{result}")
    if type1 == "fts" and type2 == "kn":
        result = num / 1.688
        if symbol == True:
            return str(f"{result}kn")
        else:
            return str(f"{result}")
    #M S
    if type1 == "ms" and type2 == "mph":
        result = num * 2.237
        if symbol == True:
            return str(f"{result}mph")
        else:
            return str(f"{result}")
    if type1 == "ms" and type2 == "fts":
        result = num * 3.281
        if symbol == True:
            return str(f"{result}ft/s")
        else:
            return str(f"{result}")
    if type1 == "ms" and type2 == "ms":
        result = num
        if symbol == True:
            return str(f"{result}m/s")
        else:
            return str(f"{result}")
    if type1 == "ms" and type2 == "kmh":
        result = num * 3.6
        if symbol == True:
            return str(f"{result}km/h")
        else:
            return str(f"{result}")
    if type1 == "ms" and type2 == "kn":
        result = num / 1.944
        if symbol == True:
            return str(f"{result}kn")
        else:
            return str(f"{result}")
    #KMS
    if type1 == "kmh" and type2 == "mph":
        result = num / 1.609
        if symbol == True:
            return str(f"{result}mph")
        else:
            return str(f"{result}")
    if type1 == "kmh" and type2 == "fts":
        result = num / 1.097
        if symbol == True:
            return str(f"{result}ft/s")
        else:
            return str(f"{result}")
    if type1 == "kmh" and type2 == "ms":
        result = num / 3.6
        if symbol == True:
            return str(f"{result}m/s")
        else:
            return str(f"{result}")
    if type1 == "kmh" and type2 == "kmh":
        result = num
        if symbol == True:
            return str(f"{result}km/h")
        else:
            return str(f"{result}")
    if type1 == "kmh" and type2 == "kn":
        result = num / 1.852
        if symbol == True:
            return str(f"{result}kn")
        else:
            return str(f"{result}")
    #Kn
    if type1 == "kn" and type2 == "mph":
        result = num * 1.151
        if symbol == True:
            return str(f"{result}mph")
        else:
            return str(f"{result}")
    if type1 == "kn" and type2 == "fts":
        result = num * 1.688
        if symbol == True:
            return str(f"{result}ft/s")
        else:
            return str(f"{result}")
    if type1 == "kn" and type2 == "ms":
        result = num / 1.944
        if symbol == True:
            return str(f"{result}m/s")
        else:
            return str(f"{result}")
    if type1 == "kn" and type2 == "kmh":
        result = num * 1.852
        if symbol == True:
            return str(f"{result}km/h")
        else:
            return str(f"{result}")
    if type1 == "kn" and type2 == "kn":
        result = num
        if symbol == True:
            return str(f"{result}kn")
        else:
            return str(f"{result}")





