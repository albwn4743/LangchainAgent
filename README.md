# Banking Information Assistant

A simple Banking Information Assistant built using LangChain and Groq AI.

## Overview

This project uses:

* LangChain
* Groq LLM
* Custom Tools
* Banking Knowledge Base

The Groq language model analyzes the user's question, selects the appropriate tool, retrieves information from the knowledge base, and generates a response.

The assistant only answers using information available in the knowledge base and does not generate bank-specific information on its own.

## Features

* Banking FAQ Support
* Interest Rate Information
* Loan Details
* Card Type Information
* Supported Bank Information
* EMI Calculation
* Conversation Memory

## Technologies Used

* Python
* LangChain
* Groq AI
* Custom Tool Calling

## Workflow

1. User asks a banking-related question.
2. LangChain sends the query to the Groq LLM.
3. The LLM identifies the appropriate tool.
4. The selected tool retrieves data from the knowledge base.
5. The assistant generates a response using the retrieved information.
6. The response is returned to the user.

## Note

The assistant relies on the provided knowledge base and tool outputs. If information is not available, it will indicate that verified information is unavailable instead of generating unsupported answers.
