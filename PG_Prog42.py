import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Hide axes without removing it:
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

# Create a numpy random array in a pandas dataframe with 10 rows, 4 columns:
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

plt.title("Pandas Dataframe Plot")
ax.table(cellText=df.values, colLabels=df.columns, loc='center')

fig.tight_layout()

plt.show()

plt.savefig('histogram.png')
