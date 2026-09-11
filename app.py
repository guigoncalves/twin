import os
from dotenv import load_dotenv

load_dotenv(override=True)

port = os.getenv("PORT") or os.getenv("GRADIO_SERVER_PORT") or "7860"
os.environ["GRADIO_SERVER_NAME"] = "0.0.0.0"
os.environ["GRADIO_SERVER_PORT"] = str(port)
os.environ["GRADIO_SSR_MODE"] = "false"

from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES
import gradio as gr

MODEL_NAME = "openai/gpt-5.4-mini"

openai = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


def chat(message, history):
    messages = system + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    while response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        tool_calls = message.tool_calls
        results = handle_tool_calls(tool_calls)
        messages.append(message)
        messages.extend(results)
        response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    return response.choices[0].message.content


if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Guigão",
        description="Online · chat with my digital twin about career, projects, and how to get in touch",
        chatbot=gr.Chatbot(show_label=False),
    ).launch(
        css=CSS,
        js=JS,
        theme=gr.themes.Base(),
        server_name="0.0.0.0",
        server_port=int(port),
        ssr_mode=False,
    )
