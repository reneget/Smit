import os
from openai import OpenAI

client = OpenAI(
    api_key="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"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)


# import openai
# from openai import OpenAI
#
# client = OpenAI()
#
# try:
#     client.finetuning.jobs.create(
#         model="gpt-3.5-turbo",
#         trainingfile="file-abc123",
#     )
# except openai.APIConnectionError as e:
#     print("The server could not be reached")
#     print(e.__cause)  # an underlying Exception, likely raised within httpx.
# except openai.RateLimitError as e:
#     print("A 429 status code was received; we should back off a bit.")
# except openai.APIStatusError as e:
#     print("Another non-200-range status code was received")
#     print(e.status_code)
#     print(e.response)








# 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
