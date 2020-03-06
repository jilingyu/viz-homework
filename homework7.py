#!/usr/bin/env python3

import os

import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv(filepath_or_buffer='toys-datasets/diabetes.data',
                      sep='\t',
                      header=0)

os.makedirs('plots/items', exist_ok=True)

# Another useful dataset exploration technique involves comparing multiple columns of the dataset
# The enumerate functions will generate pairs of indexes elements
plt.style.use("ggplot")

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

# This time we plot multiple plots on the same axes, to get some perspective on their comparisons
axes.scatter(df['AGE'], df['SEX'], alpha=0.7, label='age vs sex')
axes.scatter(df['AGE'], df['BMI'], alpha=0.7, label='AGE VS BMI')
axes.scatter(df['AGE'], df['BP'], alpha=0.7, label='age vs bp')

axes.set_xlabel('age')
axes.set_ylabel('sex/bmi/bp')
axes.set_title(f'plot for diabetes')
axes.legend()
plt.savefig(f'plots/items/item1.png', dpi=300)

plt.close()