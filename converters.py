def length(type1, type2, num, symbol):
    if type1 == "km" and type2 == "km":
        return str(f"{num}km")
    if type1 == "km" and type2 == "m":
        result = num * 1000
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "km" and type2 == "cm":
        result = num * 100000
        if symbol == True:
            return str(f"{result}cm")
        else:
            return str(f"{result}")
    if type1 == "km" and type2 == "mm":
        result = num * 1000000
        if symbol == True:
            return str(f"{result}mm")
        else:
            return str(f"{result}")
    if type1 == "km" and type2 == "nm":
        result = num * 1000000000000
        if symbol == True:
            return str(f"{result}nm")
        else:
            return str(f"{result}")
    if type1 == "km" and type2 == "mi":
        result = num / 1.609
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
        result = num / 1000
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
    else:
        return("Invalid")

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
    else:
        return("Invalid")

def speed(type1, type2, num, symbol):
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
    else:
        return("Invalid")

def time(type1, type2, num, symbol):
    #MS
    if type1 == "ms" and type2 == "ms":
        result = num
        if symbol == True:
            return str(f"{result}ms")
        else:
            return str(f"{result}")
    if type1 == "ms" and type2 == "s":
        result = num / 1000
        if symbol == True:
            return str(f"{result}s")
        else:
            return str(f"{result}")
    if type1 == "ms" and type2 == "min":
        result = num / 60000
        if symbol == True:
            return str(f"{result}min")
        else:
            return str(f"{result}")
    if type1 == "ms" and type2 == "h":
        result = num / 3600000
        if symbol == True:
            return str(f"{result}h")
        else:
            return str(f"{result}")
    if type1 == "ms" and type2 == "d":
        result = num / 86400000
        if symbol == True:
            return str(f"{result}d")
        else:
            return str(f"{result}")
    if type1 == "ms" and type2 == "w":
        result = num / 604800000
        if symbol == True:
            return str(f"{result}w")
        else:
            return str(f"{result}")
    if type1 == "ms" and type2 == "m":
        result = num / 2628000000
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "ms" and type2 == "y":
        result = num / 31540000000
        if symbol == True:
            return str(f"{result}y")
        else:
            return str(f"{result}")
    if type1 == "ms" and type2 == "dec":
        result = num / 315400000000
        if symbol == True:
            return str(f"{result}dec")
        else:
            return str(f"{result}")
    if type1 == "ms" and type2 == "dec":
        result = num / 3154000000000
        if symbol == True:
            return str(f"{result}dec")
        else:
            return str(f"{result}")

    #S
    if type1 == "s" and type2 == "ms":
        result = num * 1000
        if symbol == True:
            return str(f"{result}ms")
        else:
            return str(f"{result}")
    if type1 == "s" and type2 == "s":
        result = num
        if symbol == True:
            return str(f"{result}s")
        else:
            return str(f"{result}")
    if type1 == "s" and type2 == "min":
        result = num / 60
        if symbol == True:
            return str(f"{result}min")
        else:
            return str(f"{result}")
    if type1 == "s" and type2 == "h":
        result = num / 3600
        if symbol == True:
            return str(f"{result}h")
        else:
            return str(f"{result}")
    if type1 == "s" and type2 == "d":
        result = num / 86400
        if symbol == True:
            return str(f"{result}d")
        else:
            return str(f"{result}")
    if type1 == "s" and type2 == "w":
        result = num / 604800
        if symbol == True:
            return str(f"{result}w")
        else:
            return str(f"{result}")
    if type1 == "s" and type2 == "m":
        result = num / 2628000
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "s" and type2 == "y":
        result = num / 31540000
        if symbol == True:
            return str(f"{result}y")
        else:
            return str(f"{result}")
    if type1 == "s" and type2 == "dec":
        result = num / 315400000
        if symbol == True:
            return str(f"{result}dec")
        else:
            return str(f"{result}")
    if type1 == "s" and type2 == "dec":
        result = num / 3154000000
        if symbol == True:
            return str(f"{result}dec")
        else:
            return str(f"{result}")
    # M
    if type1 == "min" and type2 == "ms":
        result = num * 60000
        if symbol == True:
            return str(f"{result}ms")
        else:
            return str(f"{result}")
    if type1 == "min" and type2 == "s":
        result = num * 60
        if symbol == True:
            return str(f"{result}s")
        else:
            return str(f"{result}")
    if type1 == "min" and type2 == "min":
        result = num
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "min" and type2 == "h":
        result = num / 60
        if symbol == True:
            return str(f"{result}h")
        else:
            return str(f"{result}")
    if type1 == "min" and type2 == "d":
        result = num / 1440
        if symbol == True:
            return str(f"{result}d")
        else:
            return str(f"{result}")
    if type1 == "min" and type2 == "w":
        result = num / 10080
        if symbol == True:
            return str(f"{result}w")
        else:
            return str(f"{result}")
    if type1 == "min" and type2 == "m":
        result = num / 43800
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "min" and type2 == "y":
        result = num / 525600
        if symbol == True:
            return str(f"{result}y")
        else:
            return str(f"{result}")
    if type1 == "min" and type2 == "dec":
        result = num / 5256000
        if symbol == True:
            return str(f"{result}dec")
        else:
            return str(f"{result}")
    if type1 == "min" and type2 == "c":
        result = num / 52560000
        if symbol == True:
            return str(f"{result}c")
        else:
            return str(f"{result}")

    # H
    if type1 == "h" and type2 == "ms":
        result = num * 3600000
        if symbol == True:
            return str(f"{result}ms")
        else:
            return str(f"{result}")
    if type1 == "h" and type2 == "s":
        result = num * 3600
        if symbol == True:
            return str(f"{result}s")
        else:
            return str(f"{result}")
    if type1 == "h" and type2 == "min":
        result = num * 60
        if symbol == True:
            return str(f"{result}min")
        else:
            return str(f"{result}")
    if type1 == "h" and type2 == "h":
        result = num
        if symbol == True:
            return str(f"{result}h")
        else:
            return str(f"{result}")
    if type1 == "h" and type2 == "d":
        result = num / 24
        if symbol == True:
            return str(f"{result}d")
        else:
            return str(f"{result}")
    if type1 == "h" and type2 == "w":
        result = num / 168
        if symbol == True:
            return str(f"{result}w")
        else:
            return str(f"{result}")
    if type1 == "h" and type2 == "m":
        result = num / 730
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "h" and type2 == "y":
        result = num / 8760
        if symbol == True:
            return str(f"{result}y")
        else:
            return str(f"{result}")
    if type1 == "h" and type2 == "dec":
        result = num / 87600
        if symbol == True:
            return str(f"{result}dec")
        else:
            return str(f"{result}")
    if type1 == "h" and type2 == "c":
        result = num / 876000
        if symbol == True:
            return str(f"{result}c")
        else:
            return str(f"{result}")


    # D
    if type1 == "d" and type2 == "ms":
        result = num * 86400000
        if symbol == True:
            return str(f"{result}ms")
        else:
            return str(f"{result}")
    if type1 == "d" and type2 == "s":
        result = num * 86400
        if symbol == True:
            return str(f"{result}s")
        else:
            return str(f"{result}")
    if type1 == "d" and type2 == "min":
        result = num * 1440
        if symbol == True:
            return str(f"{result}min")
        else:
            return str(f"{result}")
    if type1 == "d" and type2 == "h":
        result = num * 24
        if symbol == True:
            return str(f"{result}h")
        else:
            return str(f"{result}")
    if type1 == "d" and type2 == "d":
        result = num
        if symbol == True:
            return str(f"{result}d")
        else:
            return str(f"{result}")
    if type1 == "d" and type2 == "w":
        result = num / 7
        if symbol == True:
            return str(f"{result}w")
        else:
            return str(f"{result}")
    if type1 == "d" and type2 == "m":
        result = num / 30.417
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "d" and type2 == "y":
        result = num / 365
        if symbol == True:
            return str(f"{result}y")
        else:
            return str(f"{result}")
    if type1 == "d" and type2 == "dec":
        result = num / 3650
        if symbol == True:
            return str(f"{result}dec")
        else:
            return str(f"{result}")
    if type1 == "d" and type2 == "c":
        result = num / 36500
        if symbol == True:
            return str(f"{result}c")
        else:
            return str(f"{result}")

     # W
    if type1 == "w" and type2 == "ms":
        result = num * 604800000
        if symbol == True:
            return str(f"{result}ms")
        else:
            return str(f"{result}")
    if type1 == "w" and type2 == "s":
        result = num * 604800
        if symbol == True:
            return str(f"{result}s")
        else:
            return str(f"{result}")
    if type1 == "w" and type2 == "min":
        result = num * 10080
        if symbol == True:
            return str(f"{result}min")
        else:
            return str(f"{result}")
    if type1 == "w" and type2 == "h":
        result = num * 168
        if symbol == True:
            return str(f"{result}h")
        else:
            return str(f"{result}")
    if type1 == "w" and type2 == "d":
        result = num / 7
        if symbol == True:
            return str(f"{result}d")
        else:
            return str(f"{result}")
    if type1 == "w" and type2 == "w":
        result = num
        if symbol == True:
            return str(f"{result}w")
        else:
            return str(f"{result}")
    if type1 == "w" and type2 == "m":
        result = num / 4.345
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "w" and type2 == "y":
        result = num / 52.143
        if symbol == True:
            return str(f"{result}y")
        else:
            return str(f"{result}")
    if type1 == "w" and type2 == "dec":
        result = num / 521
        if symbol == True:
            return str(f"{result}dec")
        else:
            return str(f"{result}")
    if type1 == "w" and type2 == "c":
        result = num / 5214
        if symbol == True:
            return str(f"{result}c")
        else:
            return str(f"{result}")

        # M
    if type1 == "m" and type2 == "ms":
        result = num * 2628000000
        if symbol == True:
            return str(f"{result}ms")
        else:
            return str(f"{result}")
    if type1 == "m" and type2 == "s":
        result = num * 2628000
        if symbol == True:
            return str(f"{result}s")
        else:
            return str(f"{result}")
    if type1 == "m" and type2 == "min":
        result = num * 43800
        if symbol == True:
            return str(f"{result}min")
        else:
            return str(f"{result}")
    if type1 == "m" and type2 == "h":
        result = num * 730
        if symbol == True:
            return str(f"{result}h")
        else:
            return str(f"{result}")
    if type1 == "m" and type2 == "d":
        result = num * 30.417
        if symbol == True:
            return str(f"{result}d")
        else:
            return str(f"{result}")
    if type1 == "m" and type2 == "w":
        result = num * 4.345
        if symbol == True:
            return str(f"{result}w")
        else:
            return str(f"{result}")
    if type1 == "m" and type2 == "m":
        result = num
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "m" and type2 == "y":
        result = num / 12
        if symbol == True:
            return str(f"{result}y")
        else:
            return str(f"{result}")
    if type1 == "m" and type2 == "dec":
        result = num / 120
        if symbol == True:
            return str(f"{result}dec")
        else:
            return str(f"{result}")
    if type1 == "m" and type2 == "c":
        result = num / 1200
        if symbol == True:
            return str(f"{result}c")
        else:
            return str(f"{result}")

     # Y
    if type1 == "y" and type2 == "ms":
        result = num * 31540000000
        if symbol == True:
            return str(f"{result}ms")
        else:
            return str(f"{result}")
    if type1 == "y" and type2 == "s":
        result = num * 31540000
        if symbol == True:
            return str(f"{result}s")
        else:
            return str(f"{result}")
    if type1 == "y" and type2 == "min":
        result = num * 525600
        if symbol == True:
            return str(f"{result}min")
        else:
            return str(f"{result}")
    if type1 == "y" and type2 == "h":
        result = num * 8760
        if symbol == True:
            return str(f"{result}h")
        else:
            return str(f"{result}")
    if type1 == "y" and type2 == "d":
        result = num * 365
        if symbol == True:
            return str(f"{result}d")
        else:
            return str(f"{result}")
    if type1 == "y" and type2 == "w":
        result = num * 52.143
        if symbol == True:
            return str(f"{result}w")
        else:
            return str(f"{result}")
    if type1 == "y" and type2 == "m":
        result = num * 12
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "y" and type2 == "y":
        result = num
        if symbol == True:
            return str(f"{result}y")
        else:
            return str(f"{result}")
    if type1 == "y" and type2 == "dec":
        result = num / 10
        if symbol == True:
            return str(f"{result}dec")
        else:
            return str(f"{result}")
    if type1 == "y" and type2 == "c":
        result = num / 100
        if symbol == True:
            return str(f"{result}c")
        else:
            return str(f"{result}")

    # Dec
    if type1 == "dec" and type2 == "ms":
        result = num * 315400000000
        if symbol == True:
            return str(f"{result}ms")
        else:
            return str(f"{result}")
    if type1 == "dec" and type2 == "s":
        result = num * 315400000
        if symbol == True:
            return str(f"{result}s")
        else:
            return str(f"{result}")
    if type1 == "dec" and type2 == "min":
        result = num * 5256000
        if symbol == True:
            return str(f"{result}min")
        else:
            return str(f"{result}")
    if type1 == "dec" and type2 == "h":
        result = num * 87600
        if symbol == True:
            return str(f"{result}h")
        else:
            return str(f"{result}")
    if type1 == "dec" and type2 == "d":
        result = num * 3650
        if symbol == True:
            return str(f"{result}d")
        else:
            return str(f"{result}")
    if type1 == "dec" and type2 == "w":
        result = num * 521
        if symbol == True:
            return str(f"{result}w")
        else:
            return str(f"{result}")
    if type1 == "dec" and type2 == "m":
        result = num * 120
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "dec" and type2 == "y":
        result = num * 10
        if symbol == True:
            return str(f"{result}y")
        else:
            return str(f"{result}")
    if type1 == "dec" and type2 == "dec":
        result = num
        if symbol == True:
            return str(f"{result}dec")
        else:
            return str(f"{result}")
    if type1 == "dec" and type2 == "c":
        result = num / 10
        if symbol == True:
            return str(f"{result}c")
        else:
            return str(f"{result}")

# C
    if type1 == "c" and type2 == "ms":
        result = num * 3154000000000
        if symbol == True:
            return str(f"{result}ms")
        else:
            return str(f"{result}")
    if type1 == "c" and type2 == "s":
        result = num * 3154000000
        if symbol == True:
            return str(f"{result}s")
        else:
            return str(f"{result}")
    if type1 == "c" and type2 == "min":
        result = num * 52560000
        if symbol == True:
            return str(f"{result}min")
        else:
            return str(f"{result}")
    if type1 == "c" and type2 == "h":
        result = num * 876000
        if symbol == True:
            return str(f"{result}h")
        else:
            return str(f"{result}")
    if type1 == "c" and type2 == "d":
        result = num * 36500
        if symbol == True:
            return str(f"{result}d")
        else:
            return str(f"{result}")
    if type1 == "dec" and type2 == "w":
        result = num * 5214
        if symbol == True:
            return str(f"{result}w")
        else:
            return str(f"{result}")
    if type1 == "dec" and type2 == "m":
        result = num * 1200
        if symbol == True:
            return str(f"{result}m")
        else:
            return str(f"{result}")
    if type1 == "dec" and type2 == "y":
        result = num * 100
        if symbol == True:
            return str(f"{result}y")
        else:
            return str(f"{result}")
    if type1 == "dec" and type2 == "dec":
        result = num * 10
        if symbol == True:
            return str(f"{result}dec")
        else:
            return str(f"{result}")
    if type1 == "dec" and type2 == "c":
        result = num
        if symbol == True:
            return str(f"{result}c")
        else:
            return str(f"{result}")



