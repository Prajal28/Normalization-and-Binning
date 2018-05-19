import pandas as ps
import matplotlib.pyplot as plt
data = ps.read_csv('D:\\UTA\\2nd Sem\\Data Mining\\Homework\\Assignment 03\\cycling\\dataset1.csv',skiprows=0)
#for normalizing by columns uncomment the following code (min-max normalization)
#cols_to_norm = ['avg_rss12','var_rss12']
#data[cols_to_norm] = data[cols_to_norm].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

#for normalizing whole dataset using min-max normalization
data = data.apply(lambda x: (x - x.min()) / (x.max() - x.min()))

print(data)

#for binning by equal-width partitioning on column avg_rss13
data = ps.read_csv('D:\\UTA\\2nd Sem\\Data Mining\\Homework\\Assignment 03\\cycling\\dataset1.csv',skiprows=0)
bins = [5.5, 9.75, 14, 18.25, 22.5, 26.75]
bin_name = ['5.5-9.75','9.75-14','14-18.25','18.25-22.5','22.5-26.75']
bin_column = ps.cut(data['avg_rss13'], bins, labels=bin_name)
data['bin_column'] = ps.cut(data['avg_rss13'], bins, labels=bin_name)
print(ps.value_counts(data['bin_column']))

print(data)

df = ps.value_counts(data['bin_column'])
ax = df.plot(kind='bar')
ax.set_xlabel("Bins")
ax.set_ylabel("Frequency")
plt.show()

