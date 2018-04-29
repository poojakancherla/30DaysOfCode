def vin():
    s = input()
    invalid_strings = ['$', '#', '%', '1000test', 'notavin', 'something']
    if len(s) != 17:
        print("INVALID")
        return
    else:
        for i in invalid_strings:
            if i in s:
                print("INVALID")
                return
    print("VALID")

vin()
