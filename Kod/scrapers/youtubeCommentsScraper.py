import os
import googleapiclient.discovery
from csv import writer
from dotenv import load_dotenv

load_dotenv()

# main part of the code is taken from Youtube Data API website. It's available on the link: https://developers.google.com/youtube/v3/docs/commentThreads
# In order to make a request, developer key needs to be provided, and the same can be obtain on Google Developers website
# For security reasons it's highly recommended NOT to share your developer key, therefore I won't share mine


def scrapeCommentsOnVideo(videoID, saveToFile, nextPageToken):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.environ.get('DEVELOPER_KEY')
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    # Comments are ordered by time, which means that latest comments will be
    # Text format is set to plainText, beacuse it's way easier to obtain wanted data
    # The snippet object contains basic details about the comment thread
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
    # append to file, newline is neccessary in order to avoid adding comma after every letter
    # encoding is added beacuse of the inability to read response from API
    with open(saveToFile, 'a', newline='', encoding="utf-8") as file:
        fileWriter = writer(file)
        for index in range(len(response.get('items'))):
            # response return very complex dictionary object, so to get to comments this is the path
            fileWriter.writerow([response.get('items')[index].get('snippet').get(
                'topLevelComment').get('snippet').get('textDisplay')])
        file.close()
    # recursive call if there is a next page of comments
    if(nextPageToken):
        scrapeCommentsOnVideo(videoID, saveToFile, nextPageToken)
