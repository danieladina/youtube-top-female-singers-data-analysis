from googleapiclient.discovery import build
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


api_key = 'Enter your api key here'
channel_id = 'UCKEImtWikw9usC1pl_9m1nQ'
channel_ids = ['UC-J-KZfRV8c13fOCkhXdLiQ',#dua lipa
                'UCOCgB3xd-B-1qAm-hR9OLrA',#helsay
                'UCqk3CdGN_j8IR9z4uBbVPSg',#lana
                'UCcgqSM4YEo5vVQpqwN-MaNw',#riana
                'UCN9HPn2fq-NL8M5_kp4RWZQ',#sia
                'UC9CoOnJkIBMdeijd9qYoT_g',#grande
               'UCjNRJBlxvvS0UXAT2Ack-QQ',#zara lar

               ]

youtube = build('youtube','v3',developerKey = api_key)


##function to get channel statistic
def get_channel_stats(youtube,channel_ids):
    all_data=[]
    requests=youtube.channels().list(part='snippet,contentDetails,statistics',id=','.join(channel_ids))
    response = requests.execute()

    for i in range(len(response['items'])):
        data = dict(channel_name = response['items'][i]['snippet']['title'],
                    subscribers=response['items'][i]['statistics']['subscriberCount'],
                    Views=response['items'][i]['statistics']['viewCount'],
                    Total_videos=response['items'][i]['statistics']['videoCount'],
                    playlist_id=response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
        all_data.append(data)
    return (all_data)

channel_statistics = get_channel_stats(youtube,channel_ids)

channel_data=pd.DataFrame(channel_statistics)

print(channel_data)

channel_data['subscribers'] = pd.to_numeric(channel_data['subscribers'])
channel_data['Views'] = pd.to_numeric(channel_data['Views'])
channel_data['Total_videos'] = pd.to_numeric(channel_data['Total_videos'])
#print(channel_data.dtypes)





############################################################################################################


sns.set(rc={'figure.figsize': (10, 5)})  # Adjust figure size

# Creating subplots
fig, (ax1, ax2) = plt.subplots(1, 2)

# Plotting the first bar plot in the first subplot
sns.barplot(x='channel_name', y='Total_videos', data=channel_data, ax=ax1)
ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)  # Rotate x-axis labels for better visibility
ax1.set_title('Total Videos')  # Set title for the first plot

# Plotting the second bar plot in the second subplot
sns.barplot(x='channel_name', y='Views', data=channel_data, ax=ax2)
ax2.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)  # Rotate x-axis labels for better visibility
ax2.set_title('Views')  # Set title for the second plot

plt.tight_layout()  # Adjust layout for better fit

# Adding text at the bottom of the figure
fig.text(0.5, 0.05, 'Although Sia and Dua Lipa has more videos, \nRihanna and Ariana has more views', ha='center', fontsize=15)

plt.show()  # Display the combined figure with both subplots

############################################################################################################




##function to get video ids
playlist_id=channel_data.loc[channel_data['channel_name']=='Zara Larsson','playlist_id'].iloc[0]
#print(playlist_id)



def get_video_id(youtube,playlist_id):
    requests = youtube.playlistItems().list(part='contentDetails',playlistId=playlist_id,maxResults=50)
    response=requests.execute()

    video_ids = []




    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])



    next_page_token =(response.get('nextPageToken'))
    more_pages = True

    while more_pages:
        if next_page_token is None:
            more_pages=False
        else:
            requests=youtube.playlistItems().list(part='contentDetails',
                                                  playlistId=playlist_id,
                                                  maxResults=50,
                                                  pageToken=next_page_token)
            response=requests.execute()
            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])

            next_page_token=response.get('nextPageToken')



    return (video_ids)

video_ids=get_video_id(youtube,playlist_id)





##function to get video details

def get_video_details(youtube,video_ids):
    all_video_stats=[]
    for i in range(0,len(video_ids),50):



        requests = youtube.videos().list(
            part='snippet,statistics',
            id=','.join(video_ids[i:i+50])
        )
        response=requests.execute()

        for video in response['items']:
            video_stats = dict(Title = video['snippet']['title'],
                               Published_date = video['snippet']['publishedAt'],
                               Views =video['statistics']['viewCount'],
                               Likes=video['statistics']['likeCount'],
                               #Dislikes=video['statistics']['dislikeCount'],
                               Comments=video['statistics']['commentCount'],
                               )
            all_video_stats.append(video_stats)
    return (all_video_stats)

video_details = get_video_details(youtube,video_ids)
video_data = pd.DataFrame(video_details)
#print(video_data)


video_data['Published_date']=pd.to_datetime(video_data['Published_date']).dt.date
video_data['Views']=pd.to_numeric(video_data['Views'])
video_data['Likes']=pd.to_numeric(video_data['Likes'])
video_data['Comments']=pd.to_numeric(video_data['Comments'])

top10_videos = video_data.sort_values(by='Views', ascending=False).head(10)
pd.set_option('display.max_rows', None)  # Set to None to display all rows
pd.set_option('display.max_columns', None)  # Set to None to display all columns
print(top10_videos)

ax1 = sns.barplot(x='Views', y='Title', data=top10_videos)
plt.show()

video_data['month']=pd.to_datetime(video_data['Published_date']).dt.strftime('%b')
print(video_data)

video_per_month = video_data.groupby('month',as_index=False).size()

sort_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
video_per_month.index=pd.CategoricalIndex(video_per_month['month'], categories=sort_order,ordered=True)
video_per_month = video_per_month.sort_index()
print(video_per_month )





plt.figure(figsize=(10, 6))  # Adjust the values to your desired figure size

# Create the bar plot
ax = sns.barplot(x='month', y='size', data=video_per_month)

# Rotate x-axis labels for better readability
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)  # Rotate labels by 45 degrees

# Set axes labels and plot title (if needed)
plt.xlabel('Month')
plt.ylabel('Size')
plt.title('Videos per Month by Rihanna')

# Show the plot
plt.tight_layout()  # Adjusts subplot parameters to give specified padding
ax.text(2.5, 50, 'Rihanna loves to release her songs in autumn', ha='center', fontsize=10)
plt.show()

video_data.to_csv('video_Details(Zara Larsson).csv')
