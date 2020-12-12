import re

def dia4A(raw_data):
    
    data = preprocess(raw_data)

    must = [
            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid"
           # "cid"
            ]
   
    return sum([all([key in dic for key in must]) for dic in data])


def dia4B(raw_data):

    data = preprocess(raw_data)

    must = [
            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid"
           # "cid"
            ]
    # Unir estas dos lineas para ahorrar iteraciones.
    fstC = [dic for dic in data if all([key in dic for key in must])]
    return sum([all([validateByr(d['byr']),
            validateIyr(d['iyr']),
            validateEyr(d['eyr']),
            validateHgt(d['hgt']),
            validateHcl(d['hcl']),
            validateEcl(d['ecl']),
            validatePid(d['pid'])]) for d in fstC])


def preprocess(raw_data):
     with open(raw_data) as f:
        data = f.read()

     # Hacer algo un poquito mas funcional
     data = re.split(r"(?:\r?\n){2,}",data.strip())
     data = [i.replace('\n',' ').split(' ') for i in data]
    
     return [createDict(i) for i in data]
   

def createDict(x):
    return{i.split(':')[0]: i.split(':')[1] for i in x}


def validateByr(byr):
    # (Birth Year) - four digits; at least 1920 and at most 2002.
    return len(str(byr)) == 4 and '1920' <= str(byr) <= '2020'


def validateIyr(iyr):
    # (Issue Year) - four digits; at least 2010 and at most 2020.
    return len(str(iyr)) == 4 and '2010' <= str(iyr) <= '2020'


def validateEyr(eyr):
    # (Expiration Year) - four digits; at least 2020 and at most 2030.
    return len(str(eyr)) == 4 and '2020' <= str(eyr) <= '2030'


def validateHgt(hgt):
    # (Height) - a number followed by either cm or in:
    # - If cm, the number must be at least 150 and at most 193.
    # - If in, the number must be at least 59 and at most 76.
    return ['150' <= str(hgt)[:-2] <= '193', '59' <= str(hgt)[:-2] <= '76'][str(hgt)[-2:] == 'in']


def validateHcl(hcl):
    # (Hair Color) - a # followed by exactly six characters 0-9 or a-f
    return bool(re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', str(hcl)))


def validateEcl(ecl):
    # (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    return str(ecl) in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validatePid(pid):
    # (Passport ID) - a nine-digit number, including leading zeroes.
    return len(str(pid)) == 9  


if __name__ == '__main__':
    print(dia4A('input'))
    print(dia4B('input'))
