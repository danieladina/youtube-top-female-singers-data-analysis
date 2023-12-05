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



Obtaining a Google API Key


Go to the Google Developers Console:

Visit the Google Developers Console.
Create a New Project:

Click on "Select a project" at the top left and then click on "New Project".


Enter a name for your project and click "Create".


Enable the YouTube Data API v3:

In the dashboard, click on "Enable APIs and Services".


Search for "YouTube Data API v3" and click on it.


Click the "Enable" button.


Create Credentials:

Go to the "Credentials" section from the left sidebar.


Click "Create Credentials" and select "API key".


A dialog box will appear showing your API key. Copy it.


Running the Script

Clone the Repository:

If you haven't already, clone the repository containing the script:

bash

git clone https://github.com/your_username/repository_name.git


cd repository_name


Open the Python Script:

Open the Python script named youtube_analysis.py or any relevant filename that contains the provided code in your preferred text editor or IDE.


Replace the API Key:

Locate the variable api_key = 'YOUR_API_KEY' within the script

.
Replace 'YOUR_API_KEY' with the API key you obtained from the Google Developers Console.


Specify Channel IDs (Optional):

If needed, update the channel_ids list with the desired YouTube channel IDs.


Execute the Script:

Open a terminal or command prompt.


Navigate to the directory where the script is located:

bash

cd /path/to/script_directory


Run the script using Python:


bash

python youtube_analysis.py

Interpreting the Results:

The script will fetch channel statistics, analyze top videos, and generate visualizations.

Depending on the script, it may display plots, print information, or generate CSV files as specified in the script.

Remember to replace /path/to/script_directory with the actual path where your script is located and ensure you have Python installed on your machine along with the necessary libraries mentioned in the README file.






