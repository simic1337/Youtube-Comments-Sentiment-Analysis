import os
import googleapiclient.discovery
from csv import writer
from dotenv import load_dotenv

load_dotenv()

# Main part of the code is taken from Youtube Data API website. It's available on the link: https://developers.google.com/youtube/v3/docs/commentThreads
# In order to make a request, developer API key needs to be provided, and the same can be obtain on Google Developers website
# For security reasons it's highly recommended NOT to share your API key, therefore I won't share mine

def scrapeCommentsOnVideo(videoID, saveToFile, nextPageToken):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.environ.get('DEVELOPER_KEY')
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)
    
    request = youtube.commentThreads().list(
        order="time",
        part="snippet",
        videoId=videoID,
        maxResults=500,
        pageToken=nextPageToken,
        textFormat='plainText'
    )

    response = request.execute()
    nextPageToken = response.get('nextPageToken')

    with open(saveToFile, 'a', newline='', encoding="utf-8") as file:
        fileWriter = writer(file)
        for index in range(len(response.get('items'))):
            fileWriter.writerow([response.get('items')[index].get('snippet').get(
                'topLevelComment').get('snippet').get('textDisplay')])
        file.close()

    if(nextPageToken):
        scrapeCommentsOnVideo(videoID, saveToFile, nextPageToken)