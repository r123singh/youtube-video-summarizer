# Youtube Video Summarizer

Youtube Video Summarizer creates a concise summary of YouTube videos, allowing users to understand the content without watching the entire video. It is a Python-based application that utilizes the **OpenAI API** and **youtube-transcript-api** to generate summaries. All you need to do is input a YouTube video link, and the program will provide a summary based on the transcript.

## Features

- **Fast and Concise Summaries**: Get the gist of long YouTube videos in seconds.
- **API Integrations**: 
  - **OpenAI API**: Used for generating high-quality summaries.
  - **youtube-transcript-api**: Extracts transcripts directly from YouTube videos.
- **Easy to Use**: Input a video URL, and the summary is generated automatically.

---

## Requirements

- Python 3.7+
- API Key for OpenAI (Sign up at [OpenAI](https://platform.openai.com/))
- Packages:
  - `openai`
  - `youtube-transcript-api`

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/youtube-video-summarizer.git
   cd youtube-video-summarizer

2. **Create a Virtual Environment (Optional but Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Mac/Linux
    venv\Scripts\activate     # On Windows

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt

4. **Set up OpenAI API Key: Create a .env file in the project root with the following content:**
    ```bash
    OPENAI_API_KEY=your_openai_api_key_here

---

## Usage

1. **Run the program**
    ```bash
    python main.py

2. **Input the YouTube Video URL when prompted.**

3. **View the Summary: The program will generate and display a concise summary.**

## Example
1. **Below is an example** 
    ```bash
    Enter the YouTube video link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
    Summary: "This is a music video where the artist surprises viewers with an unexpected twist..."


## Contributing

1. **Fork the project.**

2. **Create a feature branch:**
    ```bash
    git checkout -b feature-branch

3. **Commit your changes:**
    ```bash
    git commit -m "Add some feature"

4. **Push to the branch:**
    ```bash
    git push origin feature-branch

5. **Open a pull request.**

