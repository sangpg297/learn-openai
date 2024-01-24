from fastapi import FastAPI
from openai import OpenAI
from pathlib import Path
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

client = OpenAI(api_key="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")

app = FastAPI()
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


def chunk_string(input_string, chunk_size):
    """Chunk a string into smaller parts of a specified size."""
    return [
        input_string[i : i + chunk_size]
        for i in range(0, len(input_string), chunk_size)
    ]


@app.post("/chat")
def test(body: ChatRequest):
    try:
        # Text to speech
        # speech_file_path = Path(__file__).parent / "speech.mp3"
        # response = client.audio.speech.create(
        #     model="tts-1",
        #     voice="alloy",
        #     input="Today is a wonderful day to build something people love!",
        # )
        # response.stream_to_file(speech_file_path)
        # return Path(__file__).parent

        # Speech to text
        # audio_file = open(Path(__file__).parent / "speech.mp3", "rb")
        # transcript = client.audio.transcriptions.create(
        #     model="whisper-1", file=audio_file
        # )
        # return transcript.

        # Chat Completions
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "assistant", "content": "You are a helpful assistant."},
                {"role": "user", "content": body.message},
            ],
        )

        content = response.choices[0].message.content
        return content
    except Exception as exception:
        return str(exception)
