import pandas as pd
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt

df = pd.read_csv("processed_data.csv")
cols = df.columns
for col in cols:
    plt.plot(df[col],label=col)

plt.gca().invert_yaxis()
plt.xlabel('5s')
plt.ylabel('settlement mm')
plt.legend()
plt.savefig('fen_result.png')
#plt.show()
