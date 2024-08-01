from youtube_transcript_api import YouTubeTranscriptApi


def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id,languages=['hi', 'en'])

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
    

'''youtube_video_url = "https://www.youtube.com/watch?v=azpUG2GUzFI&t=31s"
#youtube_video_url ="https://www.youtube.com/watch?v=lbyhSmtou7E"
text=extract_transcript_details(youtube_video_url)
print(text)'''