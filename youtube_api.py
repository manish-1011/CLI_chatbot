import googleapiclient.discovery
import os

api_key = "YOUR_YOUTUBE_API_KEY"
api_service_name = "youtube"
api_version = "v3"

def search_videos(query, max_results=5):
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)
    request = youtube.search().list(
        part="snippet",
        maxResults=max_results,
        q=query
    )
    response = request.execute()
    return response.get("items", [])

def get_video_url(video_id):
    return f"https://www.youtube.com/watch?v={video_id}"
