def getSymbol(symbol):
     return (f"°{symbol.upper()}")
def addSymbol(result, symbol):
    return result + getSymbol(symbol)


def temp(type1, type2, num, symbol):
    result = 0
    if type1 == type2:
        result = num
    if type1 == "c" and type2 == "f":
        result = (num*9/5) + 32
    if type1 == "c" and type2 == "k":
        result = num + 273.15
    if type1 == "f" and type2 == "c":
        result = (num-32)*5/9
    if type1 == "f" and type2 == "k":
        result = (num - 32)*5 / 9 + 273.15
    if type1 == "k" and type2 == "f":
        result = (num + 32) / 5 * 9 - 273.15
    if type1 == "k" and type2 == "c":
        result = num - 273.15
    else:
        return "Invalid"
    if symbol:
        return addSymbol(result, type2)
    else:
        return result

def length(type1, type2, num, symbol):
    result = 0
    if type1 == type2:
        result = num
    if type1 == "km" and type2 == "m":
        result = num * 1000

    if type1 == "km" and type2 == "cm":
        result = num * 100000

    if type1 == "km" and type2 == "mm":
        result = num * 1000000

    if type1 == "km" and type2 == "nm":
        result = num * 1000000000000

    if type1 == "km" and type2 == "mi":
        result = num / 1.609

    if type1 == "km" and type2 == "yd":
        result = num * 1093.613298

    if type1 == "km" and type2 == "ft":
        result = num * 3280.83989

    if type1 == "km" and type2 == "in":
        result = num * 39370.07874

    # Meter
    if type1 == "m" and type2 == "km":
        result = num / 1000

    if type1 == "m" and type2 == "cm":
        result = num * 100

    if type1 == "m" and type2 == "mm":
        result = num * 1000

    if type1 == "m" and type2 == "nm":
        result = num * 1000000000

    if type1 == "m" and type2 == "mi":
        result = num * 0.00062137

    if type1 == "m" and type2 == "yd":
        result = num * 1.09361

    if type1 == "m" and type2 == "ft":
        result = num * 3.28084

    if type1 == "m" and type2 == "in":
        result = num * 39.37

    # Centimeter
    if type1 == "cm" and type2 == "km":
        result = num / 100000

    if type1 == "cm" and type2 == "m":
        result = num / 100

    if type1 == "cm" and type2 == "mm":
        result = num * 10

    if type1 == "cm" and type2 == "nm":
        result = num * 10000000

    if type1 == "cm" and type2 == "mi":
        result = num / 160934

    if type1 == "cm" and type2 == "yd":
        result = num / 91.44


    if type1 == "cm" and type2 == "ft":
        result = num / 30.48


    if type1 == "cm" and type2 == "in":
        result = num / 2.54
        if symbol:
            return str(f"{result}in")

    # Millimeter
    if type1 == "mm" and type2 == "km":
        result = num / 1000000


    if type1 == "mm" and type2 == "m":
        result = num / 1000
    if type1 == "mm" and type2 == "cm":
        result = num / 10
    if type1 == "mm" and type2 == "nm":
        result = num * 1000000


    if type1 == "mm" and type2 == "mi":
        result = num / 1609000
        if symbol:
            return str(f"{result}mi")

    if type1 == "mm" and type2 == "yd":
        result = num / 914


    if type1 == "mm" and type2 == "ft":
        result = num / 305


    if type1 == "mm" and type2 == "in":
        result = num / 25.4
        if symbol:
            return str(f"{result}in")

    # Nanometer
    if type1 == "nm" and type2 == "km":
        result = num / 1000000000000


    if type1 == "nm" and type2 == "m":
        result = num / 1000000000


    if type1 == "nm" and type2 == "cm":
        result = num / 10000000


    if type1 == "nm" and type2 == "mm":
        result = num / 1000000


    if type1 == "nm" and type2 == "mi":
        result = num / 1609000000000
        if symbol:
            return str(f"{result}mi")

    if type1 == "nm" and type2 == "yd":
        result = num / 914400000


    if type1 == "nm" and type2 == "ft":
        result = num / 304800000


    if type1 == "nm" and type2 == "in":
        result = num / 25400000
        if symbol:
            return str(f"{result}in")

    # Mile
    if type1 == "mi" and type2 == "km":
        result = num * 1.609


    if type1 == "mi" and type2 == "m":
        result = num * 1609


    if type1 == "mi" and type2 == "cm":
        result = num * 160934


    if type1 == "mi" and type2 == "mm":
        result = num * 1609000


    if type1 == "mi" and type2 == "nm":
        result = num * 1609000000000


    if type1 == "mi" and type2 == "yd":
        result = num * 1764


    if type1 == "mi" and type2 == "ft":
        result = num * 5280


    if type1 == "mi" and type2 == "in":
        result = num * 63360
        if symbol:
            return str(f"{result}in")

    # Yard
    if type1 == "yd" and type2 == "km":
        result = num / 1094


    if type1 == "yd" and type2 == "m":
        result = num / 1.094


    if type1 == "yd" and type2 == "cm":
        result = num * 91.44


    if type1 == "yd" and type2 == "mm":
        result = num * 914


    if type1 == "yd" and type2 == "nm":
        result = num * 914400000


    if type1 == "yd" and type2 == "mi":
        result = num / 1760
        if symbol:
            return str(f"{result}mi")

    if type1 == "yd" and type2 == "ft":
        result = num * 3


    if type1 == "yd" and type2 == "in":
        result = num * 36
        if symbol:
            return str(f"{result}in")

        # Foot
    if type1 == "ft" and type2 == "km":
        result = num / 3281


    if type1 == "ft" and type2 == "m":
        result = num / 3.281


    if type1 == "ft" and type2 == "cm":
        result = num * 30.48


    if type1 == "ft" and type2 == "mm":
        result = num * 305


    if type1 == "ft" and type2 == "nm":
        result = num * 304800000


    if type1 == "ft" and type2 == "mi":
        result = num / 5280
        if symbol:
            return str(f"{result}mi")

    if type1 == "ft" and type2 == "yd":
        result = num / 3


    if type1 == "ft" and type2 == "in":
        result = num * 12
        if symbol:
            return str(f"{result}in")

        # Inch
    if type1 == "in" and type2 == "km":
        result = num / 39370


    if type1 == "in" and type2 == "m":
        result = num / 39.37


    if type1 == "in" and type2 == "cm":
        result = num * 2.54


    if type1 == "in" and type2 == "mm":
        result = num * 25.4


    if type1 == "in" and type2 == "nm":
        result = num * 25400000


    if type1 == "in" and type2 == "mi":
        result = num / 63360
        if symbol:
            return str(f"{result}mi")

    if type1 == "in" and type2 == "yd":
        result = num / 36


    if type1 == "in" and type2 == "ft":
        result = num / 12


    else:
        return ("Invalid")
    if symbol:
        return addSymbol(result, type2)
    else:
        return result

def speed(type1, type2, num, symbol):
    result = 0
    if type1 == type2:
        result = num

    if type1 == "mph" and type2 == "fts":
        result = num * 1.467

    if type1 == "mph" and type2 == "ms":
        result = num / 2.237

    if type1 == "mph" and type2 == "kmh":
        result = num * 1.609

    if type1 == "mph" and type2 == "kn":
        result = num / 1.151

    # FPS
    if type1 == "fts" and type2 == "mph":
        result = num / 1.467


    if type1 == "fts" and type2 == "ms":
        result = num / 3.281

    if type1 == "fts" and type2 == "kmh":
        result = num * 1.097

    if type1 == "fts" and type2 == "kn":
        result = num / 1.688

    # M S
    if type1 == "ms" and type2 == "mph":
        result = num * 2.237

    if type1 == "ms" and type2 == "fts":
        result = num * 3.281


    if type1 == "ms" and type2 == "kmh":
        result = num * 3.6

    if type1 == "ms" and type2 == "kn":
        result = num / 1.944

    # KMS
    if type1 == "kmh" and type2 == "mph":
        result = num / 1.609

    if type1 == "kmh" and type2 == "fts":
        result = num / 1.097

    if type1 == "kmh" and type2 == "ms":
        result = num / 3.6


    if type1 == "kmh" and type2 == "kn":
        result = num / 1.852

    # Kn
    if type1 == "kn" and type2 == "mph":
        result = num * 1.151

    if type1 == "kn" and type2 == "fts":
        result = num * 1.688

    if type1 == "kn" and type2 == "ms":
        result = num / 1.944

    if type1 == "kn" and type2 == "kmh":
        result = num * 1.852

    else:
        return ("Invalid")
    if symbol:
        return addSymbol(result, type2)
    else:
        return result


def time(type1, type2, num, symbol):
    result = 0
    if type1 == type2:
        result = num
    # MS
    if type1 == "ms" and type2 == "s":
        result = num / 1000

    if type1 == "ms" and type2 == "min":
        result = num / 60000

    if type1 == "ms" and type2 == "h":
        result = num / 3600000

    if type1 == "ms" and type2 == "d":
        result = num / 86400000

    if type1 == "ms" and type2 == "w":
        result = num / 604800000

    if type1 == "ms" and type2 == "m":
        result = num / 2628000000

    if type1 == "ms" and type2 == "y":
        result = num / 31540000000

    if type1 == "ms" and type2 == "dec":
        result = num / 315400000000

    # S
    if type1 == "s" and type2 == "ms":
        result = num * 1000

    if type1 == "s" and type2 == "min":
        result = num / 60

    if type1 == "s" and type2 == "h":
        result = num / 3600

    if type1 == "s" and type2 == "d":
        result = num / 86400

    if type1 == "s" and type2 == "w":
        result = num / 604800

    if type1 == "s" and type2 == "m":
        result = num / 2628000

    if type1 == "s" and type2 == "y":
        result = num / 31540000

    if type1 == "s" and type2 == "dec":
        result = num / 315400000

    if type1 == "s" and type2 == "dec":
        result = num / 3154000000

    # M
    if type1 == "min" and type2 == "ms":
        result = num * 60000

    if type1 == "min" and type2 == "s":
        result = num * 60

    if type1 == "min" and type2 == "h":
        result = num / 60

    if type1 == "min" and type2 == "d":
        result = num / 1440

    if type1 == "min" and type2 == "w":
        result = num / 10080

    if type1 == "min" and type2 == "m":
        result = num / 43800

    if type1 == "min" and type2 == "y":
        result = num / 525600

    if type1 == "min" and type2 == "dec":
        result = num / 5256000

    if type1 == "min" and type2 == "c":
        result = num / 52560000

    # H
    if type1 == "h" and type2 == "ms":
        result = num * 3600000

    if type1 == "h" and type2 == "s":
        result = num * 3600

    if type1 == "h" and type2 == "min":
        result = num * 60

    if type1 == "h" and type2 == "d":
        result = num / 24

    if type1 == "h" and type2 == "w":
        result = num / 168

    if type1 == "h" and type2 == "m":
        result = num / 730

    if type1 == "h" and type2 == "y":
        result = num / 8760

    if type1 == "h" and type2 == "dec":
        result = num / 87600

    if type1 == "h" and type2 == "c":
        result = num / 876000

    # D
    if type1 == "d" and type2 == "ms":
        result = num * 86400000

    if type1 == "d" and type2 == "s":
        result = num * 86400

    if type1 == "d" and type2 == "min":
        result = num * 1440

    if type1 == "d" and type2 == "h":
        result = num * 24

    if type1 == "d" and type2 == "w":
        result = num / 7

    if type1 == "d" and type2 == "m":
        result = num / 30.417

    if type1 == "d" and type2 == "y":
        result = num / 365

    if type1 == "d" and type2 == "dec":
        result = num / 3650

    if type1 == "d" and type2 == "c":
        result = num / 36500

    # W
    if type1 == "w" and type2 == "ms":
        result = num * 604800000

    if type1 == "w" and type2 == "s":
        result = num * 604800

    if type1 == "w" and type2 == "min":
        result = num * 10080

    if type1 == "w" and type2 == "h":
        result = num * 168

    if type1 == "w" and type2 == "d":
        result = num / 7

    if type1 == "w" and type2 == "m":
        result = num / 4.345

    if type1 == "w" and type2 == "y":
        result = num / 52.143

    if type1 == "w" and type2 == "dec":
        result = num / 521

    if type1 == "w" and type2 == "c":
        result = num / 5214

        # M
    if type1 == "m" and type2 == "ms":
        result = num * 2628000000

    if type1 == "m" and type2 == "s":
        result = num * 2628000

    if type1 == "m" and type2 == "min":
        result = num * 43800

    if type1 == "m" and type2 == "h":
        result = num * 730

    if type1 == "m" and type2 == "d":
        result = num * 30.417

    if type1 == "m" and type2 == "w":
        result = num * 4.345

    if type1 == "m" and type2 == "y":
        result = num / 12

    if type1 == "m" and type2 == "dec":
        result = num / 120

    if type1 == "m" and type2 == "c":
        result = num / 1200

    # Y
    if type1 == "y" and type2 == "ms":
        result = num * 31540000000

    if type1 == "y" and type2 == "s":
        result = num * 31540000

    if type1 == "y" and type2 == "min":
        result = num * 525600

    if type1 == "y" and type2 == "h":
        result = num * 8760

    if type1 == "y" and type2 == "d":
        result = num * 365

    if type1 == "y" and type2 == "w":
        result = num * 52.143

    if type1 == "y" and type2 == "m":
        result = num * 12

    if type1 == "y" and type2 == "dec":
        result = num / 10

    if type1 == "y" and type2 == "c":
        result = num / 100

    # Dec
    if type1 == "dec" and type2 == "ms":
        result = num * 315400000000

    if type1 == "dec" and type2 == "s":
        result = num * 315400000

    if type1 == "dec" and type2 == "min":
        result = num * 5256000

    if type1 == "dec" and type2 == "h":
        result = num * 87600

    if type1 == "dec" and type2 == "d":
        result = num * 3650

    if type1 == "dec" and type2 == "w":
        result = num * 521

    if type1 == "dec" and type2 == "m":
        result = num * 120

    if type1 == "dec" and type2 == "y":
        result = num * 10

    if type1 == "dec" and type2 == "c":
        result = num / 10

    # C
    if type1 == "c" and type2 == "ms":
        result = num * 3154000000000

    if type1 == "c" and type2 == "s":
        result = num * 3154000000

    if type1 == "c" and type2 == "min":
        result = num * 52560000

    if type1 == "c" and type2 == "h":
        result = num * 876000

    if type1 == "c" and type2 == "d":
        result = num * 36500

    if type1 == "dec" and type2 == "w":
        result = num * 5214

    if type1 == "dec" and type2 == "m":
        result = num * 1200

    if type1 == "dec" and type2 == "y":
        result = num * 100

    if type1 == "dec" and type2 == "dec":
        result = num * 10

    if symbol:
        return addSymbol(result, type2)
    else:
        return result






