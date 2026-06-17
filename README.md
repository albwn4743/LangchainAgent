# Banking Information Assistant

A simple Banking Information Assistant built using LangChain, LangGraph, Groq AI, and Model Context Protocol (MCP).

## Overview

This project uses:

* LangChain
* LangGraph
* Playwright
* Groq LLM
* Model Context Protocol (MCP)
* Custom Tools
* Banking Knowledge Base

The Groq language model analyzes the user's question, selects the appropriate tool, retrieves information from the knowledge base, and generates a response.

If the answer is not available in the knowledge base, the system searches the web for relevant information, scrapes the content from trusted sources, and generates an appropriate response based on the retrieved data.

The assistant only answers using information regarding the banking sector. It relies on its knowledge base, MCP tools, and web search results to generate responses. It does not generate bank-specific information on its own.

## Features

* Banking FAQ Support
* Interest Rate Information
* Loan Details
* Card Type Information
* Supported Bank Information
* EMI Calculation
* Compound Interest Calculation
* Currency Conversion
* Conversation Memory
* Web Automation using Playwright
* MCP Tool Integration

## Technologies Used

* Python
* LangChain
* LangGraph
* Playwright
* Groq AI
* Model Context Protocol (MCP)
* Custom Tool Calling

## MCP Integration

The project integrates a dedicated Financial MCP Server that exposes financial utility tools through the Model Context Protocol.

### MCP Tools

* EMI Calculator
* Compound Interest Calculator
* Currency Converter

The Banking Agent connects to the MCP Server through the LangChain MCP Client (`MultiServerMCPClient`) and automatically discovers the available financial tools.

This architecture separates financial calculations from the agent logic and demonstrates how reusable tools can be exposed through MCP and consumed by LangChain agents.

## Workflow

1. User asks a banking-related question.
2. The question is passed to the Supervisor Agent.
3. The router in the Supervisor Agent decides which route should be used to answer the user's query:

   * Banking Agent for banking-related questions.
   * Search Agent for general information queries.
   * Not Banking for questions related to domains other than banking.
4. If the Banking Agent is selected, it invokes the appropriate banking tools and MCP tools.
5. For financial calculations such as EMI, compound interest, and currency conversion, the Banking Agent communicates with the Financial MCP Server through the MCP Client.
6. If the required information is unavailable in the banking knowledge base, the Banking Agent routes the request to the Search Agent.
7. Playwright opens Chrome and searches for relevant websites containing the required information.
8. Relevant information is scraped and provided as context to the Groq LLM.
9. The assistant generates a response using retrieved banking information, MCP tool outputs, and web search results.
10. The final response is returned to the user.

##

## Note

The assistant relies on the provided knowledge base, MCP tool outputs, and web search results. If a query is not banking related, it will indicate that verified information is unavailable instead of generating unsupported answers.
