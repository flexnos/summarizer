import streamlit as st
import streamlit_extras.switch_page_button as switch

# Page Configuration
st.set_page_config(page_title="YouTube AI Assistant", page_icon="📽️", layout="wide")

# Custom CSS for Styling
st.markdown(
    """
    <style>
    /* Title Styling */
    .title-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        margin-bottom: 20px;
    }
    .title-logo {
        width: 50px;
        height: 50px;
    }
    .title-text {
        font-size: 50px;
        font-weight: bold;
    }

    /* General Styles */
    h1 { font-size: 50px !important; text-align: center; font-weight: bold; }
    h2 { font-size: 30px !important; text-align: center; color: #ddd; }
    h3 { font-size: 24px !important; text-align: center; color: #bbb; }
    p { font-size: 18px !important; text-align: justify; color: #aaa; line-height: 1.6; }

    /* Glowing Thin Line Divider */
    .divider {
        height: 2px;
        background: linear-gradient(to right, #ff4b4b, #ff9800, #ff4b4b);
        box-shadow: 0px 0px 5px rgba(255, 75, 75, 0.5);
        margin: 40px 0;
        border-radius: 2px;
    }

    /* Feature Box Styling */
    .feature-box {
        transition: all 0.3s ease-in-out;
        transform: scale(1);
        padding: 20px;
        border-radius: 8px;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        box-shadow: 0 0 8px rgba(255, 255, 255, 0.2);
    }
    .feature-box:hover {
        transform: scale(1.05);
        box-shadow: 0 0 12px rgba(255, 255, 255, 0.3);
    }

    /* Footer */
    .footer {
        text-align: center;
        font-size: 16px;
        color: #777;
        margin-top: 50px;
        padding: 20px;
        border-top: 1px solid #333;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Section with Logo
st.markdown(
    """
    <div class="title-container">
        <img class="title-logo" src="https://cdn-icons-png.flaticon.com/512/1384/1384060.png">
        <span class="title-text">YouTube AI Assistant</span>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation (Fixed)
st.sidebar.title("Navigation")
st.sidebar.markdown("[Summarize Video](pages/summarize.py)")
st.sidebar.markdown("[AI-Powered Q&A](pages/QnA.py)")

# Main Content
#st.markdown('<h1>YouTube AI Assistant</h1>', unsafe_allow_html=True)
st.markdown('<h2>AI-Powered Tool for Summarizing & Understanding Video Content</h2>', unsafe_allow_html=True)


# Display the animated GIF
gif_path = r"C:\Users\win10\Desktop\Sum\summarize_with_ease.gif"  # Make sure the file exists in the project folder
st.image(gif_path, use_container_width=True)

st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🏠 Home Page")
st.write("Welcome to the Home Page! Sidebar is now hidden.")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🔍 Go to Summarize"):
        switch.switch_page("summarize")  # Make sure your summary page is named "summary.py"

with col2:
    if st.button("💬 Go to QnA"):
        switch.switch_page("qna")  # Make sure your QnA page is named "qna.py"






# Main Image
#st.image("https://cdn.pixabay.com/photo/2023/03/22/14/18/ai-7868471_1280.jpg", use_container_width=True)

# Divider
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Introduction Section
st.markdown("<h3>About the Tool</h3>", unsafe_allow_html=True)
st.write(
    "YouTube AI Assistant is designed to help users quickly extract key insights from YouTube videos "
    "without watching the entire content. Using advanced AI techniques, this tool can summarize videos, "
    "generate transcripts, and even answer questions based on video content. Whether you're a student, "
    "researcher, or content creator, this tool enhances productivity and saves time."
)

# Divider
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Features Section
st.markdown("<h3>Key Features</h3>", unsafe_allow_html=True)

# Add spacing before feature boxes
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.image(r"C:\Users\win10\Downloads\artificial-intelligence.png", width=90)
    st.markdown("<p><strong>Summarize Videos</strong><br>Generate meaningful summaries.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/1256/1256650.png", width=90)
    st.markdown("<p><strong>AI-Powered Q&A</strong><br>Ask questions, get AI-generated answers.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/841/841364.png", width=90)
    st.markdown("<p><strong>High Accuracy</strong><br>Utilizes state-of-the-art AI models.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Add more space after features
st.markdown("<br><br>", unsafe_allow_html=True)

# Divider
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# How It Works Section
st.markdown("<h3>How It Works</h3>", unsafe_allow_html=True)

st.write(
    "1. Select a feature from the sidebar—Summarize Video or AI-Powered Q&A.\n"
    "2. Enter a YouTube video link to process the content.\n"
    "3. Get a concise summary or ask AI-generated questions.\n"
    "4. Improve your productivity by quickly understanding key insights."
)

# Divider
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Footer (Fixed Alignment)
st.markdown('<div class="footer">Developed by <strong>IA²S</strong></div>', unsafe_allow_html=True)
