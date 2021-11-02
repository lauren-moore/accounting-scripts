"""Print out all the melons in our inventory."""


from melons import melon_names


def print_melon(melon_names):
    """Print each melon with corresponding attribute information."""

    for key, value in melon_names.items():
        print(f"{key}")

    # have_or_have_not = 'have'
    # if seedless:
    #     have_or_have_not = 'do not have'

    # print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


for i in melon_names:
    print_melon(melon_names[i])
