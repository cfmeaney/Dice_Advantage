# Generalized Advantage With Advantage Calculator

This small Python script computes the expected value of the maximum result obtained when rolling multiple identical dice. This was motivated by the common situation of this (with a d20) that occurs in Dungeons and Dragons 5e. Instead of using simulation or Monte Carlo sampling, it uses a closed-form algebraic solution, making it fast and exact even for large numbers of dice.

## Calculation

If you roll **d** dice and each die has **N** sides, and you **keep only the highest value**, the expected value is:

\[
E[\max] = \sum_{n=1}^{N} n \cdot P(\text{max} = n)
\]

where

\[
P(\text{max} = n) = \left(\frac{n}{N}\right)^d - \left(\frac{n-1}{N}\right)^d
\]

## Usage

Run the script with Python:

```bash
python script_name.py
```

You will be prompted for:

```
How many sides are on the die?
How many dice are being rolled?
```

Example:

```
How many sides are on the die? 20
How many dice are being rolled? 2
```

Output:

```
The average is 13.825
```
