import streamlit as st
import requests

# Backend API Endpoint (Update this if running on a different host)
BACKEND_URL = "http://localhost:8000"

st.title("Japanese Learning Assistant 🎧📖")

# Search Bar for Transcripts
query = st.text_input("🔍 Search for a transcript (e.g., 'conversation about travel'):")

if st.button("Search"):
    if query.strip():
        response = requests.post(f"{BACKEND_URL}/search", json={"query": query})
        if response.status_code == 200:
            results = response.json()
            if results:
                for i, item in enumerate(results):
                    st.subheader(f"Match {i+1}: {item['video_id']}")
                    st.write(item["excerpt"])
                    
                    # Log to see if this block is being executed
                    st.write(f"Rendering button for video_id: {item['video_id']}")
                    
                    # Using unique key for each button inside the loop
                    button_key = f"generate_q_{i}"
                    if st.button(f"🧠 Generate Questions for {item['video_id']}", key=button_key):
                        st.write(f"Button clicked for video ID: {item['video_id']}")  # Log the button click
                        
                        # Make the request to generate questions
                        q_response = requests.post(f"{BACKEND_URL}/generate_questions", json={"video_id": item['video_id']})
                        if q_response.status_code == 200:
                            questions = q_response.json()
                            for q in questions:
                                st.write(f"**Q: {q['question']}**")
                                options = q['choices']
                                answer = q['answer']
                                
                                selected = st.radio("Choose an answer:", options, key=f"q_{i}")
                                if st.button(f"Submit Answer for {q['question']}", key=f"submit_{i}"):
                                    if selected == answer:
                                        st.success("✅ Correct!")
                                    else:
                                        st.error(f"❌ Incorrect! The correct answer is: {answer}")
                        else:
                            st.error("Failed to generate questions. Try again!")
            else:
                st.warning("No results found.")
        else:
            st.error("Error fetching transcripts from the backend.")
    else:
        st.warning("Please enter a search term.")
