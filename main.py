import sys
from youtube_api import search_videos, get_video_url
from transcript_api import get_transcript
from transformer_summarizer import summarize_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <query>")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    videos = search_videos(query)

    if not videos:
        print("No videos found.")
        return

    transcripts = []
    for video in videos:
        if "videoId" in video["id"]:
            title = video["snippet"]["title"]
            video_id = video["id"]["videoId"]
            video_url = get_video_url(video_id)
            print(f"{title}: {video_url}")

            transcript = get_transcript(video_id)
            if transcript:
                print(f"Transcript fetched for video {video_id}")
                transcripts.append(transcript)
            else:
                print(f"Could not fetch transcript for video {video_id}")

    print("\nTranscripts list:")
    for i, transcript in enumerate(transcripts):
        summary = summarize_text(transcript)
        print(f"\nSummary {i + 1}: {summary}")

if __name__ == "__main__":
    main()
