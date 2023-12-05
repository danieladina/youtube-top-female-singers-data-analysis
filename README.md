YouTube Channel and Video Analysis


This Python script uses the YouTube Data API to gather statistics and details from specified channels and their videos. The script includes functionalities to:

Retrieve channel statistics such as subscribers, total views, and video count.


Analyze top videos based on views, likes, comments, and published dates.


Visualize the data using Matplotlib and Seaborn.


Requirements


Python 3.x
Google API key with access to the YouTube Data API v3


Installation


Clone this repository.



Install the required dependencies:
bash

pip install google-api-python-client pandas matplotlib seaborn


Setup


Obtain a Google API key with access to the YouTube Data API v3 here.


Replace 'YOUR_API_KEY' in the script with your API key.

Usage

Update the channel_ids list with the desired YouTube channel IDs.
Run the script to fetch channel statistics and video details.
View generated visualizations and top videos.
bash
Copy code
python youtube_analysis.py
Functionality Overview
1. Retrieving Channel Statistics
The script fetches statistics including subscribers, views, and total videos for specified channels.

2. Analyzing Top Videos
It retrieves video details such as views, likes, comments, and published dates. The script then identifies the top 10 videos based on views.

3. Visualizations
The script creates visualizations:

Bar plots displaying total videos and views for each channel.
Monthly distribution of videos released by a specific artist.
Outputs
A DataFrame displaying channel statistics and video details.
Visualizations showing comparative analysis and trends.
CSV file with detailed video information.
Credits
This script utilizes the google-api-python-client, pandas, matplotlib, and seaborn libraries.

Contributing
Feel free to contribute by forking this repository, making changes, and creating a pull request.
