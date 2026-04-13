import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="EPIC Insight-to-Action", page_icon="🚀", layout="wide")
st.title("🚀 EPIC Insight-to-Action Engine")
st.markdown("Turn dense institutional text into high-growth, quantifiable performance marketing assets.")

# User Inputs
api_key = st.text_input("Enter your Gemini API Key:", type="password")
user_input = st.text_area("Paste EPIC Lab Research or Text Here:", height=150)

if st.button("Generate Growth Assets"):
    if not api_key or not user_input:
        st.warning("Please enter your API Key and text.")
    else:
        try:
            genai.configure(api_key=api_key)
            # Using Gemini 2.5 Flash for speed
            model = genai.GenerativeModel('gemini-2.5-flash') 
            
            prompt = f"""
            You are the Lead Growth Architect for EPIC Lab.
            Translate the following text into three assets:
            1. A TikTok Script (focus on loss aversion/FOMO for the hook)
            2. 3 Google Ads variations (Character optimized for CTR)
            3. A Landing Page Wireframe (Hero, Social Proof, 3 Pillars)
            
            Text to translate:
            {user_input}
            """
            
            with st.spinner("Generating Assets..."):
                response = model.generate_content(prompt)
                st.success("Assets Generated Successfully!")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"An error occurred: {e}")
            
