# The Era of Agentic Application Programming

Good things are often hidden beneath the noise and distractions.

> **Agentic Application Programming(A2P)** is one such thing.

*While people are talking loudly about things like vibe coding and AI assisted coding, they missed a crucial usability of agents being part of your software run time alongside your code, in the same process and working in the same address space, not as a separate outside entity.*

*These agents will in turn call the functions within your code as and when required instead of us manually hardcoding the sequence within the code.*

>This is Agentic Application Programming (A2P).

## Why We Need Agentic Application Programming (A2P)?

Assume that you've build one of the most widely used, complex, and reliable security systems which uses levels of security, for example, Level - 1 to Level - 5 where 5 being the highest security zone for incoming requests.

Now, not all requests can be handled at Level - 5 security zone. It is not only costly but also takes a lot of time. If every request has to go through level - 5 then the customer service will be impacted drastically.

It's also possible for some requests to go through Level - 1 and then based on the outcome it can be rerouted to higher levels.

>What we're seeing over here, a programming nightmare of permutations and combinations.

Yes, we have a solution called machine learning, but even with machine learning, we'll have to write code to trigger these ML constructs and take decisions based on the outcomes of machine learning.

>Writing code (hardcoding) the scenarios is the smaller problem, the bigger problem is with respect to changing the code to accommodate new information and threat assessments. 

With Agentic Application Programming(A2P), we can ask agents to determine what level of security must be applied to the incoming requests and then agents can apply those. This is where the AI agents using LLM enabled intelligence comes into picture.

The best part is that we can not only use the agents to route the incoming requests, we can continuously train the underlying LLM or build new harness around agents to make it more accurate. 

> All without changing even a single line of code.

This is one of the most complex examples of Agentic Application Programming(A2P)Agentic
. There are other simple examples where it can be used, one of the same is of run time log analysis.

## Run-Time & In-Place Log Analysis
Historically, logs are analyzed separately outside of the running program. Logs are written in a separate file and the analyzed internally (within the system) or externally (outside of the system). 

With Agentic Application Programming(A2P), the agents can analyze the logs before its written on the file and can trigger possible proactive actions based on the contents of the logs. This may prevent lots of catastrophic failures and prevent vulnerability exploitation.

>Please note that the Agentic Application Programming(A2P) may not be suitable for in-depth analysis of the logs and is not a replacement of an existing mechanism of transferring and storing the logs in data lakes. 

## You Don't need to write code for everything

***
## Building a Simple Calculation Application with Agentic Programming

An AI agent is inherently capable of doing basic (and even complex) calculations which means, we don't need to write code for doing mathematical calculations. Here is a smallest and simplest example of an **Agentic Application Programming(A2P)** in python.

>In this program, we're using langchain and local LLM `gpt-oss` (via Ollama). So no API key is required.

Please note that this example omits lots of parameters so that I can explain the same in the simplest possible way.

```
from langchain.agents import create_agent  
from langchain_ollama import ChatOllama  
  
model = ChatOllama(model="gpt-oss:latest")  
  
agent = create_agent(  
    model=model,  
)  
  
first_variable = 100  
second_variable = 299  
  
result = agent.invoke(  
    {  
        "messages": [  
            {  
                "role": "user",  
                "content": f"What is the sum total of {first_variable} and {second_variable}?",  
            }  
        ]  
    },  
)  
  
print(result["messages"][-1].content)
```

This is an Agentic Application Program where agents uses its own capability of doing mathematical computations. Just change the variables `first_variable` and `second_variable` and you'll get the correct output.

When I run this code, here is the output i get

```
The sum of 100 and 299 is **399**.
```


___
## Calling a Success / Failure callback function, based on the outcome of the function call

In traditional programming, callbacks are the key to sequential executions of instructions based on the success or failure of the previous instructions/functions. Developers have to build this capability by checking the error conditions and the error conditions were manually listed. 

Here is a simple Agentic Application Programming(A2P) source code where the agents will call the success or failure function based on the error message.

>Note that the agents can call the appropriate function based on the tone of the error message. It doesn't needs to be hardcoded.

#### Tool Calling by the Agents
This is done by enabling tool calling by the AI agents in the program. This allow agents to call the function where the capabilities and the purpose of the function is stated in the function itself as a comment (in python at least).

Here is how the simplest possible code looks like

```
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
                "content": "Every function is executed successfully, Let's inform that Everything is Fine with 200 OK",  

            }  
        ]  
    },  
  
)  
```

The AI agent inside the code calls `print_success_message` and here is what I get as an output while running this code.

```
Hello! Looks like everything is going well. We got a success message: Everything is Fine with 200 OK
```

And if I change the content of the message with a message of failure as 

```result = agent.invoke(  
    {  
        "messages": [  
            {  
                "role": "system",  
                "content": "The function returned an error, Let's inform the user error code 404",  
            }  
        ]  
    }

```

The AI agent successfully calls `print_failure_message` and here is what I get as an output while running the code

```
Hello! Looks like we need to talk, we got an error: Error code 404
```

>Now I hope you can see how the agents can use the intelligence of the LLM's to call the appropriate functions. You can change the LLM (use a more capable or flagship model) without changing even the single line of code and you get a better agent behavior.

___

## Real-Time and In-Place monitoring of logs
As stated earlier, let's see and example where the AI agent is monitoring the logs generated by the execution of the program and can act if a log message is reporting something unusual.

In the code below, the AI agents looking at the logs is a proactive mechanism. Here is how the simple code which explains this concept looks like.

In the code below, before writing the logs to the local file, it is reviewed by the agent.

```
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

##########################################
```

Now the model is setup, let's create  the function which add the log message into the global log variable

```
log = ""  
  
def function_a():  
    global log  
    log = "Function A executed successfully."  
  
def function_b():  
    global log  
    log = "Function B executed successfully"  
 
```

Then before or after writing the log to the logfile, we can invoke the agent to look into the log message 
```
def write_log_to_file():  
    global log  
    with open("log.txt", "w") as f:  
        f.write(log)  
  
    # ask agent to check the log for any failure  
    agent_log_check(log)
```

And here is how our agent is setup

```
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
```

Now, its time to invoke the application as

```
if __name__ == "__main__":  
    function_a()  
    function_b()  
    write_log_to_file()
```

If the log generated by `function_a` and `function_b` doesn't contains any unusual contents, then the agents does nothing. 

However, if we change the log of any function with unusual message like

```
def function_b():  
    global log  
    log = "Function B Failed with access permission error"
```

The agents reports the failure in the log message of `function_b`

___
## The opportunities are limitless for Agentic Application Programming(A2P)

I've shared a few examples, but in reality, the limit is your imagination on how you want to build you product where and AI agent is the first class member of the house.

I'll keep on sharing more details on the same.

___
Thanks for Reading

Daksh


