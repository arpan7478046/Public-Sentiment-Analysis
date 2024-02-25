#CODE TO EXTRACT COMMENT OF ANY VIDEO FROM YOUTUBE USING API



# -*- coding: utf-8 -*-
# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "YOUR_API_KEY"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        maxResults=NUMBER_OF_COMMENTS_YOU_NEED,
        videoId="VIDEO_ID"
    )
    response = request.execute()

    i = 0
    data2 = []
    for i in range(len(response['items'])):
        data = response['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay']
        data2 += [data]
        
    
    print(data2)

if __name__ == "__main__":
    main()