# pp 189 - 191

import pandas as pd
df_retail = pd.read_excel('https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx', index_col=0, engine='openpyxl') 

print('The number of instances: ', len(df_retail)) 
print(df_retail.head())

df_retail = df_retail.dropna(subset=['Description'])
df_retail = df_retail.astype({"Description":'str'})

trans = df_retail.groupby(['InvoiceNo'])['Description'].apply(list).to_list()

from mlxtend.preprocessing import TransactionEncoder
encoder = TransactionEncoder()
encoded_array = encoder.fit(trans).transform(trans) 
df_itemsets = pd.DataFrame(encoded_array, columns=encoder.columns_)

from mlxtend.frequent_patterns import apriori
frequent_itemsets = apriori(df_itemsets, min_support=0.025, use_colnames=True) 

from mlxtend.frequent_patterns import association_rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3) 

print(rules.iloc[:,0:7])
print(rules.iloc[:,2:7])
