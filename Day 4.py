import DATA

Checks = {"byr": True, "iyr": True, "eyr": True, "hgt": True, "hcl": True, "ecl": True, "pid": True, "cid": False}


def param_split(sample):
    sample = sample.split(":")
    return sample


def test_hcl(data):
    leters = "abcdefgh0123456789"
    print("hcl testing")
    for i in data:
        print("testing {}".format(i))
        if i in leters:
            print("yes.. continue")
            continue
        else:
            return False
    return True


def date_val(key, data, yr1, yr2):
    if test_int(data) and len(data) == 4 and yr1 <= int(data) <= yr2:
        print("{} is Valid".format(key))
        return True
    else:
        print("{} is not valid".format(key))

        return False


def test_int(data):
    try:
        int(data)
        return True
    except ValueError:
        return False


def check():
    count = 0
    pas = Passport()
    for i in Input:
        # print(i)
        if i == "":
            print("blank line.. reset passport......................")
            if pas.validate() and pas.validate_data():
                count += 1
            pas = Passport()
            continue
        test = i.split(" ")
        if len(test) > 1:
            for ii in test:
                key, data = param_split(ii)
                pas.param[key] = True
                pas.data[key] = data
        else:
            key, data = param_split(i)
            pas.param[key] = True
            pas.data[key] = data
    if pas.validate() and pas.validate_data():
        count += 1
    return count


class Passport:
    def __init__(self):
        self.param = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False,
                      "cid": False}
        self.Checks = {"byr": True, "iyr": True, "eyr": True, "hgt": True, "hcl": True, "ecl": True, "pid": True,
                       "cid": False}
        self.data = {"byr": "", "iyr": "", "eyr": "", "hgt": "", "hcl": "", "ecl": "", "pid": "",
                     "cid": ""}
        self.valid = False

    def validate(self):
        for key in self.Checks:
            if not self.Checks[key]:
                continue
            if self.Checks[key] and self.param[key]:
                # print("Para {} is present".format(key))
                self.valid = True
            else:
                self.valid = False
                return self.valid
                # print("Para {} is not present".format(key))
        # print("passport valid= {}".format(str(self.valid)))
        return self.valid

    def validate_data(self):
        if self.valid:
            for key in self.data:
                print(self.valid)
                data = self.data[key]
                print("{} with data: {}".format(key, data))
                if key == "byr":
                    if date_val(key,data,1920, 2002):
                        continue
                    else:
                        self.valid = False
                        continue
                if key == "iyr":
                    if date_val(key, data, 2010, 2020):
                        continue
                    else:
                        self.valid = False
                        continue
                if key == "eyr":
                    if date_val(key,data,2020, 2030):
                        continue
                    else:
                        self.valid = False
                        continue
                if key == "hgt":
                    if data[-2:] == "cm" and test_int(data[:-2]) and 150 <= int(data[:-2]) <= 193:

                        print("{} is valid".format(key))
                        continue
                    elif data[-2:] == "in" and test_int(data[:-2]) and 59 <= int(data[:-2]) <= 76:
                        print("{} is valid".format(key))
                        continue

                    else:
                        self.valid = False
                        print("{} not valid".format(key))
                        continue
                if key == "hcl":
                    if data[0] == "#" and len(data[1:]) == 6:
                        print("passed first")
                        if test_hcl(data[-1:]):
                            print("{} is valid".format(key))
                            continue
                        else:
                            self.valid = False
                            print("{} not valid".format(key))
                            continue
                    else:
                        self.valid = False
                        print("{} not valid".format(key))
                        continue
                if key == "ecl":
                    dict_ecl = "amb blu brn gry grn hzl oth"
                    if data in dict_ecl:
                        print("{} is valid".format(key))
                        continue
                    else:
                        print("{} not valid".format(key))
                        self.valid = False
                        continue
                if key == "pid":
                    if test_int(data) and len(data) == 9:
                        print("{} is valid".format(key))
                        continue
                    else:
                        self.valid = False
                        print("{} not valid".format(key))
                        continue

        print("pasport passed {}".format(self.valid))
        return self.valid


print(check())
