import os
from groq import Groq

client = Groq(
    api_key=""
)



def generate_questions(video_id: str, transcript_text: str):
    """Generate multiple-choice questions based on the transcript."""
    prompt = f"Generate a multiple-choice listening comprehension question based on the following transcript:\n\n{transcript_text[:1000]}\n\nProvide the question, 4 answer choices, and the correct answer in JSON format."
    
    try:
        response = client.chat.completions.create(
            model="deepseek-r1-distill-llama-70b",
            messages=[{"role": "system", "content": "You are a language learning assistant."},
                      {"role": "user", "content": prompt}],
           
        )
        generated_text = response["choices"][0]["message"]["content"]
        return generated_text  # Returns the generated questions as JSON
    except Exception as e:
        print(f"Error generating questions for {video_id}: {e}")
        return None