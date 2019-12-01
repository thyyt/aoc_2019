import click
import numpy as np
import pandas as pd


def first_order_fuel_counter(masses):
    return max(int(np.floor(masses / 3) - 2), 0)


def recursive_fuel_counter(module_mass):
    module_fuel = max(int(np.floor(module_mass / 3) - 2), 0)
    if module_fuel == 0:
        return module_fuel
    else:
        return module_fuel + recursive_fuel_counter(module_fuel)


def count_initial_fuel_requirement(masses):
    mass_df = pd.read_csv(masses, names=["mass"])
    mass_df.loc[:, "fuel_requirement"] = mass_df.mass.apply(first_order_fuel_counter)
    required_fuel = mass_df.fuel_requirement.sum()

    return mass_df, required_fuel


def count_total_fuel_requirement(mass_df):
    mass_df.loc[:, "total_fuel_requirement"] = mass_df.mass.apply(
        recursive_fuel_counter
    )
    return mass_df


@click.command()
@click.option("--masses", help="Input file")
def main(masses):
    mass_df, initial_required_fuel = count_initial_fuel_requirement(masses=masses)
    print(f"Initial fuel required: {initial_required_fuel}")

    mass_df = count_total_fuel_requirement(mass_df)
    print(f"Total required fuel: {mass_df.total_fuel_requirement.sum()}")


if __name__ == "__main__":
    main()
