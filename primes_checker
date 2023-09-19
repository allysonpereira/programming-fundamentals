#Prime Numbers code practice

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for current in range(2, int(limit**0.5) + 1):
        if sieve[current]:
            for multiple in range(current * current, limit + 1, current):
                sieve[multiple] = False

    primes = [number for number, is_prime in enumerate(sieve) if is_prime]
    return primes

def get_positive_integer_input():
    while True:
        try:
            user_input = input("Enter a positive integer (type 'quit' to exit): ")
            if user_input.lower() == 'quit':
                return None
            user_input = int(user_input)
            if user_input > 0:
                return user_input
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    while True:
        users_number = get_positive_integer_input()
        if users_number is None:
            break  # Exit the loop if the user types 'quit'
        primes = sieve_of_eratosthenes(users_number)
        print("Prime numbers up to", users_number, "are:", primes)

if __name__ == "__main__":
    main()







# def showprimes(test):
#     prime_list = []
#     not_prime_list = []
#     for item in range(2, test+1):
#         if item not in not_prime_list:
#             prime_list.append(item)
#             for item2 in range(item*item, test+1, item):
#                 not_prime_list.append(item2)

#     return prime_list


# users_number = int(input("Enter the number you want to see all prime numbers up to: "))

# print(showprimes(users_number))




