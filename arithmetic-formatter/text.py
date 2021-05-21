import re


def arithmetic_arranger(problems, result=False):
    l = len(problems)

    for problem in problems:
        num1, oprt, num2 = problem.split()

        if l > 5:
            print('Error: Too many problems.')
        elif oprt != '+' or oprt != '-':
            print("Error: Operator must be ' + ' or ' - '.")
        elif re.search("[a-zA-Z]", problem) != None or "." in problem:
            print('Error: Numbers must only contain digits.')
        elif len(num1) > 4 or len(num2) > 4:
            print('Error: Numbers cannot be more than four digits.')

        arranged_problems = [[], [], [], []]
        #line1
        arranged_problems[0].append(num1)
        #line2
        arranged_problems[1].append(num2)

        max_len = max(len((num1)), len((num2)))
        #line3
        arranged_problems[2].append('-' * (max_len + 2))
        #line4
        if result == True:
            if '+' in problem:
                arranged_problems[3].append(str(int(num1) + int(num2)))
            elif '-' in problem:
                arranged_problems[3].append(str(int(num1) - int(num2)))

    line_one = []
    line_two = []
    line_three = []
    line_four = []

    problem_width = []
    for element in arranged_problems[2]:
        problem_width.append(len(element))

    separator = '    '

    for count, i in enumerate(range(l)):
        if count != l - 1:
            line_one.append(arranged_problems[0][i].rjust(problem_width[i]) +
                            separator)
        else:
            line_one.append(arranged_problems[0][i].rjust(problem_width[i]) +
                            "\n")
    print(line_one)

    for i in range(l):
        if "+" in problems[i]:
            if arranged_problems[1][i] != arranged_problems[1][-1]:
                line_two.append(
                    "+" + arranged_problems[1][i].rjust(problem_width[i] - 1) +
                    separator)
            else:
                line_two.append(
                    "+" + arranged_problems[1][i].rjust(problem_width[i] - 1) +
                    "\n")
        elif "-" in problems[i]:
            if arranged_problems[1][i] != arranged_problems[1][-1]:
                line_two.append(
                    "-" + arranged_problems[1][i].rjust(problem_width[i] - 1) +
                    separator)
            else:
                line_two.append(
                    "-" + arranged_problems[1][i].rjust(problem_width[i] - 1) +
                    "\n")

    if result == True:
        line_three.append(separator.join(arranged_problems[2]) + '\n')
    else:
        line_three.append(separator.join(arranged_problems[2]))

    if result == True:
        for i in range(l):
            if arranged_problems[3][i] != arranged_problems[3][-1]:
                line_four.append(
                    arranged_problems[3][i].rjust(problem_width[i]) +
                    separator)
            else:
                if problems[i] != problems[-1]:
                    line_four.append(
                        arranged_problems[3][i].rjust(problem_width[i]) + "\n")
                else:
                    line_four.append(arranged_problems[3][i].rjust(
                        problem_width[i]))

    string1 = ''.join(line_one)
    string2 = ''.join(line_two)
    string3 = ''.join(line_three)
    string4 = ''.join(line_four)
    arranged_strings = string1 + string2 + string3 + string4

    return arranged_strings


arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
