import random
from period import find_period


def rand(): return int(random.random()*10)


# the number must have at least one unique digit, 4444 is incorrect
def is_correct(array): return True if len(list(dict.fromkeys(array))) > 1 else False


def create_number(N):
    number = 0
    while number < 10 ** (N - 1):
        r_n = rand()
        number = number * 10 + r_n
    return number


def compose_number(digits):
    number = 0
    for d in digits:
        number = number * 10 + d
    return number


def distract_sort_compose(digits):
    digits.sort()
    small_number = compose_number(digits)
    digits.sort(reverse=True)
    big_number = compose_number(digits)
    difference = big_number - small_number
    return difference


def get_digits(number): return list(map(int, str(number)))


def process(N, R):
    results = []
    number = create_number(N)
    digits = get_digits(number)
    while not is_correct(digits):
        number = create_number(N)
        digits = get_digits(number)
    print("Experiment number", number)
    difference = distract_sort_compose(digits)
    results.append(difference)
    while len(results) < 2 or results[-1] != results[-2]:
        if len(results) > R:
            string_number = ""
            for i in results:
                string_number += str(i)
            period = find_period(string_number)
            if period == 0:
                print("No repeated period")
            else:
                print("Repeated period is", period)
            return period
        digits = get_digits(results[-1])
        difference = distract_sort_compose(digits)
        results.append(difference)
    print("The number", number, "got to point", results[-1], "by", len(results), "steps")
    return results[-1]


if __name__ == "__main__":
    N = 21   # number of digits in number
    R = 500  # how many distracts do if there is no obvious point
    A = 300  # number of experiments with numbers of the same amount of digits

    results = [process(N, R) for i in range(A)]
    print(results)



