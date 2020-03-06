import os

import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv(filepath_or_buffer='toys-datasets/diabetes.data',
                      sep='\t',
                      header=0)

os.makedirs('plots/items', exist_ok=True)

fig, axes = plt.subplots(2, 2, figsize=(8,8))

axes[0][0].scatter(df['AGE'], df['SEX'], alpha=0.7, label='age vs sex')
axes[0][1].scatter(df['AGE'], df['BMI'], alpha=0.7, label='AGE VS BMI')
axes[1][0].scatter(df['AGE'], df['BP'], alpha=0.7, label='age vs bp')


plt.savefig(f'plots/items/item2.png', dpi=300)

plt.close()