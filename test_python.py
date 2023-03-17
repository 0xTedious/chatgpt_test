import pandas as pd

input_1 = "Ronnie"
input_2 = "Eats"
input_3 = "Cucumber"

def string_concat(input_1, input_2, input_3):
    output = input_1 + " " + input_2 + " " + input_3
    return output

output = string_concat(input_1, input_2, input_3)
print(output)
