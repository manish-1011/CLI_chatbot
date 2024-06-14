# YouTube Chatbot

## Description
This CLI-powered chatbot allows users to find YouTube videos, fetch transcripts, and summarize the content using a Transformer model for summarization.

## Setup
1. Clone the repository:
    ```bash
    git clone 
    cd youtube_chatbot
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv youtubebot
    source youtubebot/bin/activate  # On Windows use `youtubebot\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Update the API keys in `youtube_api.py`.

## Usage
Run the main application:
```bash
python main.py <query>
