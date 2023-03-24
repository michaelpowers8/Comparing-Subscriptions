#!/usr/bin/env python
# coding: utf-8

# Hello Michael!
# 
# My name is Dmitry.  I'm glad to review your work today.
# I will mark your mistakes and give you some hints how it is possible to fix them. We are getting ready for real job, where your team leader/senior colleague will do exactly the same. Don't worry and study with pleasure! 
# 
# Below you will find my comments - **please do not move, modify or delete them**.
# 
# You can find my comments in green, yellow or red boxes like this:
# 
# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Success. Everything is done succesfully.
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Remarks. Some recommendations.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Needs fixing. The block requires some corrections. Work can't be accepted with the red comments.
# </div>
# 
# You can answer me by using this:
# 
# <div class="alert alert-block alert-info">
# <b>Student answer.</b> <a class="tocSkip"></a>
# 
# Text here.
# </div>

# # Which one is a better plan?
# 
# You work as an analyst for the telecom operator Megaline. The company offers its clients two prepaid plans, Surf and Ultimate. The commercial department wants to know which of the plans brings in more revenue in order to adjust the advertising budget.
# 
# You are going to carry out a preliminary analysis of the plans based on a relatively small client selection. You'll have the data on 500 Megaline clients: who the clients are, where they're from, which plan they use, and the number of calls they made and text messages they sent in 2018. Your job is to analyze the clients' behavior and determine which prepaid plan brings in more revenue.

# [We've provided you with some commentary to guide your thinking as you complete this project. However, make sure to remove all the bracketed comments before submitting your project.]
# 
# [Before you dive into analyzing your data, explain for yourself the purpose of the project and actions you plan to take.]
# 
# [Please bear in mind that studying, amending, and analyzing data is an iterative process. It is normal to return to previous steps and correct/expand them to allow for further steps.]

# # Comparing Subscription Plans

# # I have spent about 25 hours on this, I know I have a lot to work on, but I really want feedback on what I have. Sorry for the low quality first draft.

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Don't worry, we will handle this project =)
# </div>

# ## Initialization

# 

# In[1]:


# Loading all the libraries
import pandas as pd
import numpy as np
import datetime as dt
from scipy import stats as st
from matplotlib import pyplot as plt
import math


# ## Load data

# 

# In[2]:


# Load the data files into different DataFrames

df_calls = pd.read_csv('/datasets/megaline_calls.csv')
df_internet = pd.read_csv('/datasets/megaline_internet.csv')
df_messages = pd.read_csv('/datasets/megaline_messages.csv')
df_plans = pd.read_csv('/datasets/megaline_plans.csv')
df_users = pd.read_csv('/datasets/megaline_users.csv')


# ## Prepare the data

# [The data for this project is split into several tables. Explore each one to get an initial understanding of the data. Do necessary corrections to each table if necessary.]

# In[3]:


display(df_calls.info())
display(df_calls.head())


# In[4]:


display(df_internet.info())
display(df_internet.head())


# In[5]:


display(df_messages.info())
display(df_messages.head())


# In[6]:


display(df_plans.info())
display(df_plans.head())


# In[7]:


display(df_users.info())
display(df_users.head())


# The data frame for users seems to have many empty cells in the churn date column. All columns in all data frames are properly named using all lowercase letters and underscores. Everything else in all other data frames seems fine initially. I will search for duplicates or needed conversions below.

# ## Plans

# In[8]:


# Print the general/summary information about the plans' DataFrame
display(df_plans)
display(df_plans.info())


# In[9]:


# Print a sample of data for plans
display(df_plans)


# All of the nexessary information for each plan seems to be included. The only thing that may be confusing to customers would be seeing the cost per gb, message, and minute. Some may think that's included in the package, and not the costs after going over the monthly plan. I am not sure how I would change it, so for now I will leave it how it is.

# [Describe what you see and notice in the general information and the printed data sample for the above price of data. Are there any issues (inappropriate data types, missing data etc) that may need further investigation and changes? How that can be fixed?]

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Great start!
# </div>

#  

# ## Fix data

# [Fix obvious issues with the data given the initial observations.]

# In[10]:


df_users['churn_date'] = pd.to_datetime(df_users['churn_date'],format='%Y-%m-%d')
df_users['churn_date'] = df_users['churn_date'].fillna('Unknown')
display(df_users.head(20))


# In[ ]:





# In[11]:


display(df_calls.duplicated().sum())
display(df_internet.duplicated().sum())
display(df_messages.duplicated().sum())
display(df_plans.duplicated().sum())
display(df_users.duplicated().sum())


# No obvious duplicate rows have been found in any row of any data frame. Under the city, there are several cities and corresponding states that need to 

# In[12]:


display(df_users[(df_users['first_name'].duplicated()) & (df_users['last_name'].duplicated())])


# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Well done!
# </div>

# ## Enrich data

# [Add additional factors to the data if you believe they might be useful.]

# In[ ]:





# ## Users

# In[13]:


# Print the general/summary information about the users' DataFrame
display(df_users.info())
display(df_users.head())


# In[14]:


# Print a sample of data for users

display(df_users.sample(10))


# In[ ]:





# [Describe what you see and notice in the general information and the printed data sample for the above price of data. Are there any issues (inappropriate data types, missing data etc) that may need further investigation and changes? How that can be fixed?]

#  

# ### Fix Data

# [Fix obvious issues with the data given the initial observations.]

# In[15]:


df_users['reg_date'] = pd.to_datetime(df_users['reg_date'],format='%Y-%m-%d')


# ### Enrich Data

# [Add additional factors to the data if you believe they might be useful.]

# In[16]:


df_users['month'] = df_users['reg_date'].dt.strftime("%Y-%m")
display(df_users.head())


# ## Calls

# In[17]:


# Print the general/summary information about the calls' DataFrame
display(df_calls.info())
display(df_calls.describe())


# In[18]:


# Print a sample of data for calls
display(df_calls.head(10))


# [Describe what you see and notice in the general information and the printed data sample for the above price of data. Are there any issues (inappropriate data types, missing data etc) that may need further investigation and changes? How that can be fixed?]

#  

# ### Fix data

# [Fix obvious issues with the data given the initial observations.]

# In[ ]:





# ### Enrich data

# [Add additional factors to the data if you believe they might be useful.]

# In[19]:


df_calls['duration'] = df_calls['duration'].apply(np.ceil)
df_calls['call_date'] = pd.to_datetime(df_calls['call_date'], format='%Y-%m-%d')
df_calls['month'] = df_calls['call_date'].dt.strftime("%Y-%m")
display(df_calls.groupby('month')['duration'].sum())


# ## Messages

# In[20]:


# Print the general/summary information about the messages' DataFrame
display(df_messages.info())
display(df_messages.describe())


# In[21]:


# Print a sample of data for messages

df_messages.sample(10)


# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Pro tip: we do not need print() or display() here. We can use just df.sample()/df.head().
# </div>

# [Describe what you see and notice in the general information and the printed data sample for the above price of data. Are there any issues (inappropriate data types, missing data etc) that may need further investigation and changes? How that can be fixed?]

#  

# ### Fix data

# [Fix obvious issues with the data given the initial observations.]

# In[ ]:





# ### Enrich data

# [Add additional factors to the data if you believe they might be useful.]

# In[22]:


df_messages['message_date'] = pd.to_datetime(df_messages['message_date'],format='%Y-%m-%d')
df_messages['month'] = df_messages['message_date'].dt.month
display(df_messages)


# ## Internet

# In[23]:


# Print the general/summary information about the internet DataFrame

display(df_internet.info())
display(df_internet.describe())


# In[24]:


# Print a sample of data for the internet traffic

display(df_internet.sample(10))


# [Describe what you see and notice in the general information and the printed data sample for the above price of data. Are there any issues (inappropriate data types, missing data etc) that may need further investigation and changes? How that can be fixed?]

#  

# ### Fix data

# [Fix obvious issues with the data given the initial observations.]

# In[ ]:





# ### Enrich data

# [Add additional factors to the data if you believe they might be useful.]

# In[25]:


df_internet['session_date'] = pd.to_datetime(df_internet['session_date'],format='%Y-%m-%d')
df_internet['month'] = df_internet['session_date'].dt.month
display(df_internet)


# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Pro tip: we can get month in this way: df_internet['session_date'].dt.month
# </div>

# ## Study plan conditions

# [It is critical to understand how the plans work, how users are charged based on their plan subscription. So, we suggest printing out the plan information to view their conditions once again.]

# In[26]:


# Print out the plan conditions and make sure they are clear for you

display(df_plans)


# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Good job!
# </div>

# ## Aggregate data per user
# 
# [Now, as the data is clean, aggregate data per user per period in order to have just one record per user per period. It should ease the further analysis a lot.]

# In[27]:


# Calculate the number of calls made by each user per month. Save the result.
call_count = df_calls.groupby(['user_id' , 'month']).agg(call_count=('user_id','count'))
display(call_count.head(10))


# In[28]:


# Calculate the amount of minutes spent by each user per month. Save the result.
minutes_per_user = df_calls.groupby(['user_id' , 'month']).agg(minutes_per_user=('duration','sum'))
display(minutes_per_user.head(10))


# In[29]:


# Calculate the number of messages sent by each user per month. Save the result.
df_messages['month'] = df_messages['message_date'].dt.strftime("%Y-%m")
message_count = df_messages.groupby(['user_id' , 'month']).agg(message_count=('user_id','count'))
display(message_count)


# In[30]:


# Calculate the volume of internet traffic used by each user per month. Save the result.
df_internet['month'] = df_internet['session_date'].dt.strftime("%Y-%m")
internet_volume = df_internet.groupby(['user_id' , 'month']).agg(data=('mb_used','sum'))
internet_volume = np.ceil(internet_volume)
display(internet_volume)


# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Nice work.
# </div>

# [Put the aggregate data together into one DataFrame so that one record in it would represent what an unique user consumed in a given month.]

# In[31]:


# Merge the data for calls, minutes, messages, internet based on user_id and month
df_users_calls =  pd.merge(call_count,minutes_per_user, how='outer',left_on=['user_id','month'],right_on=['user_id','month'])
df_calls_and_minutes = pd.merge(df_users_calls,message_count, how='outer',left_on=['user_id','month'],right_on=['user_id','month'])
calls_minutes_messages = pd.merge(df_calls_and_minutes,internet_volume, how='outer',left_on=['user_id','month'],right_on=['user_id','month'])
users_merged = pd.merge(df_users,calls_minutes_messages, how='outer',left_on=['user_id','month'],right_on=['user_id','month'])
users_merged[['message_count','call_count','minutes_per_user']] = users_merged[['message_count','call_count','minutes_per_user']].fillna(0) 
users_merged = users_merged.sort_values(by=['user_id','month'])
users_merged = users_merged.ffill()


# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>OK, no worries, but there's just a small mix-up here.
#     
# Please fix an error and rerun whole project to check your findings.
# 
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Let's take a look at how to improve your code.
#     
# Not all users have messages, calls and internet, right? Our recommendation is to change join strategy (to take all information) and check final df shape and number of users.
# 
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>1. Our recommendation here is to use outer join for every join to keep all information.
#     
# 2. Are your sure that ffill is suitable here?
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Perfect!
# </div>

# In[32]:


display(users_merged[users_merged['plan']=='ultimate']['message_count'].mean())


# In[33]:


# Add the plan information
display(df_plans)
display(df_plans.info())


# [Calculate the monthly revenue from each user (subtract the free package limit from the total number of calls, text messages, and data; multiply the result by the calling plan value; add the monthly charge depending on the calling plan). N.B. This might not be as trivial as just a couple of lines given the plan conditions! So, it's okay to spend some time on it.]

# In[34]:


# Calculate the monthly revenue for each user
def call_revenue(row):
    if(row['plan']=='ultimate'):
        row['minutes_per_user'] -= df_plans[df_plans['plan_name']=='ultimate']['minutes_included']
        minutes = row['minutes_per_user']
        minutes = float(minutes)
        if(minutes > 0):
            return 0.01*minutes
        else:
            return 0
    elif(row['plan']=='surf'):
        row['minutes_per_user'] -= df_plans[df_plans['plan_name']=='surf']['minutes_included']
        minutes = row['minutes_per_user']
        minutes = float(minutes)
        if(minutes > 0):
            return 0.03*minutes
        else:
            return 0
    else:
        return 0
    
def message_revenue(row):
    if(row['plan']=='ultimate'):
        row['message_count'] -= df_plans[df_plans['plan_name']=='ultimate']['messages_included']
        messages = row['message_count']
        messages = int(messages)
        if(messages > 0):    
            return 0.01*messages
        return 0
    elif(row['plan']=='surf'):
        row['message_count'] -= df_plans[df_plans['plan_name']=='surf']['messages_included']
        messages = row['message_count']
        messages = int(messages)
        if(messages > 0):
            return 0.03*(messages)
        return 0
    else:
        return 0

def data_revenue(row):
    if(row['plan']=='ultimate'):
        row['data'] -= df_plans[df_plans['plan_name']=='ultimate']['mb_per_month_included']
        data = row['data']
        data = float(data)
        data = (np.ceil(data/1000))
        if(data > 0):
            return round(7*np.ceil((data/1000)),2)
        else:
            return 0
    elif(row['plan']=='surf'):
        row['data'] -= df_plans[df_plans['plan_name']=='surf']['mb_per_month_included']
        data = row['data']
        data = float(data)
        data = (np.ceil(data/1000))
        if(data > 0):
            return round(10*np.ceil(data),2)
        else:
            return 0
    else:
        return 0

def plan_revenue(plan):
    if(plan['plan'] == 'surf'):
        return int(df_plans[df_plans['plan_name']=='surf']['usd_monthly_pay'])
    elif(plan['plan'] == 'ultimate'):
        return int(df_plans[df_plans['plan_name']=='ultimate']['usd_monthly_pay'])
    else:
        return 0


# <div class="alert alert-block alert-warning">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Great function! But it's not a good practice to hardcode values, better to use links to df with information.
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Excellent!
# </div>

# In[35]:


user_excess = pd.DataFrame(data=users_merged,columns=users_merged.columns)
user_excess['plan_revenue'] = np.nan
user_excess['data_revenue'] = np.nan
user_excess['call_revenue'] = np.nan
user_excess['message_revenue'] = np.nan


# In[36]:


user_excess['plan_revenue'] = users_merged.apply(plan_revenue,axis=1)
user_excess['data_revenue'] = users_merged.apply(data_revenue,axis=1)
user_excess['call_revenue'] = users_merged.apply(call_revenue,axis=1)
user_excess['message_revenue'] = users_merged.apply(message_revenue,axis=1)
user_excess['total_revenue'] = user_excess['plan_revenue'] + user_excess['data_revenue'] + user_excess['call_revenue'] + user_excess['message_revenue']


# In[37]:


display(user_excess)


# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Why we apply ffill here? Do we have NaNs?
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Well done.
# </div>

# ## Study user behaviour

# [Calculate some useful descriptive statistics for the aggregated and merged data, which typically reveal an overall picture captured by the data. Draw useful plots to help the understanding. Given that the main task is to compare the plans and decide on which one is more profitable, the statistics and the plots should be calculated on a per-plan basis.]
# 
# [There are relevant hints in the comments for Calls but they are not provided for Messages and Internet though the principle of statistical study is the same for them as for Calls.]

# ### Calls

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Let's take a look at how to improve your code.
#     
# Seems we do not need to make another df. We already join all data in one df.
# </div>

# # Compare average duration of calls per each plan per each distinct month. Plot a bar plot to visualize it.
# df_user_calls = pd.merge(df_calls,df_users,how='outer',on='user_id')
# plan_surf_call = df_user_calls[df_user_calls['plan']=='surf'].groupby('month_x')['duration'].mean()
# plan_ultimate_call = df_user_calls[df_user_calls['plan']=='ultimate'].groupby('month_x')['duration'].mean()

# In[38]:


users_merged[users_merged['plan']=='surf'].groupby('month')['minutes_per_user'].mean().plot(kind='bar',x='month_x',xlabel='Month',ylabel='Duration(minutes)',title='Call Duration Surf',alpha=0.5,color='red')
users_merged[users_merged['plan']=='ultimate'].groupby('month')['minutes_per_user'].mean().plot(kind='bar',x='month_x',xlabel='Month',ylabel='Duration (minutes)',title='Call Duration Ultimate',alpha=0.5)
plt.legend(['Surf','Ultimate'])
plt.show()


# In[39]:


# Compare the number of minutes users of each plan require each month. Plot a histogram.
users_merged[users_merged['plan']=='surf'].groupby('month')['minutes_per_user'].sum().plot(kind='bar',x='month_x',xlabel='Month',ylabel='Duration (minutes)',title='Minutes Needed',alpha=0.5,color='red')
users_merged[users_merged['plan']=='ultimate'].groupby('month')['minutes_per_user'].sum().plot(kind='bar',x='month_x',xlabel='Month',ylabel='Duration (minutes)',title='Minutes Needed',alpha=0.5)
plt.legend(['Surf','Ultimate'])
plt.show()


# [Calculate the mean and the variable of the call duration to reason on whether users on the different plans have different behaviours for their calls.]

# # Calculate the mean and the variance of the monthly call duration
# '''
# surf_mean = df_user_calls[df_user_calls['plan']=='surf'].groupby('month_x')['duration'].mean()
# ultimate_mean = df_user_calls[df_user_calls['plan']=='ultimate'].groupby('month_x')['duration'].mean()
# surf_var = df_user_calls[df_user_calls['plan']=='surf'].groupby('month_x')['duration'].var()
# ultimate_var = df_user_calls[df_user_calls['plan']=='ultimate'].groupby('month_x')['duration'].var()
# display(surf_mean)
# display(surf_var)
# display(ultimate_mean)
# display(ultimate_var)
# '''

# In[40]:


display(round(users_merged[users_merged['plan']=='surf'].groupby('month')['minutes_per_user'].mean(),2))
display(round(users_merged[users_merged['plan']=='surf'].groupby('month')['minutes_per_user'].var(),2))
display(round(users_merged[users_merged['plan']=='ultimate'].groupby('month')['minutes_per_user'].mean(),2))
display(round(users_merged[users_merged['plan']=='ultimate'].groupby('month')['minutes_per_user'].var(),2))


# In[41]:


# Plot a boxplot to visualize the distribution of the monthly call duration
data = [users_merged[users_merged['plan']=='surf'].groupby('month')['minutes_per_user'].mean(),users_merged[users_merged['plan']=='ultimate'].groupby('month')['minutes_per_user'].mean()]
plt.boxplot(data,vert=False)
plt.show()


# People on the Surf plan typically spend longer on the phone. Almost 100% of surf call durations is larger than the longest 50% of calls of users with the ultimate plan with the exception of an outlier between 6.7 and 6.8. People with surf plans spend more time on calls than users of the ultimate plan.

# [Formulate conclusions on how the users behave in terms of calling. Is their behaviour different between the plans?]

#  

# ### Messages

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Let's take a look at how to improve your code.
#     
# Seems we do not need to make another df. We already join all data in one df.
# </div>

# In[42]:


# Compare the number of messages users of each plan tend to send each month
#df_user_messages = pd.merge(df_messages,df_users,how='outer',on='user_id')
#plan_surf_message = df_user_messages[df_user_messages['plan']=='surf'].groupby(['user_id','month_x']).count()
#plan_surf_message = plan_surf_message.groupby('month_x')['id'].mean()
#display(plan_surf_message)
display(users_merged[users_merged['plan']=='surf'].groupby('month')['message_count'].mean())
display(users_merged[users_merged['plan']=='ultimate'].groupby('month')['message_count'].mean())


# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Seems not all changes applied here...
# </div>

# In[43]:


plt.boxplot([users_merged[users_merged['plan']=='surf'].groupby('month')['message_count'].mean(),users_merged[users_merged['plan']=='ultimate'].groupby('month')['message_count'].mean()],vert=False)
plt.show()


# In[44]:


#plan_surf_message.plot(kind='bar',x='month_x',xlabel='Month',ylabel='Messages',title='Messages Used',alpha=0.5,color='red')
#plan_ultimate_message.plot(kind='bar',x='month_x',xlabel='Month',ylabel='Messages',title='Messages Used',alpha=0.5)
users_merged[users_merged['plan']=='surf'].groupby('month')['message_count'].mean().plot(kind='bar',x='month',xlabel='Month',ylabel='Messages',title='Messages Used',alpha=0.5,color='red')
users_merged[users_merged['plan']=='ultimate'].groupby('month')['message_count'].mean().plot(kind='bar',x='month',xlabel='Month',ylabel='Messages',title='Messages Used',alpha=0.5,color='blue')
plt.legend(['Surf','Ultimate'])
plt.show()


# People with the Ultimate Plan tend to send more messages per month on average. Customers on the Surf plan vary their number of messages more per month as seen in the box plot. Users from the Surf plan had a significantly larger IQR than the Ultimate plan.

# [Formulate conclusions on how the users behave in terms of messaging. Is their behaviour different between the plans?]

#  

# ### Internet

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Let's take a look at how to improve your code.
#     
# Seems we do not need to make another df. We already join all data in one df.
# </div>

# In[45]:


# Compare the amount of internet traffic consumed by users per plan
#df_user_data = pd.merge(df_internet,df_users,how='outer',on='user_id')
#plan_surf_data = df_user_data[df_user_data['plan']=='surf'].groupby(['user_id','month_x']).count()
#users_merged[users_merged['plan']=='surf'].groupby('month')['data'].mean()
#plan_surf_data = plan_surf_data.groupby('month_x')['id'].mean()
display(users_merged[users_merged['plan']=='surf'].groupby('month')['data'].mean())


# In[46]:


#plan_ultimate_data = df_user_messages[df_user_messages['plan']=='ultimate'].groupby(['user_id','month_x']).count()
#plan_ultimate_data = plan_ultimate_data.groupby('month_x')['id'].mean()
#display(plan_ultimate_data)
display(users_merged[users_merged['plan']=='ultimate'].groupby('month')['data'].mean())


# In[47]:


plt.boxplot([users_merged[users_merged['plan']=='surf'].groupby('month')['data'].mean(),users_merged[users_merged['plan']=='ultimate'].groupby('month')['data'].mean()],vert=False)
plt.show()


# [Formulate conclusions on how the users tend to consume the internet traffic? Is their behaviour different between the plans?]

# In[48]:


users_merged[users_merged['plan']=='surf'].groupby('month')['data'].mean().plot(kind='bar',x='month_x',xlabel='Month',ylabel='Data(MB)',title='Data Used',alpha=0.5,color='red')
users_merged[users_merged['plan']=='ultimate'].groupby('month')['data'].mean().plot(kind='bar',x='month_x',xlabel='Month',ylabel='Data(MB)',title='Data Used',alpha=0.5)
plt.legend(['Surf','Ultimate'])
plt.ylim(0,22000)
plt.show()


# People with the Ultimate plan tend to use a little more data every month as seen in the bar chart. 

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Nice vizualisations and good conclusions.
# </div>

#  

# ## Revenue

# [Likewise you have studied the user behaviour, statistically describe the revenue between the plans.]

# In[49]:


#plan_surf_revenue = (user_excess[user_excess['plan']=='surf'].groupby('month')['total_revenue'].mean())
#plan_ultimate_revenue = (user_excess[user_excess['plan']=='ultimate'].groupby('month')['total_revenue'].mean())
#display(plan_surf_revenue)
#display(plan_ultimate_revenue)
display(user_excess[user_excess['plan']=='surf'].groupby('month')['total_revenue'].mean())
display(user_excess[user_excess['plan']=='ultimate'].groupby('month')['total_revenue'].mean())


# In[50]:


plt.boxplot([user_excess[user_excess['plan']=='surf'].groupby('month')['total_revenue'].mean(),user_excess[user_excess['plan']=='ultimate'].groupby('month')['total_revenue'].mean()],vert=False)
plt.show()


# In[51]:


user_excess[user_excess['plan']=='surf'].groupby('month')['total_revenue'].mean().plot(kind='bar',x='month_x',xlabel='Month',ylabel='Revenue',title='Revenue Made Surf',alpha=0.5,color='red')
user_excess[user_excess['plan']=='ultimate'].groupby('month')['total_revenue'].mean().plot(kind='bar',x='month_x',xlabel='Month',ylabel='Revenue',title='Revenue Made Ultimate',alpha=0.5)
plt.legend(['Surf','Ultimate'])
plt.ylim(0,90)
plt.show()


# <div class="alert alert-block alert-info">
# <b>Conclusion:</b> <a class="tocSkip"></a>
#     People on the Ultimate plan typically bring in more revenue than people on the Surf plan.
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Well done!
# </div>

# 

# [Formulate conclusions about how the revenue differs between the plans.]

# <div class="alert alert-block alert-warning">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Can we formulate some conclusion here?
# </div>

#  

# ## Test statistical hypotheses

# [Test the hypothesis that the average revenue from users of the Ultimate and Surf calling plans differs.]

# [Formulate the null and the alternative hypotheses, choose the statistical test, decide on the alpha value.]
The mean revenue per month does not change regardless of plan.
The mean revenue per month can change regardless of plan.
# In[52]:


# Test the hypotheses

alpha = 0.05
results = st.ttest_ind(user_excess[user_excess['plan']=='surf'].groupby('month')['total_revenue'].mean() , user_excess[user_excess['plan']=='ultimate'].groupby('month')['total_revenue'].mean() , equal_var=True)
display('p-value:', results.pvalue)

if (results.pvalue < alpha):
    display("We reject the null hypothesis: revenue was significantly lower than the average")
else:
    display("We can't reject the null hypothesis: revenue wasn't significantly lower")


# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Why we divide pvalue by 2 here?
# 
# </div>

# <div class="alert alert-block alert-info">
# <b>Student reply.</b> <a class="tocSkip"></a>
#     I did this initially because I was seeing this as a one sided hypothesis because I wanted to measure the revenue being 70 or more.
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Our recommendation is to use ttest_ind here too.
#     
# Also, we make conclusion based only on pvalue.
# </div>

# [Test the hypothesis that the average revenue from users in the NY-NJ area is different from that of the users from the other regions.]

# [Formulate the null and the alternative hypotheses, choose the statistical test, decide on the alpha value.]

# 

# The mean monthly revenue doesn't change regardless of the city.
# The mean monthly revenue does change in some cities.

# In[53]:


# Test the hypotheses

cities = user_excess['city'].unique()
nynj_revenue = (user_excess[user_excess['city'].isin(['New York-Newark-Jersey City, NY-NJ-PA MSA',
                                                      'Philadelphia-Camden-Wilmington, PA-NJ-DE-MD MSA',
                                                      'Rochester, NY MSA',
                                                      'Albany-Schenectady-Troy, NY MSA',
                                                      'Buffalo-Cheektowaga, NY MSA'])]).groupby('month')['total_revenue'].mean()
interested_value = round(user_excess['total_revenue'].mean(),2)
alpha = 0.05
results = st.ttest_ind(nynj_revenue , user_excess['total_revenue'], equal_var=True)
display(interested_value)
display('p-value:', results.pvalue)

if (results.pvalue < alpha) and (nynj_revenue.mean() < interested_value):
    display("We reject the null hypothesis: revenue was significantly lower than average")
else:
    display("We can't reject the null hypothesis: revenue wasn't significantly lower")


# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Seems we missed second test =)
# 
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Something needs to be changed, but don't worry, you've got this.
#     
# 1. Based on project requirements, we need to test 2 hypotheses: "The average revenue from users of Ultimate and Surf calling plans differs." and "The average revenue from users in NY-NJ area is different from that of the users from other regions.". We do not need to apply test for 70 dollars or something else.
#     
# <s>2. Our recommendation here is to use ttest_ind test.
# 
# </div>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# We make conclusion based only on pvalue.
# </div>

# In[54]:


# reviewer's example

if (results.pvalue < alpha):
    display("We reject the null hypothesis: revenue was significantly lower than average")
else:
    display("We can't reject the null hypothesis: revenue wasn't significantly lower")


# In[ ]:





# ## General conclusion
# 
# [List your important conclusions in this final section, make sure they cover all those important decisions (assumptions) that you've made and that led you to the way you processed and analyzed the data.]

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Please add final conclusion.
# 
# </div>

# <div class="alert alert-block alert-warning">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Michael, please do not forget to rerun whole project before sending!
# 
# </div>

# <div class="alert alert-block alert-info">
# <b>Conclusion.</b> <a class="tocSkip"></a>
#     Overall, more customers buy the surf plan and would rather pay a little more by going over their allowances. There is a significant loss of potential revenue by more people using Surf. Customers on the Ultimate plan give about 70 dollars of revenue while Surf members only bring in between 35-55 dollars per month. The average revenue brought in does not change by the geographic location of customers though. Customers on the Ultimate plan use a lot more data and send a few more messages on average monthly.
# </div>
# 

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Well done!
# 
# </div>

# In[ ]:





# <div class="alert alert-block alert-warning">
# <b>Overall reviewer's comment</b> <a class="tocSkip"></a>
# 
# Michael, thank you for correcting your project!
#     
# However, there are still some issues. I wrote comments. Please elaborate them.
#     
# <span class="text-danger"> Remember: in case of any problems, you can contact your tutor. </span>
#     
# You have good analytic skills, keep up the good work! I will be waiting for your corrected project.
# </div>

# <div class="alert alert-block alert-warning">
# <b>Overall reviewer's comment v2</b> <a class="tocSkip"></a>
# 
# Thanks for sending in your project with corrections. It's clear you've put a lot of effort into it.
#     
# There's still an issue with Test statistical hypotheses. Could you take a second glance at it? 
#     
# <span class="text-danger"> Please do not forget to rerun project before sending! </span>
#     
# Keep working on it, you are improving!
# </div>

# <div class="alert alert-block alert-success">
# <b>Overall reviewer's comment v3</b> <a class="tocSkip"></a>
# 
# Much better!
#     
# Your project has been accepted and you can go to the next sprint.
# </div>

# In[ ]:





#  
