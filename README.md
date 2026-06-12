# Banking Information Assistant

A simple Banking Information Assistant built using LangChain and Groq AI.

## Overview

This project uses:

* LangChain
* LangGraph
* Tavily
* Groq LLM
* Custom Tools
* Banking Knowledge Base

The Groq language model analyzes the user's question, selects the appropriate tool, retrieves information from the knowledge base, and generates a response.
If the answer is not present in the Knowledge base. it will search the web for the appropriate answer and generates a response based on the result provided by tavily.

The assistant only answers using information regarding the banking sector, it uses the knowledge base and web to generate the answer. It does not generate bank-specific information on its own.

## Features

* Banking FAQ Support
* Interest Rate Information
* Loan Details
* Card Type Information
* Supported Bank Information
* EMI Calculation
* Conversation Memory
* Web Search using Tavily.

## Technologies Used

* Python
* LangChain
* LangGraph
* Tavily
* Groq AI
* Custom Tool Calling

## Workflow

1. User asks a banking-related question.
2. The question is passed to the Supervisor agent.
3. The router in supervisor agent decides which route is to be used for the answer. Shown below are the two different routes.
   -Banking Agent for banking-related questions.
   -Search Agent for general information queries.
4. If it is a banking agent then, the agent invokes the appropriate retrieval tool to access the knowledge base.
5. If the answer is not present in the Banking agent, it will use the route: search for using the web search.
6. Relevant information is retrieved and provided as context to the Groq LLM.
5. The assistant generates a response using the retrieved information.
6. The final response is returned to the user.

## Note

The assistant relies on the provided knowledge base, tool outputs and Web Search. If query is not banking related, it will indicate that verified information is unavailable instead of generating unsupported answers.
