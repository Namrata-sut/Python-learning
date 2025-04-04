import pyinputplus as pyip
# response = pyip.inputInt(prompt='Enter a number: ')

# The min, max, greaterThan, and lessThan
response = pyip.inputNum()
print(response)
response_min = pyip.inputNum('Enter num: ', min=4)
print(response_min)
response_gt = pyip.inputNum('Enter num gt: ', greaterThan=4)
print(response_gt)
response_lt_min = pyip.inputNum('>', min=4, lessThan=6)
print(response_lt_min)

# The blank Keyword Argument
response_blank = pyip.inputNum(blank=False)
response_blank_true = pyip.inputNum(blank=True)

# The limit, timeout, and default Keyword Arguments
response_limit = pyip.inputNum(limit=2)
# raise limitOrTimeoutException
# pyinputplus.RetryLimitException

response_timeout = pyip.inputNum(timeout=10)
# pyinputplus.TimeoutException

response_default = pyip.inputNum(limit=2, default='N/A')
print(response_default)

# allowRegexes
response_allow_regex = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+'])
# response_allow_regex = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+'])

# blockRegexes
response_block_regex = pyip.inputNum(blockRegexes=[r'[02468]$'])

response_allow_block_regex = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])

# Passing a Custom Validation Function to inputCustom()
# def adds_up_to_ten(numbers):
#     numbers_list = list(numbers)
#     for i, digit in enumerate(numbers_list):
#         numbers_list[i] = int(digit)
#     if sum(numbers_list) != 10:
#         raise Exception('The digits must add up to 10, not %s.' %(sum(numbers_list)))
#     return int(numbers) # Return an int form of numbers.
#
# response = pyip.inputCustom(adds_up_to_ten)

# # inputYesNo
while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break
        print('Thank you. Have a nice day.')

# Answer 10 question
import random, time

number_of_questions = 10
correct_answers = 0
for question_number in range(number_of_questions):
    # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (question_number, num1, num2)
    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        if True:
            pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                          blockRegexes=[('.*', 'Incorrect!')],
                          timeout=8, limit=3)
            correct_answers += 1
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')

time.sleep(1) # Brief pause to let user see the result.
print('Score: %s / %s' % (correct_answers, number_of_questions))