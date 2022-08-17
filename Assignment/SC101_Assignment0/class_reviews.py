"""
File: class_reviews.py
Name: Antina Yeh
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
    """
    TODO:
    """
    sc001 = False
    sc001_score = 0
    sc001_count = 0
    sc001_max = 0
    sc001_min = 0

    sc101 = False
    sc101_score = 0
    sc101_count = 0
    sc101_max = 0
    sc101_min = 0

    class_code = (input("Which class?")).lower().strip()
    if class_code == '-1':
        return print("No class scores were entered")

    while class_code != '-1':
        score = int(input("Score?"))
        if class_code == 'sc001':
            sc001 = True
            sc001_count += 1
            sc001_score += score
            if score > sc001_max:
                sc001_max = score
            if sc001_min == 0:
                sc001_min = score
            elif score < sc001_min:
                sc001_min = score
        else:
            sc101 = True
            sc101_count += 1
            sc101_score += score
            if score > sc101_max:
                sc101_max = score
            if sc101_min == 0:
                sc101_min = score
            elif score < sc101_min:
                sc101_min = score
        class_code = (input("Which class?")).lower().strip()

    result('SC001', sc001, sc001_score, sc001_count, sc001_max, sc001_min)
    result('SC101', sc101, sc101_score, sc101_count, sc101_max, sc101_min)


def result(code, data, score, count, max, min):
    """
    :param code: what class the result is for
    :param data: whether there is data for the class or not
    :param score: the total score
    :param count: the number of scores entered
    :param max: the maximum score
    :param min: the minimum score
    """
    short_code = code[2:5]
    for i in range(12):
        print("=", end="")
    print(code, end="")
    for i in range(12):
        print("=", end="")
    print("")
    if data:
        avg = score / count
        print('Max (' + short_code + '): ' + str(max))
        print('Min (' + short_code + '): ' + str(min))
        print('Avg (' + short_code + '): ' + str(avg))
    else:
        print('No score for ' + code)














# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
