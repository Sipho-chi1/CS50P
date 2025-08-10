def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum() and s[0:2].isalpha():
        for x in range(len(s)):
            if s[x].isdigit():
                if s[x] == '0':
                    return False
                if not s[x:].isdigit():
                    return False
                break
        return True
    return False

main()