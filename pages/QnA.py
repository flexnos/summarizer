import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import pyttsx3
from deep_translator import GoogleTranslator

# Load API keys
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("🚨 GOOGLE_API_KEY is missing!")

# Function to extract video ID
def extract_video_id(youtube_url):
    parsed_url = urlparse(youtube_url)
    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed_url.query).get("v", [None])[0]
    elif parsed_url.hostname in ["youtu.be"]:
        return parsed_url.path[1:]
    return None

# Function to fetch transcript with Hindi fallback
def extract_transcript(youtube_url):
    video_id = extract_video_id(youtube_url)
    if not video_id:
        return "Invalid YouTube link."
    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id, languages=['hi'])
        return " ".join([i["text"] for i in transcript_data])
    except:
        try:
            transcript_data = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            return " ".join([i["text"] for i in transcript_data])
        except Exception as e:
            return f"Error: {e} (No subtitles available.)"

# Function to generate AI response
def ask_ai(transcript_text, question):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        prompt = f"You are an AI. Use the transcript below to answer the user's question.\nTranscript:\n{transcript_text}\n\nQ: {question}\nA:"
        response = model.generate_content(prompt)
        return response.text if response.text else "No response."
    except Exception as e:
        return f"Error: {e}"

# Function to generate AI summary
def generate_summary(transcript_text):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        prompt = "Summarize the transcript into key points within 400 words."
        response = model.generate_content(prompt + transcript_text)
        return response.text if response.text else "No response."
    except Exception as e:
        return f"Error: {e}"

# Function to translate summary to Hinglish
def translate_to_hinglish(text):
    return GoogleTranslator(source='en', target='hi').translate(text)

# Function to read summary aloud
def speak_summary(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# UI Layout
st.title("🤖 Ask AI About the Video")
youtube_link = st.text_input("🔗 Enter YouTube Video Link:")
user_question = st.text_input("❓ Ask a question:")

if youtube_link:
    video_id = extract_video_id(youtube_link)
    if video_id:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)
    else:
        st.error("Invalid YouTube link.")

if st.button("Get Answer"):
    with st.spinner("⏳ Thinking..."):
        transcript_text = extract_transcript(youtube_link)
        if "Error" in transcript_text:
            st.error(transcript_text)
        else:
            answer = ask_ai(transcript_text, user_question)
            st.markdown("### 🎯 Answer")
            st.markdown(f'<div class="summary-box">{answer}</div>', unsafe_allow_html=True)

if st.button("Generate Summary"):
    with st.spinner("⏳ Generating Summary..."):
        transcript_text = extract_transcript(youtube_link)
        if "Error" in transcript_text:
            st.error(transcript_text)
        else:
            summary = generate_summary(transcript_text)
            st.markdown("### 📝 Summary")
            st.markdown(f'<div class="summary-box">{summary}</div>', unsafe_allow_html=True)
            if st.button("Read Summary"):
                speak_summary(summary)
            if st.button("Translate to Hinglish"):
                hinglish_summary = translate_to_hinglish(summary)
                st.markdown("### 🇮🇳 Hinglish Summary")
                st.markdown(f'<div class="summary-box">{hinglish_summary}</div>', unsafe_allow_html=True)
