number = int(input())


def isprime(number):
	for i in range(2, int(number ** 1/2) + 1):
		if number % i == 0:
			return False
	return True


print(isprime(number))