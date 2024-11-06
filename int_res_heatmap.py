import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(sys.argv[1], index_col=0) # import and read  input file (csv)

plt.figure(figsize=(16, 14))
heatmap=sns.heatmap(df, annot=False, cmap='Greens', fmt='d', linewidths=1, linecolor='white')
plt.yticks(rotation=0)

cbar = heatmap.collections[0].colorbar  # show the color bar
cbar.ax.yaxis.set_tick_params(length=6, width=3) # obtain tick labels
for l in cbar.ax.yaxis.get_ticklabels():
    l.set_weight("bold") # make labels font bold
    l.set_fontsize(14) # set size of the font

plt.title('Pair-residue occurrence at interface', fontsize=16, fontweight='bold') # get the title settings
plt.xlabel('Antigen residue', fontsize=16, fontweight='bold') # axis x label
plt.ylabel('Antibody residue', fontsize=16, fontweight='bold') #axis y label
plt.xticks(fontweight='bold', fontsize=12) # bold ticks
plt.yticks(fontweight='bold', fontsize=12)
#plt.show()
plt.savefig(sys.argv[2]) #save choosing the file name in the command line
