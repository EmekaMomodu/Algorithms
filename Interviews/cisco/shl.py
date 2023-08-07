"""
You are given a list of strings that may represent valid latitude/longitude pairs. Your task is to check if the given latitude/longitude pairs are valid or not.
A string (X,Y) is considered valid if the following criteria are met:
The string starts with a bracket, has a comma after X and ends with a bracket.There is no space between the opening parenthesis and the first character of
There is no space between the comma and the last character of x.
There is no space between the comma and the first character of V.
There is no space between Y and the closing parenthesis.
X and Y are decimal numbers and may be preceded by a sign.
There are no leading zeros.
No other characters are allowed in X or Y.
-90 - X s 90 and -180 s Y s 180
Write an algorithm to identify the valid and invalid latitude/longitude pairs from the given list of strings.
Input
The first line of input consists of an integer-input size, representing the size of the string (N).
The next line consists of N space-separated substrings containing the latitude/longitude
Output
Print N space-separated strings representing the valid and invalid latitude/longitude pairs from the given list of strings. Print "Valid" for valid pairs and "Invalid" for invalid pairs.
Constraints
1 s Ns 100
"""
def is_valid(cords):
    res = []
    signs = "+-"
    for cord in cords:
        if len(cord) < 1:
            res.append("Invalid")
            continue

        if cord[0] != '(' or cord[-1] != ')' or ' ' in cord or cord.count(',') != 1:
            res.append("Invalid")
            continue

        cord_list = cord.split(',')
        x_str = cord_list[0][1:]
        y_str = cord_list[1][:-1]

        try:
            x = float(x_str)
            y = float(y_str)
        except ValueError:
            res.append("Invalid")
            continue

        x_str_revert = str(x)
        y_str_revert = str(y)

        if x_str[0] == '+': x_str = x_str[1:]
        if y_str[0] == '+': y_str = y_str[1:]

        if len(x_str.split('.')[0]) != len(x_str_revert.split('.')[0]
            or len(y_str.split('.')[0]) != len(y_str_revert.split('.')[0])):
            res.append("Invalid")
            continue

        if -90 <= x <= 90 and -180 <= y <= 180:
            res.append("Valid")
            continue

        res.append("Invalid")

    return res

if __name__ == '__main__':
    cords_arg = ["(C)", "(++90,-180)", "(0.0,9.)"]
    print(is_valid(cords_arg))
