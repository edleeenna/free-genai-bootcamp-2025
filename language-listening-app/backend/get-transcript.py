from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_transcript(video_id):
    """Fetches the transcript of a YouTube video if available."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ja'])
        return " ".join([entry['text'] for entry in transcript])
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

# Example Usage
video_id = "hVOvyR3fSrU"
transcript = get_youtube_transcript(video_id)
print(transcript if transcript else "No transcript available.")
