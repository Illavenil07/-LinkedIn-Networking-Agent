import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Configure Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

def generate_message(target_name, target_role, company_name, topic):
    with open("prompts/base_prompt.txt", "r") as file:
        prompt_template = file.read()

    prompt = prompt_template.replace("[TARGET_NAME]", target_name)\
                            .replace("[TARGET_ROLE]", target_role)\
                            .replace("[COMPANY_NAME]", company_name)\
                            .replace("[TOPIC]", topic)

    response = model.generate_content(prompt)

    return response.text.strip()
