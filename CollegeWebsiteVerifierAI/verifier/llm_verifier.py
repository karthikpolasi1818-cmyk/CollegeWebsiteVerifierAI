import json

from openai import OpenAI

from config import OPENAI_API_KEY
from verifier.prompt_builder import PromptBuilder


class LLMVerifier:

    def __init__(self):

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

    def verify(self, college, candidate):

        prompt = PromptBuilder.build(
            college,
            candidate
        )

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        text = response.choices[0].message.content

        return json.loads(text)