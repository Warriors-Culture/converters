def length(type1, type2, num):
    if type1 == "1" and type2 == "1":
        return str(f"{num}km")
    if type1 == "1" and type2 == "2":
        result = num / 1000
        return str(f"{result}m")
    if type1 == "1" and type2 == "3":
        result = num/100000
        return str(f"{result}cm")
    if type1 == "1" and type2 == "4":
        result = num/1000000
        return str(f"{result}mm")
    if type1 == "1" and type2 == "5":
        result = num/1000000000000
        return str(f"{result}nm")
    if type1 == "1" and type2 == "6":
        result = num * 0.6214
        return str(f"{result}mi")
    if type1 == "1" and type2 == "7":
        result = num * 1093.613298
        return str(f"{result}yd")
    if type1 == "1" and type2 == "8":
        result = num * 3280.83989
        return str(f"{result}ft")
    if type1 == "1" and type2 == "9":
        result = num * 39370.07874
        return str(f"{result}in")
    # Meter
    if type1 == "2" and type2 == "1":
        result = num * 1000
        return str(f"{result}km")
    if type1 == "2" and type2 == "2":
        result = num
        return str(f"{result}m")
    if type1 == "2" and type2 == "3":
        result = num * 100
        return str(f"{result}cm")
    if type1 == "2" and type2 == "4":
        result = num * 1000
        return str(f"{result}mm")
    if type1 == "2" and type2 == "5":
        result = num * 1000000000
        return str(f"{result}nm")
    if type1 == "2" and type2 == "6":
        result = num * 0.00062137
        return str(f"{result}mi")
    if type1 == "2" and type2 == "7":
        result = num * 1.09361
        return str(f"{result}yd")
    if type1 == "2" and type2 == "8":
        result = num * 3.28084
        return str(f"{result}ft")
    if type1 == "2" and type2 == "9":
        result = num * 39.37
        return str(f"{result}in")
    # Centimeter
    if type1 == "3" and type2 == "1":
        result = num / 100000
        return str(f"{result}km")
    if type1 == "3" and type2 == "2":
        result = num / 100
        return str(f"{result}m")
    if type1 == "3" and type2 == "3":
        result = num
        return str(f"{result}cm")
    if type1 == "3" and type2 == "4":
        result = num * 10
        return str(f"{result}mm")
    if type1 == "3" and type2 == "5":
        result = num * 10000000
        return str(f"{result}nm")
    if type1 == "3" and type2 == "6":
        result = num / 160934
        return str(f"{result}mi")
    if type1 == "3" and type2 == "7":
        result = num / 91.44
        return str(f"{result}yd")
    if type1 == "3" and type2 == "8":
        result = num / 30.48
        return str(f"{result}ft")
    if type1 == "3" and type2 == "9":
        result = num / 2.54
        return str(f"{result}in")
    # Millimeter
    if type1 == "4" and type2 == "1":
        result = num/1000000
        return str(f"{result}km")
    if type1 == "4" and type2 == "2":
        result = num/1000
        return str(f"{result}m")
    if type1 == "4" and type2 == "3":
        result = num / 10
        return str(f"{result}cm")
    if type1 == "4" and type2 == "4":
        result = num
        return str(f"{result}mm")
    if type1 == "4" and type2 == "5":
        result = num * 1000000
        return str(f"{result}nm")
    if type1 == "4" and type2 == "6":
        result = num / 1609000
        return str(f"{result}mi")
    if type1 == "4" and type2 == "7":
        result = num / 914
        return str(f"{result}yd")
    if type1 == "4" and type2 == "8":
        result = num / 305
        return str(f"{result}ft")
    if type1 == "4" and type2 == "9":
        result = num / 25.4
        return str(f"{result}in")
    # Nanometer
    if type1 == "5" and type2 == "1":
        result = num/1000000000000
        return str(f"{result}km")
    if type1 == "5" and type2 == "2":
        result = num/1000000000
        return str(f"{result}m")
    if type1 == "5" and type2 == "3":
        result = num / 10000000
        return str(f"{result}cm")
    if type1 == "5" and type2 == "4":
        result = num / 1000000
        return str(f"{result}mm")
    if type1 == "5" and type2 == "5":
        result = num
        return str(f"{result}nm")
    if type1 == "5" and type2 == "6":
        result = num / 1609000000000
        return str(f"{result}mi")
    if type1 == "5" and type2 == "7":
        result = num / 914400000
        return str(f"{result}yd")
    if type1 == "5" and type2 == "8":
        result = num / 304800000
        return str(f"{result}ft")
    if type1 == "5" and type2 == "9":
        result = num / 25400000
        return str(f"{result}in")
    # Mile
    if type1 == "6" and type2 == "1":
        result = num*1.609
        return str(f"{result}km")
    if type1 == "6" and type2 == "2":
        result = num*1609
        return str(f"{result}m")
    if type1 == "6" and type2 == "3":
        result = num * 160934
        return str(f"{result}cm")
    if type1 == "6" and type2 == "4":
        result = num * 1609000
        return str(f"{result}mm")
    if type1 == "6" and type2 == "5":
        result = num * 1609000000000
        return str(f"{result}nm")
    if type1 == "6" and type2 == "6":
        result = num
        return str(f"{result}mi")
    if type1 == "6" and type2 == "7":
        result = num * 1764
        return str(f"{result}yd")
    if type1 == "6" and type2 == "8":
        result = num * 5280
        return str(f"{result}ft")
    if type1 == "6" and type2 == "9":
        result = num * 63360
        return str(f"{result}in")
    # Yard
    if type1 == "7" and type2 == "1":
        result = num/1094
        return str(f"{result}km")
    if type1 == "7" and type2 == "2":
        result = num/1.094
        return str(f"{result}m")
    if type1 == "7" and type2 == "3":
        result = num * 91.44
        return str(f"{result}cm")
    if type1 == "7" and type2 == "4":
        result = num * 914
        return str(f"{result}mm")
    if type1 == "7" and type2 == "5":
        result = num * 914400000
        return str(f"{result}nm")
    if type1 == "7" and type2 == "6":
        result = num / 1760
        return str(f"{result}mi")
    if type1 == "7" and type2 == "7":
        result = num
        return str(f"{result}yd")
    if type1 == "7" and type2 == "8":
        result = num * 3
        return str(f"{result}ft")
    if type1 == "7" and type2 == "9":
        result = num * 36
        return str(f"{result}in")
        # Foot
    if type1 == "8" and type2 == "1":
        result = num / 3281
        return str(f"{result}km")
    if type1 == "8" and type2 == "2":
        result = num / 3.281
        return str(f"{result}m")
    if type1 == "8" and type2 == "3":
        result = num * 30.48
        return str(f"{result}cm")
    if type1 == "8" and type2 == "4":
        result = num * 305
        return str(f"{result}mm")
    if type1 == "8" and type2 == "5":
        result = num * 304800000
        return str(f"{result}nm")
    if type1 == "8" and type2 == "6":
        result = num / 5280
        return str(f"{result}mi")
    if type1 == "8" and type2 == "7":
        result = num / 3
        return str(f"{result}yd")
    if type1 == "8" and type2 == "8":
        result = num
        return str(f"{result}ft")
    if type1 == "8" and type2 == "9":
        result = num * 12
        return str(f"{result}in")
        # Inch
    if type1 == "9" and type2 == "1":
        result = num / 39370
        return str(f"{result}km")
    if type1 == "9" and type2 == "2":
        result = num / 39.37
        return str(f"{result}m")
    if type1 == "9" and type2 == "3":
        result = num * 2.54
        return str(f"{result}cm")
    if type1 == "9" and type2 == "4":
        result = num * 25.4
        return str(f"{result}mm")
    if type1 == "9" and type2 == "5":
        result = num * 25400000
        return str(f"{result}nm")
    if type1 == "9" and type2 == "6":
        result = num / 63360
        return str(f"{result}mi")
    if type1 == "9" and type2 == "7":
        result = num / 36
        return str(f"{result}yd")
    if type1 == "9" and type2 == "8":
        result = num / 12
        return str(f"{result}ft")
    if type1 == "9" and type2 == "9":
        result = num
        return str(f"{result}in")

def temp(type1, type2, num):
    if type1 == "1" and type2 == "1":
        return str(f"{num}°C")
    if type1 == "1" and type2 == "2":
        result = (num*9/5) + 32
        return str(f"{result}°F")
    if type1 == "1" and type2 == "3":
        result = num + 273.15
        return str(f"{result}°K")
    if type1 == "2" and type2 == "2":
        return str(f"{num}°F")
    if type1 == "2" and type2 == "1":
        result = (num-32)*5/9
        return str(f"{result}°C")
    if type1 == "2" and type2 == "3":
        result = (num - 32)*5 / 9 + 273.15
        return str(f"{result}°K")
    if type1 == "3" and type2 == "3":
        return str(f"{num}°K")
    if type1 == "3" and type2 == "2":
        result = (num + 32) / 5 * 9 - 273.15
        return str(f"{result}°F")
    if type1 == "3" and type2 == "1":
        result = num - 273.15
        return str(f"{result}°C")

def speed(type1,type2,num):
    if type1 == "1" and type2 == "1":
        result = num
        return str(f"{result}mph")
    if type1 == "1" and type2 == "2":
        result = num * 1.467
        return str(f"{result}ft/s")
    if type1 == "1" and type2 == "3":
        result = num / 2.237
        return str(f"{result}m/s")
    if type1 == "1" and type2 == "4":
        result = num * 1.609
        return str(f"{result}km/h")
    if type1 == "1" and type2 == "5":
        result = num / 1.151
        return str(f"{result}kn")
    # FPS
    if type1 == "2" and type2 == "1":
        result = num / 1.467
        return str(f"{result}mph")
    if type1 == "2" and type2 == "2":
        result = num
        return str(f"{result}ft/s")
    if type1 == "2" and type2 == "3":
        result = num / 3.281
        return str(f"{result}m/s")
    if type1 == "2" and type2 == "4":
        result = num * 1.097
        return str(f"{result}km/h")
    if type1 == "2" and type2 == "5":
        result = num / 1.688
        return str(f"{result}kn")
    #M S
    if type1 == "3" and type2 == "1":
        result = num * 2.237
        return str(f"{result}mph")
    if type1 == "3" and type2 == "2":
        result = num * 3.281
        return str(f"{result}ft/s")
    if type1 == "3" and type2 == "3":
        result = num
        return str(f"{result}m/s")
    if type1 == "3" and type2 == "4":
        result = num * 3.6
        return str(f"{result}km/h")
    if type1 == "3" and type2 == "5":
        result = num / 1.944
        return str(f"{result}kn")
    #KMS
    if type1 == "4" and type2 == "1":
        result = num / 1.609
        return str(f"{result}mph")
    if type1 == "4" and type2 == "2":
        result = num / 1.097
        return str(f"{result}ft/s")
    if type1 == "4" and type2 == "3":
        result = num / 3.6
        return str(f"{result}m/s")
    if type1 == "4" and type2 == "4":
        result = num
        return str(f"{result}km/h")
    if type1 == "4" and type2 == "5":
        result = num / 1.852
        return str(f"{result}kn")
    #Kn
    if type1 == "5" and type2 == "1":
        result = num * 1.151
        return str(f"{result}mph")
    if type1 == "5" and type2 == "2":
        result = num * 1.688
        return str(f"{result}ft/s")
    if type1 == "5" and type2 == "3":
        result = num / 1.944
        return str(f"{result}m/s")
    if type1 == "5" and type2 == "4":
        result = num * 1.852
        return str(f"{result}km/h")
    if type1 == "5" and type2 == "5":
        result = num
        return str(f"{result}kn")





