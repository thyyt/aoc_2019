import click
import numpy as np
import pandas as pd


def fuel_counter(masses):
    return np.floor(masses / 3) - 2


@click.command()
@click.option("--masses", help="Input file")
def count_fuel_requirement(masses):
    mass_df = pd.read_csv(masses, names=["mass"])
    mass_df.loc[:, "fuel_requirement"] = mass_df.mass.apply(fuel_counter)


if __name__ == "__main__":
    required_fuel = count_fuel_requirement()
    print(f"Total fuel required: {required_fuel}")
