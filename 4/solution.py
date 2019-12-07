from collections import Counter

RANGE_LOW = 246540
RANGE_HIGH = 787419


def int_to_password(pw_int):
    password = str(pw_int)
    return (6 - len(password)) * "0" + password


def is_six_digits(password):
    return len(password) == 6


def is_within_range(password, lower, upper):
    return (lower <= int(password)) and (int(password) <= upper)


def has_two_adjacent(password):
    for idx in range(1, len(password)):
        if password[idx] == password[idx - 1]:
            return True


def is_monotonic(password):
    for idx in range(1, len(password)):
        if int(password[idx]) < int(password[idx - 1]):
            return False
    return True


def compute_valid_passwords(low=RANGE_LOW, high=RANGE_HIGH):
    valids = []
    for pw_int in range(low, high + 1):
        password = int_to_password(pw_int)

        if has_two_adjacent(password) and is_monotonic(password):
            valids.append(password)
    return valids


def at_most_two_equal(password):
    counts = Counter(password)
    return counts.most_common(1)[0][1] < 3


def has_double(password):
    counts = Counter(password)
    return 2 in counts.values()


if __name__ == "__main__":
    initial_valid_passwords = compute_valid_passwords()
    print(
        f"Range from {RANGE_LOW} to {RANGE_HIGH} has "
        f"{len(initial_valid_passwords)} initially valid passwords"
    )
    valids = [pw for pw in initial_valid_passwords if has_double(pw)]
    print(f"Out of those, {len(valids)} are actually valid")
