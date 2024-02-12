from openai import OpenAI

from app.config import settings

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=settings.SECRET_KEY_OPEN_AI,
)


def ask_gpt(request: str):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": request,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return response

