# import a size comparator?
# dict = { "example": "length" }
# tuple = {"example", length, "unit"}
# all units converted using Google Conversion as base
meter_to_unit = { "m": 1,"ft":0.3048, "km":1000, "cm": 0.01, "mm": 0.001}

class Measurement:
    number = int
    unit = str

    def __init__(self, number, unit):
        self.number = number
        self.unit = unit
    
    def __str__(self):
        return_str = str(self.number) + " " + self.unit
        return return_str

def check_unit(unit):
    if unit in meter_to_unit:
        return True
    else:
        return False

def convert_measurement(measurement):
    if measurement.unit != "m":
        new_unit = meter_to_unit[measurement.unit]
        converted_measurement = Measurement(measurement.number * new_unit, "m")
        print(converted_measurement)
        return converted_measurement
    else:
        return measurement

def find_closest(measurement, examples):
    closest_id = 0
    closest_no = 0.0
    diff_list = []
    for i in range(len(examples)):
        diff_list.append(examples[i][1] - measurement.number)
        
    print(diff_list)
    index_min = min(range(len(diff_list)), key = lambda i: abs(diff_list[i] - 0))
        
    return index_min

def compare_statement(comp_msrmt, conv_measurement, examples_list, examples_close_id):
    print(str(comp_msrmt.number) + " " + str(comp_msrmt.unit) + " is approximately " )
    msrmt_dec = conv_measurement.number / examples_list[examples_close_id][1]
    if msrmt_dec > 0:
        print(str(round(msrmt_dec, 3)) + " times of the " + examples_list[examples_close_id][0])
    else: 
        print(str(round(msrmt_dec, 3)) + " of the " + examples_list[examples_close_id][0])

def size_comparator(measurement_no, unit):
    examples_list = [ ("height of the Statue of Liberty", 46), ("height of a Moai statue", 21), ("length of the WCML", 642000) ]
    # 33.5m+ is SoL
    
    comp_measurement = Measurement(measurement_no, unit)
    conv_measurement = convert_measurement(comp_measurement)
    example_close_id = find_closest(conv_measurement, examples_list)
    compare_statement(comp_measurement, conv_measurement, examples_list, example_close_id)
    


def main():
    valid_unit = False
    valid_measurement = False

    while valid_measurement == False:
        measurement_no = input("Measurement: ")
        str_int = float(measurement_no)
        if str_int > 0:
            valid_measurement = True

    while valid_unit == False:
        unit = input("Unit: ")
        valid_unit = check_unit(unit)

    size_comparator(str_int, unit)

main()