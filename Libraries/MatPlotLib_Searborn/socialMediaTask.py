import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

df = pd.read_csv('~/Desktop/Task Data set/social_media_user_behavior.csv')
# df.shape
# df.head(10)
# df.isnull()
# df.info()
df.duplicated()

# age group & relationship status wise education level count

# agGrop = df.groupby(['education_level','relationship_status'])['age_group'].count().reset_index()
# print(agGrop)
# plt.figure(figsize=(10,6))
# sbn.lineplot(agGrop, x='education_level', y='age_group', hue='relationship_status',markers='o')
# plt.title('age group & relationship status wise education level count')
# plt.xticks(rotation=10)
# plt.show()

# agegroup and relationship status wise avg num of primary_platform 

# avgPlatform = df.groupby(['age_group','relationship_status','primary_platform'])['num_platforms_used'].sum().reset_index()
# print(avgPlatform)

# plt.figure(figsize=(10,6))
# sbn.barplot(data=avgPlatform, x='relationship_status', y='num_platforms_used', hue='age_group')
# plt.title('agegroup and relationship status wise avg num of platform')
# plt.xticks(rotation=10)
# plt.show()

# num_platforms_used and avg daily_screen_time_minutes

# rec = df.groupby('num_platforms_used')['daily_screen_time_minutes'].mean().reset_index()
# plt.figure(figsize=(10,6))
# plt.title('number of platforms used to avg daily screen time minutes')
# plt.scatter(rec['num_platforms_used'],rec['daily_screen_time_minutes'], marker='o', color='purple')
# plt.xlabel('number of platform')
# plt.ylabel('daily screen time')
# plt.xticks(rotation=10)
# plt.show()

# use of primaryplatform to daily screen time

# dta = df.groupby('primary_platform')[['daily_screen_time_minutes','avg_session_duration_minutes']].mean().reset_index()
# print(dta)
# plt.figure(figsize=(10,6))
# plt.title('use of primary platform to daily screen time')
# sbn.kdeplot(data=dta, color='darkblue', fill=True)
# plt.xlabel('Primary platform')
# plt.ylabel('Daily screen time and average session duration mins')
# plt.show()

# primary device preferred_content_type wise avg weekly_sessions

# prefCont = df.groupby(['primary_device','preferred_content_type'])['weekly_sessions'].mean().reset_index()
# print(prefCont)
# plt.figure(figsize=(10,6))
# plt.title('primary device preferred_content_type wise avg weekly_sessions')
# sbn.histplot(data=prefCont,x='weekly_sessions',hue='preferred_content_type',kde=True)
# plt.show()

# Follwers Count and Following Count

# fcot = df.groupby('primary_platform')[['followers_count','following_count']].count().reset_index()
# print(fcot)

# plt.figure(figsize=(10,6))
# plt.title('Follwers Count')
# plt.pie(fcot['followers_count'], labels=fcot['primary_platform'], autopct='%0.2f%%')
# plt.show()

# plt.title('Following Count')
# plt.pie(fcot['following_count'], labels=fcot['primary_platform'], autopct='%0.2f%%')
# plt.show()

# sum of post per week, like per day, cmt per day, shares per week

# pstwk = df.groupby('primary_platform')[['posts_per_week','likes_per_day','comments_per_day','shares_per_week']].sum().reset_index()
# pstwk = pstwk.set_index('primary_platform')
# print(pstwk,'\n')
# plt.figure(figsize=(10,6))
# plt.title('sum of post per week, like per day, cmt per day, shares per week')
# sbn.heatmap(pstwk, annot=True, cmap='Blues_r', fmt='d', linewidths=2)
# plt.show()

# agg func Daily Notifications, Screen Time, Morning Phone Check with Primary Platform, Satisfaction, Productivity Impact
pss = df.groupby(['primary_platform','platform_satisfaction','productivity_impact'])[['daily_notifications','uses_screen_time_limits','checks_phone_first_morning']].agg({'daily_notifications':'count','uses_screen_time_limits':'mean','checks_phone_first_morning':'max'})
print(pss)

plt.figure(figsize=(10,6))
sbn.barplot(pss, x='platform_satisfaction', y='daily_notifications', hue='productivity_impact')
plt.title(' Daily Notifications, Screen Time, Morning Phone Check with Primary Platform, Satisfaction, Productivity Impact aggerate')
plt.xticks(rotation=10)
plt.show()