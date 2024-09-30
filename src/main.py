import os
import googleapiclient.discovery
import googleapiclient.errors

# Replace with your API key or OAuth credentials
API_KEY = "YOUR_API_KEY"

youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

def get_video_details(video_id):
    request = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        id=video_id
    )
    response = request.execute()

    video_title = response['items'][0]['snippet']['title']
    video_description = response['items'][0]['snippet']['description']
    video_views = response['items'][0]['statistics']['viewCount']
    video_likes = response['items'][0]['statistics']['likeCount']
    video_duration = response['items'][0]['contentDetails']['duration']

    print(f"Title: {video_title}")
    print(f"Description: {video_description}")
    print(f"Views: {video_views}")
    print(f"Likes: {video_likes}")
    print(f"Duration: {video_duration}")

# Replace with the video ID you want to retrieve details for
video_id = "VIDEO_ID_HERE"
get_video_details(video_id)