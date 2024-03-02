from collections import Counter


def matchingStrings(strings, queries):
    # Write your code here
    output = []
    for x in queries:
        if x in strings:
            output += [v for k, v in Counter(strings).items() if k == x]
        else:
            output += [0]

    return output


strings = ['aba', 'baba', 'aba', 'xzxb']
quieries = [4,
            'aba',
            'baba',
            'aba',
            'xzxb',
            '3',
            'aba',
            'xzxb',
            'ab']


print(matchingStrings(strings, quieries))
