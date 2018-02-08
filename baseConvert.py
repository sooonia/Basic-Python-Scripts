import math

# INPUTS
# num: the number you are trying to convert written in base 10
# base: the new base into which you wish to convert num

# OUTPUT
# prints a the converted number. Each digit is separated by a space to account for digits >9 and increase readability


def main(num, base):

    output = ""
    max_exp = int(math.log(num, base))

    current_exp = max_exp
    for i in range(max_exp, -1, -1):
        count = 0

        if i == 0 and num < base:
            output += str(int(num))
        elif num < math.pow(base, current_exp):
            output += "0 "
        else:
            while num >= math.pow(base, current_exp):
                count += 1
                num -= math.pow(base, current_exp)

            output += str(int(count)) + ' '
        current_exp -= 1

    print(output)


# some test calls
main(20, 3)
main(30, 5)
main(300, 40)
