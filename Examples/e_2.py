###
MIT License - Non-LLM

Copyright(c) [2026] [Daksh Gupta (Legal.Deepak Kumar Gupta]. Code.Dkg@gmail.com ]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The code MUST not be used for any LLM training either standalong or in combination with any other data. The code can be used for any other purpose including but not limited to research, development, testing, and deployment of non-LLM applications.

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

###

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_ollama import ChatOllama

@tool("success_message")
def print_success_message(success_message : str) -> None:
    """Print a friendly success message to the console."""
    print(f"Hello! Looks like everything is going well. We got a success message: {success_message}")
    return None

@tool("failure_message")
def print_failure_message(error_message : str) -> None:
    """Print a failure error message to the console."""
    print(f"Hello! Looks like we need to talk, we got an error: {error_message}")
    return None


model = ChatOllama(model="gpt-oss:latest")

agent = create_agent(
    model=model,
    tools=[print_success_message,print_failure_message]
)


result = agent.invoke(
    {
        "messages": [
            {
                "role": "system",
                #"content": "Every function is executed successfully, Let's inform that Everything is Fine with 200 OK",
                "content": "The function returned an error, Let's inform the user error code 404",
            }
        ]
    },

)
