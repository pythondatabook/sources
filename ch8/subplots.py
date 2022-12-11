# pp 134

# importing modules
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
# data to plot
salaries = [1215, 1221, 1263, 1267, 1271, 1274, 1275, 1318, 1320, 1324, 1324, 1326, 1337, 1346, 1354, 1355, 1364, 1367, 1372, 1375, 1376, 1378, 1378, 1410, 1415, 1415, 1418, 1420, 1422, 1426, 1430, 1434, 1437, 1451, 1454, 1467, 1470, 1473, 1477, 1479, 1480, 1514, 1516, 1522, 1529, 1544, 1547, 1554, 1562, 1584, 1595, 1616, 1626, 1717]
# preparing a histogram
fig, ax = plt.subplots()
fig.set_size_inches(5.6, 4.2)
ax.hist(salaries, bins=np.arange(1100, 1900, 50), edgecolor='black',linewidth=1.2)
formatter = ticker.FormatStrFormatter('$%1.0f')
ax.xaxis.set_major_formatter(formatter)
plt.title('Monthly Salaries in the Sales Department')
plt.xlabel('Salary (bin size = $50)')
plt.ylabel('Frequency')
# showing the histogram
plt.show()

