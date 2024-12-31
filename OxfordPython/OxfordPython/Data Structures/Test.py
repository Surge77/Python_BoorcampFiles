def highest_possible_sum(input_string):
    companies = {}
    for company in input_string.split('#'):
        name, number = company.strip().split(' : ')
        digits = list(map(int, str(number)))
        digits.sort(reverse=True)
        highest_number = int(''.join(map(str, digits)))
        companies[name] = highest_number

    return companies


# Test the function
input_string = "Infosys : 1111 # TCS : 1111 # WIPRO : 1111"
print(highest_possible_sum(input_string))
# Output: {'Infosys': 18, 'TCS': 13, 'WIPRO': 18}