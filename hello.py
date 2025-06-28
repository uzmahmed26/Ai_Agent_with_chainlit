import os
import chainlit as cl 

from agents import Agent, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from dotenv import load_dotenv, find_dotenv 
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from openai.types.responses import ResponseTextDeltaEvent

load_dotenv(find_dotenv())

gemini_api_key = "AIzaSyCob5rKYgQb49XxeLBco8JYCv5Bo6o-sXY"
#step 1: Provider

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
#step 2: Model
model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=provider,
)

run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

#step 3: Agent
agent1 = Agent(
    instructions="You are a helpful assistance that can answer question and ",
    name="Panaversity Support Agent"
)

#step 4 :Run
# result = Runner.run_sync(
#     input="What is the capital of France?",
#     run_config=run_config,
#     starting_agent=agent1
# )

# print(result.final_output)
@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history",[])
    await cl.Message(content="Hello! I am Panaversity Support Agent. How can I help you today?").send()
@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")

    msg = cl.Message(content="")
    await msg.send()

    history.append({"role": "user","content":message.content})
    result = Runner.run_streamed(
        agent1,
        input=history,
        run_config=run_config,
    )
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            await msg.stream_token(event.data.delta)

    history.append({"role":"assistant","content":result.final_output})
    cl.user_session.set("history", history)
    # await cl.Message(content=result.final_output).send()