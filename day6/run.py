def run():
    initial_gen = read_input()

    sim80 = simulate_days(initial_gen, 80)
    sim256 = simulate_days(initial_gen, 256)

    print(f"ans 1: {sim80}")
    print(f"ans 2: {sim256}")


def read_input():
    with open("input.txt") as f:
        fishes = f.read().strip().split(",")
    return [int(f) for f in fishes]


def simulate_days(initial_gen, num_days):
    return sum(after_days(t, num_days) for t in initial_gen)


def cached(f):
    cache = {}

    def wrapped(*args):
        if not args in cache:
            cache[args] = f(*args)
        return cache[args]

    return wrapped


@cached
def after_days(timer, num_days):
    spawn_days = list(range(timer + 1, num_days + 1, 7))

    return 1 + sum(after_days(d + 8, num_days) for d in spawn_days)
