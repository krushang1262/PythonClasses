import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

df = pd.read_csv('~/Desktop/Task Data set/social_media_user_behavior.csv')
# df.shape
# df.head(10)
# df.isnull()
# df.info()
df.duplicated()

# 1 sum of post per week, like per day, cmt per day, shares per week

pstwk = df.groupby('primary_platform')[['posts_per_week','likes_per_day','comments_per_day','shares_per_week']].sum().reset_index()
pstwk = pstwk.set_index('primary_platform')
print(pstwk,'\n')
plt.figure(figsize=(10,6))
plt.title('sum of post per week, like per day, cmt per day, shares per week')
sbn.heatmap(pstwk, annot=True, cmap='Blues_r', fmt='d', linewidths=2)
plt.show()