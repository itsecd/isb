def get_check_digit(sequence_numbers: int, modulus: int = 10) -> int:

    if sequence_numbers < 0:
        raise ValueError("This is not a sequence of numbersя: the number is negative")

    sum = 0
    even = True

    while sequence_numbers > 0:
        digit = 2 * (sequence_numbers % 10) if even else sequence_numbers % 10
        sum += digit if digit < 10 else sum_sequence(digit)
        even = not even
        sequence_numbers //= 10

    return (modulus - sum % modulus) % modulus

        
def sum_sequence(sequence_numbers: int):
    
    if sequence_numbers < 0:
        raise ValueError("This is not a sequence of numbers, the number is negative")
    
    sum = 0

    while sequence_numbers > 0:
        sum += sequence_numbers % 10
        sequence_numbers //= 10
    
    return sum


print(get_check_digit(5511792468029858))
print(get_check_digit(5308895034093956))
print(get_check_digit(5273430260826183))
print(get_check_digit(5380973562693777))