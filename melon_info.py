"""Print out all the melons in our inventory."""

from melons import melons


def print_melon(melons):
    """Print each melon with corresponding attribute information."""

    for key, value in melons.items():
            print(f"{key.upper()}")
            for attribute, value in value.items():
                print(f"    {attribute}:{value}")
            print()    


print_melon(melons)
