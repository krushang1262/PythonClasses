import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

df = pd.read_csv('~/Desktop/Task Data set/social_media_user_behavior.csv')
# df.shape
# df.head(10)
# df.isnull()
# df.info()
df.duplicated()

# # 1 Education Level & Relationship Status Count

agGrop = df.groupby(['education_level','relationship_status'])['age_group'].count().reset_index()
print(agGrop)
plt.figure(figsize=(10,6))
sbn.barplot(data=agGrop, x='education_level', y='age_group', hue='relationship_status')
plt.title('Education Level & Relationship Status Count.')
plt.xticks(rotation=10)
plt.show()

# # 2 Average Number of Platforms Used 

avgPlatform = df.groupby(['age_group','relationship_status','primary_platform'])['num_platforms_used'].mean().reset_index()
print(avgPlatform)

plt.figure(figsize=(10,6))
sbn.barplot(data=avgPlatform, x='relationship_status', y='num_platforms_used', hue='age_group')
plt.title('Average Number of Platforms Used')
plt.xticks(rotation=10)
plt.show()

# # 3 Platforms Used vs Daily Screen Time

rec = df.groupby('num_platforms_used')['daily_screen_time_minutes'].mean().reset_index()
plt.figure(figsize=(10,6))
plt.title('Platforms Used vs Daily Screen Time')
plt.scatter(rec['num_platforms_used'],rec['daily_screen_time_minutes'], marker='o', color='purple')
plt.xlabel('number of platform')
plt.ylabel('daily screen time')
plt.xticks(rotation=10)
plt.show()

# # 4 Primary Platform vs Daily Screen Time

dta = df.groupby('primary_platform')[['daily_screen_time_minutes','avg_session_duration_minutes']].mean().reset_index()
print(dta)
plt.figure(figsize=(10,6))
plt.title('Primary Platform vs Daily Screen Time')
sbn.barplot(data=dta, x='primary_platform', y='daily_screen_time_minutes')
plt.xlabel('Primary platform')
plt.ylabel('Daily screen time and average session duration mins')
plt.xticks(rotation=30)
plt.show()

# # 5 Device & Content Type vs Weekly Sessions

prefCont = df.groupby(['primary_device','preferred_content_type'])['weekly_sessions'].max().reset_index()
print(prefCont)
plt.figure(figsize=(10,6))
plt.title('Device & Content Type vs Weekly Sessions')
sbn.barplot(data=prefCont, x='preferred_content_type', y='weekly_sessions', hue='primary_device')
plt.ylabel('max weekly sessions')
plt.xticks(rotation=30)
plt.show()

# # 6 Follwers Count and Following Count

fcot = df.groupby('primary_platform')[['followers_count','following_count']].sum().reset_index()
print(fcot)

plt.figure(figsize=(10,6))
plt.title('Follwers Count')
plt.pie(fcot['followers_count'], labels=fcot['primary_platform'], autopct='%0.2f%%')
plt.show()

plt.title('Following Count')
plt.pie(fcot['following_count'], labels=fcot['primary_platform'], autopct='%0.2f%%')
plt.show()

# # 7 sum of post per week, like per day, cmt per day, shares per week

pstwk = df.groupby('primary_platform')[['posts_per_week','likes_per_day','comments_per_day','shares_per_week']].sum().reset_index()
pstwk = pstwk.set_index('primary_platform')
print(pstwk,'\n')
plt.figure(figsize=(10,6))
plt.title('sum of post per week, like per day, cmt per day, shares per week')
sbn.heatmap(pstwk, annot=True, cmap='Blues_r', fmt='d', linewidths=2)
plt.show()

# # 8 Notifications & Productivity Impact
pss = df.groupby(['primary_platform','platform_satisfaction','productivity_impact'])[['daily_notifications','uses_screen_time_limits','checks_phone_first_morning']].max()
pss = pss.reset_index()
print(pss)

plt.figure(figsize=(10,6))
sbn.barplot(pss, x='platform_satisfaction', y='daily_notifications', hue='productivity_impact')
plt.title('Notifications & Productivity Impact')
plt.ylabel('max notification screen time & check phone in morning')
plt.xticks(rotation=10)
plt.show()

# # 9 find the Addiction Level of Users

records = df.groupby(['user_id', 'primary_platform', 'age'])[['sleep_hours_per_night', 'addiction_level_1_to_10']].mean().reset_index().head(25)
print(records)
plt.figure(figsize=(10,6))
plt.title('Addiction Level of Users', fontsize=14)
sbn.barplot(data=records,x='user_id',y='addiction_level_1_to_10',palette='Set2',hue='primary_platform')
plt.xlabel('User ID')
plt.ylabel('Addiction Level')
plt.xticks(rotation=90)
plt.show()