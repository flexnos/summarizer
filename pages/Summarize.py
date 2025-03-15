import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import pyttsx3

# Load API keys
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("🚨 GOOGLE_API_KEY is missing!")

# Initialize pyttsx3 engine globally
if "tts_engine" not in st.session_state:
    st.session_state.tts_engine = pyttsx3.init()
    st.session_state.is_speaking = False  # Track speaking state

# Function to extract video ID
def extract_video_id(youtube_url):
    parsed_url = urlparse(youtube_url)
    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed_url.query).get("v", [None])[0]
    elif parsed_url.hostname in ["youtu.be"]:
        return parsed_url.path[1:]
    return None

# Function to fetch transcript
def extract_transcript(youtube_url):
    video_id = extract_video_id(youtube_url)
    if not video_id:
        return "Invalid YouTube link."
    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([i["text"] for i in transcript_data])
    except Exception as e:
        return f"Error: {e} (No subtitles available.)"

# Function to generate summary
def generate_summary(transcript_text):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Updated model name
        prompt = "Summarize the transcript into key points within 250 words:\n"
        response = model.generate_content(prompt + transcript_text)
        return response.text if response.text else "No response."
    except Exception as e:
        return f"Error: {e}"

# Function for text-to-speech
def read_summary(summary_text):
    if not st.session_state.is_speaking:
        st.session_state.is_speaking = True
        engine = st.session_state.tts_engine
        engine.setProperty("rate", 150)  # Adjust speech speed
        engine.setProperty("volume", 1.0)  # Set volume
        engine.say(summary_text)
        engine.runAndWait()
        st.session_state.is_speaking = False  # Reset after speaking

# Function to stop speech
def stop_speech():
    if st.session_state.is_speaking:
        st.session_state.tts_engine.stop()  # Stop speech
        st.session_state.is_speaking = False

# Initialize session state for summary
if "summary" not in st.session_state:
    st.session_state.summary = None

# UI Layout
st.title("📜 Summarize YouTube Video")
youtube_link = st.text_input("🔗 Enter YouTube Video Link:")

if youtube_link:
    video_id = extract_video_id(youtube_link)
    if video_id:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    else:
        st.error("Invalid YouTube link.")

if st.button("Get Summary"):
    with st.spinner("⏳ Generating Summary..."):
        transcript_text = extract_transcript(youtube_link)
        if "Error" in transcript_text:
            st.error(transcript_text)
        else:
            st.session_state.summary = generate_summary(transcript_text)  # Store in session state

# Display summary if available
if st.session_state.summary:
    # Styled Summary Box
    st.markdown("""
        <style>
        .summary-box {
            background-color: #f5f5f5;
            padding: 15px;
            border-radius: 8px;
            border-left: 5px solid #4CAF50;
            font-size: 16px;
            color: #333;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("## 📝 Summary")
    st.markdown(f'<div class="summary-box">{st.session_state.summary}</div>', unsafe_allow_html=True)

    # Buttons for reading and stopping the summary
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("🔊 Read Summary"):
            read_summary(st.session_state.summary)  # Read from session state

    with col2:
        if st.button("⏹️ Stop"):
            stop_speech()  # Stop the voice output
