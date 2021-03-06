# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers
#
#
# numbers = get_prime_numbers(20)
# print(numbers)


class PrimeNumbers:

    def __init__(self, n):
        self.n, self.i, self.prime_numbers = n, 0, []

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.n:
            raise StopIteration()
        else:
            for prime in self.prime_numbers:
                if self.i % prime == 0:
                    break
            else:
                self.prime_numbers.append(self.i)
                return self.i


prime_number_iterator = PrimeNumbers(n=10)
for number in prime_number_iterator:
    print(number)
