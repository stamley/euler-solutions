#p17

def num_letter_counts():
    sum = 0
    for i in range(1,1000):
        if i < 20:
            sum += len(translate(i))
        elif i < 100:
            sum += len(translate(i - i % 10)) + len(translate(int(str(i)[-1])))
            #print(translate(i - i % 10) + translate(int(str(i)[-1])))
        elif i % 100 == 0:
            sum += len(translate(int(str(i)[0]))) + len(translate(i))
        else:
            sum += len(translate(i)) + len('and') + len(translate(int(str(i)[1:3]) - i % 10)) + len(translate(int(str(i)[-1])))
            #print(translate(i) + 'and' + translate(int(str(i)[1:3]) - i % 10) + translate(int(str(i)[-1])))
    sum += len("onethousand")
    return sum

#print(int(str(123)[1:3]) - 123 % 10)

def translate(num):
    if num < 10:
        match num:
            case 1: return 'one'
            case 2: return 'two'
            case 3: return 'three'
            case 4: return 'four'
            case 5: return 'five'
            case 6: return 'six'
            case 7: return 'seven'
            case 8: return 'eight'
            case 9: return 'nine'
            case _: return ''
    if num < 100:
        match num:
            case 10: return 'ten'
            case 11: return 'eleven'
            case 12: return 'twelve'
            case 13: return 'thirteen'
            case 14: return 'fourteen'
            case 15: return 'fifteen'
            case 16: return 'sixteen'
            case 17: return 'seventeen'
            case 18: return 'eighteen'
            case 19: return 'nineteen'
            case 20: return 'twenty'
            case 30: return 'thirty'
            case 40: return 'forty'
            case 50: return 'fifty'
            case 60: return 'sixty'
            case 70: return 'seventy'
            case 80: return 'eighty'
            case 90: return 'ninety'
            case _: return ''
    if num < 1000:
        return translate(int(str(num)[0])) + 'hundred'

print(num_letter_counts())
