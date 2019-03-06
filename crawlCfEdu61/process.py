import pandas as pd
file_name = r'C:\Users\Administrator\Desktop\crawlCfEdu61\CfEdu61.csv'
names = ['rank','name','number_solved','penalty','success_hacks/fail_hacks','A','B','C','D','E','F','G']
data = pd.DataFrame(pd.read_csv(file_name,header=None,names=names))
new_data = data.sort_values(by=['rank'],ascending=True)
new_data = new_data.reset_index(drop=True)
new_data.to_csv('../sorted.csv')