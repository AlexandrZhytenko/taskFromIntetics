from sympy import sieve
from sympy.utilities.iterables import multiset_combinations
from numpy import prod

def is_palindrome(number):
    s = str(number)
    return s == s[::-1]

def max_palindrome(prime_numbers):
    result = []
    prime_numbers_list_unique_combinations = tuple(multiset_combinations(prime_numbers, 2))
    product_for_each_pair = prod(prime_numbers_list_unique_combinations, axis=1)
    for i in product_for_each_pair:
        if is_palindrome(i):
            result.append((i, prime_numbers_list_unique_combinations[product_for_each_pair.tolist().index(i)]))
    return "The max polindrome is {0} which is producted of {1} and {2} numbers.".format(max(result)[0], \
                                                                                                max(result)[1][0], \
                                                                                                max(result)[1][1])

prime_numbers = (i for i in sieve.primerange(9999, 99999))
print max_palindrome(prime_numbers)
