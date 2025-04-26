# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv('.env')

def generate(note:str)->str:
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=note)
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        properties = {
                            "note_summary": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                        },
                    ),
        system_instruction=[
            types.Part.from_text(text="""Extract and keep only the most important information from the following note, and summarize it clearly and concisely:"""),
        ],
    )

    responce = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,)
    return responce.parsed['note_summary']


