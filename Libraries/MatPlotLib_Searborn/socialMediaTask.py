import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
import seaborn.objects as so

df = pd.read_csv('~/Desktop/Task Data set/social_media_user_behavior.csv')
# df.shape
# df.head(10)
# df.isnull()
# df.info()
df.drop_duplicates()

# 1 Total of post per week, like per day, cmt per day, shares per week

pstwk = df.groupby('primary_platform')[['posts_per_week','likes_per_day','comments_per_day','shares_per_week']].sum().reset_index()
pstwk = pstwk.set_index('primary_platform')
print(pstwk,'\n')
plt.figure(figsize=(10,6))
plt.title('Total`s of post per week, like per day, cmt per day, shares per week')
sbn.heatmap(pstwk, annot=True, cmap='Blues_r', fmt='d', linewidths=2)
plt.show()

# 2  Max Screen time according to country and platfrom they use

trackScreentime = df.groupby(['country','primary_platform'])['daily_screen_time_minutes'].max().reset_index().drop_duplicates().head(70)
print(trackScreentime)

plt.figure(figsize=(10,6))
plt.title("Max Screen time according to country and platfrom they use")
sbn.barplot(data=trackScreentime, x='country', y='daily_screen_time_minutes', hue='primary_platform', palette='pastel')
plt.xlabel('Countries')
plt.ylabel('Max Daily Screen Time')
plt.xticks(rotation=30)
plt.show()

# 3 count followers and following platform they used.

followersfollowingCount = df.groupby('primary_platform')[['followers_count','following_count']].sum().reset_index()
dt = followersfollowingCount.melt(id_vars='primary_platform',
                    value_vars=['followers_count','following_count'],
                    var_name='Type',
                    value_name='count')

print(followersfollowingCount) 

plt.figure(figsize=(10,6))
plt.title("count followers platform they used")
sbn.barplot(data=dt, x='primary_platform', y='count',hue='Type', palette='colorblind')
plt.xlabel('Primary Platform')
plt.ylabel('Count Followers')
plt.xticks(rotation=70)

plt.show()

# 4 avg addiction level according to platform user are used

addLevel = df.groupby(['primary_platform'])['addiction_level_1_to_10'].mean().reset_index()
print(addLevel)

plt.figure(figsize=(10,6))
sbn.barplot(data=addLevel,x='primary_platform',y='addiction_level_1_to_10',palette='Set2')

plt.title("Average Addiction Level by Platform")
plt.xlabel("Platform")
plt.ylabel("Avg Addiction Level (1–10)")
plt.xticks(rotation=30)

plt.show()