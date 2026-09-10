"""A small Python practice script."""


def main():
	a = 10
	b = 15
	username = "lorenzo"
	name = username
	status = "learning python"
	numbers = [1, 2, 3, 4, 5]
	quick_sum = sum(numbers)

	print(f"Hello, {name or 'Python learner'}!")
	print(f"user: {username}")
	print(f"status: {status}")
	print(f"The numbers are: {numbers}")
	print(f"Their sum is: {quick_sum}")
	print(f"sum of {a} + {b} = {a + b}")


if __name__ == "__main__":
	main()
