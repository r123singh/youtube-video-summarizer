import re
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI



client = OpenAI(api_key= "sk-proj-")


def create_transcript(videoid): 
    transcript = YouTubeTranscriptApi.get_transcript(videoid)
    data = ""
    for item in transcript:
        data = data +" "+ item['text']
    return data

def get_videoId(youtube_link):
    pattern = r"(?<=v=).+"
    match = re.search(pattern, youtube_link)
    if match:
        print(match.group())
        return match.group()
    else:
        return -1

    
def summary_extraction(transcription):
    response = client.chat.completions.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following text and summarize it into a concise abstract paragraph. Aim to retain the most important points, providing a coherent and readable summary that could help a person understand the main points of the discussion without needing to read the entire text. Please avoid unnecessary details or tangential points."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response.choices[0].message.content



def start():
    youtube_link = input("Enter the youtube video link: ")
    videoid = get_videoId(youtube_link)
    if videoid == -1:
         print("Please enter correct Youtube video link")
         print("*******************************************************")
         start()
    else:
        transcription = create_transcript(videoid)
        if len(transcription) >0:
            print("*******************************************************")
            print("Video Summary")
            print("*******************************************************")
            print(summary_extraction(transcription))
        
start()