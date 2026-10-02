def format_phone_number(number):
    number = number.strip()

    if number.startswith("+254"):
        rest = number[4:]
    elif number.startswith("254"):
        rest = number[3:]
    elif number.startswith("0"):
        rest = number[1:]
    else:
        rest = number

    if len(rest) == 9 and rest.isdigit() and rest[0] in "71":
        return "+254" + rest
    return "Invalid phone number"


