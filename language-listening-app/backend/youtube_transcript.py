from youtube_transcript_api import YouTubeTranscriptApi


class YouTubeTranscriptFetcher:
    """Fetches transcripts from YouTube videos."""

    def __init__(self, language="ja"):
        """Initialize with a default language for transcripts."""
        self.language = language

    def get_transcript(self, video_id):
        """Fetches the transcript of a YouTube video if available."""
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[self.language])
            return " ".join([entry['text'] for entry in transcript])
        except Exception as e:
            print(f"Error fetching transcript for {video_id}: {e}")
            return None

# Example Usage (if running this file directly)
if __name__ == "__main__":
    fetcher = YouTubeTranscriptFetcher(language="ja")
    video_id = "hVOvyR3fSrU"
    transcript = fetcher.get_transcript(video_id)
    print(transcript if transcript else "No transcript available.")
