# pp 136

import numpy as np
salaries = [1215, 1221, 1263, 1267, 1271, 1274, 1275, 1318, 1320, 1324, 1324, 1326, 1337, 1346, 1354, 1355, 1364, 1367, 1372, 1375, 1376, 1378, 1378, 1410, 1415, 1415, 1418, 1420, 1422, 1426, 1430, 1434, 1437, 1451, 1454, 1467, 1470, 1473, 1477, 1479, 1480, 1514, 1516, 1522, 1529, 1544, 1547, 1554, 1562, 1584, 1595, 1616, 1626, 1717]
count, labels = np.histogram(salaries, bins=np.arange(1100, 1900, 50))
labels = ['$'+str(labels[i])+'-'+str(labels[i+1]) for i, _ in enumerate(labels[1:])]
non_zero_pos = [i for i, x in enumerate(count) if x != 0]
labels = [e for i, e in enumerate(labels) if i in non_zero_pos]
count = [e for i, e in enumerate(count) if i in non_zero_pos]

lbls = [labels[i] for i,c in enumerate(count) if c>2]
cnt = [c for c in count if c>2]  
cnt.append(sum(count) - sum(cnt))
lbls.append('Others')

from matplotlib import pyplot as plt
plt.pie(cnt, labels=lbls, autopct='%1.1f%%')
plt.title('Monthly Salaries in the Sales Department')
plt.show() 
