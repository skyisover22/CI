def donuts(count):
    if count >= 10:
        return 'Number of donuts: many'
    return 'Number of donuts: ' + str(count)


def both_ends(s):
    if len(s) < 2:
        return ''
    return s[:2] + s[-2:]


def fix_start(s):
    return  s[0] + s[1:].replace(s[0], '*')


def mix_up(a, b):
    return b[:2] + a[2:] + ' ' + a[:2] + b[2:]
                                 

def verbing(s):
    if len(s) > 3:
        if s[-3:] == 'ing':
            return s + 'ly'
        else:
            return s + 'ing'
    return s


def not_bad(s):
    x = s.find('not')
    y = s.find('bad')
    if x != -1:
        if x < y:
            return s[:x] + 'good' + s[y+3:]
    return s


def front_back(a, b):
    mid_a = len(a)//2 + len(a)%2
    mid_b = len(b)//2 + len(b)%2
    return a[:mid_a] + b[:mid_b] + a[mid_a:] + b[mid_b:]



def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{0} got: {1} expected: {2}'.format(prefix, repr(got),
                                              repr(expected)))


def main():
    print('donuts')
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print()
    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print()
    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')

    print()
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    main()
