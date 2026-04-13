import streamlit as st
import google.generativeai as genai
from PIL import Image # We need this to read the uploaded image

# Page Config
st.set_page_config(page_title="EPIC Insight-to-Action", page_icon="🚀", layout="wide")
st.title("🚀 EPIC Insight-to-Action Engine")
st.markdown("Turn dense institutional text AND visual data into high-growth performance marketing assets.")

# User Inputs
api_key = st.text_input("Enter your Gemini API Key:", type="password")
user_input = st.text_area("Paste EPIC Lab Research or Context Here:", height=150)

# NEW: Add an image uploader
uploaded_file = st.file_uploader("Optional: Upload an EPIC Lab chart, flyer, or infographic...", type=["jpg", "jpeg", "png"])

if st.button("Generate Growth Assets"):
    if not api_key or not user_input:
        st.warning("Please enter your API Key and text context.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.5-flash') 
            
            prompt = f"""
            You are the Lead Growth Architect for EPIC Lab.
            Using the provided text and/or image, generate in english regardless of the lenguage of the info provided:
            1. A TikTok Script (focus on loss aversion/FOMO for the hook, you can use several types of tiktok to engage audience, telling a story, 
            acting, if you make a sketch for example,  you can use a humor that appelas to entrepeneurs, people into business, etc. use characters like a finance, crypto bro only two characters at moat
            people who want to get outside the matrix, 9-5 rejection, buy be sure that the final message is that the epic lab is the institutional right way and professional way to do it, this sketch thing 
            only if it fits, you can use other type of videos, do not limit yourself and be creative)
            2. 3 Google Ads/meta ads variations (Character optimized for CTR, you should implemment behavioral economics biases, loss aversion, anchoring etc...
            for the output please create  1. key words for the add. 2. titles 3. descriptions 4. sugggested images)
            3. A Landing Page Wireframe (Hero, Social Proof, 3 Pillars)
            
            Text Context:
            {user_input}
            """
            
            with st.spinner("Analyzing data and generating assets..."):
                # If they uploaded an image, send BOTH the prompt and the image
                if uploaded_file is not None:
                    img = Image.open(uploaded_file)
                    response = model.generate_content([prompt, img])
                # If no image, just send the text prompt
                else:
                    response = model.generate_content(prompt)
                    
                st.success("Assets Generated Successfully!")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"An error occurred: {e}")
            
