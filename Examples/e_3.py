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

@tool("detect_failure_message")
def detect_failure_message(log_message : str) -> None:
    """Checks the logs message for the presence of any failure."""
    print(f"Function Called - Detecting failure in log message: {log_message}")
    return None


model = ChatOllama(model="gpt-oss:latest")

agent = create_agent(
    model=model,
    tools=[detect_failure_message]
)

log = ""

def function_a():
    global log
    log = "Function A executed successfully."

def function_b():
    global log
    log = "Function B executed successfully"

def write_log_to_file():
    global log
    with open("log.txt", "w") as f:
        f.write(log)

    # ask agent to check the log for any failure
    agent_log_check(log)

def agent_log_check(log_message: str):
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "system",
                    "content": f"check if any error is present in the {log_message} "
                               f"and if yes, please inform the user",
                }
            ]
        },
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    function_a()
    function_b()
    write_log_to_file()
