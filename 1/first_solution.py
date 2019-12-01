import click
import numpy as np
import pandas as pd


def fuel_counter(masses):
    return int(np.floor(masses / 3) - 2)


@click.command()
@click.option("--masses", help="Input file")
def count_fuel_requirement(masses):
    mass_df = pd.read_csv(masses, names=["mass"])
    mass_df.loc[:, "fuel_requirement"] = mass_df.mass.apply(fuel_counter)
    required_fuel = mass_df.fuel_requirement.sum()
    print(f"Total fuel required: {required_fuel}")


if __name__ == "__main__":
    count_fuel_requirement()
