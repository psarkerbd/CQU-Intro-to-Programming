def ticket_price(age, is_member):
    if is_member:
        return 7
    elif not age > 12:
        return 5
    elif age >= 60:
        return 6
    else:
        return 10
    
def process_transactions(transactions):
    return [x**2 for x in transactions if x >= 100 or x <= -100]

def extract_acronyms(product_name):
    chars = ''.join([s[0].upper() for s in product_name.split()])
    return chars

def multiply_vectors(row_vector, col_vector):
    p = len(row_vector)
    q = len(col_vector)
    if p == q:
        res = 0
        for i in range(p):
            res = res + (row_vector[i] * col_vector[i])
        return res
    else:
        return "The vectors must be of the same length."


if __name__ == "__main__":
    #print(ticket_price(10, False))
    #print(ticket_price(65, False))
    #print(process_transactions([50, -200, 100, -150, 75]))
    #print(process_transactions([0, 99, 101, -101]))
    #print(extract_acronyms("advanced micro Devices"))
    #print(extract_acronyms("international business machines"))
    #print(extract_acronyms("graphic Processing unit"))
    print(multiply_vectors([1, 2, 3], [4, 5, 6]))
    print(multiply_vectors([-1, -2, -3], [-4, -5, -6]))
    print(multiply_vectors([7, 8], [9, 10]))
