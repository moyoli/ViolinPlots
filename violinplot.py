import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("PSL_Violin_Plot_Ages.csv")
CSLcols = ("#FF0000", "#9A050A", "#112987", "#00A4FA", "#FF6600", "#008040", "#004EA1", "#5B0CB3", "#E50211", "#FF0000",
           "#00519A",  "#75A315", "#E70008", "#E40000", "#C80815", "#FF3300")
CSLPalette = sns.color_palette(CSLcols)
fig,ax = plt.subplots()
fig.set_size_inches(20, 8)
ax= sns.violinplot(x="Club",y="Age",data=data)
ax.set_title("Violin Plot for PSL Squads 2019/20")
plt.xticks(rotation=65)
plt.show()



