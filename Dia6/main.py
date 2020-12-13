import re

def day6A(raw_data):
    data = preprocess(raw_data)

    return sum([len(set(i.replace('\n', ''))) for i in data])


def day6B(raw_data):
    data = preprocess(raw_data)

    sets = [i.split('\n') for i in data]
    sets[-1].pop(-1)
    return sum([equalResponses(i) for i in sets])


def preprocess(raw_data):
    with open(raw_data) as f:
        data = f.read()

    return data.split('\n\n')


def equalResponses(x):
    return len(set.intersection(*[set(i) for i in x]))


if __name__ == '__main__':
    print(day6A('input'))
    print(day6B('input'))
