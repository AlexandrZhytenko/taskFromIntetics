from sympy import sieve
from itertools import combinations_with_replacement

def max_palindrome(prime_numbers):
    prime_numbers_list_unique_combinations = combinations_with_replacement(prime_numbers, 2)
    list_palindromes = ((i * j, i, j) for i, j in prime_numbers_list_unique_combinations if \
                        str(i * j) == str(i * j)[::-1])
    result = max(list_palindromes)
    return "The max palindrome with product numbers {1} and {2} is: {0}".format(result[0], \
                                                                                 result[1], \
                                                                                 result[2])

from timeit import default_timer
start = default_timer()

print max_palindrome((i for i in sieve.primerange(9999, 99999)))
# The max palindrome with product numbers 30109 and 33211 is: 999949999

end = default_timer()
print "The time of max_palindrome program's execution is {} sec".format(end - start)
# The time of max_palindrome program's execution is 60.7272051733 sec