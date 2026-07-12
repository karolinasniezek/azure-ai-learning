# Azure AI Learning

Hands-on examples built while learning Azure AI Foundry and Azure AI services using Python.

## Overview

This repository contains small, focused examples demonstrating different Azure AI capabilities, including Azure OpenAI, Azure AI Language, Azure AI Vision, and Azure AI Projects.

## Repository

```
.
├── 01-model-chat-completion
├── 02-hosted-agent-client
├── 03-text-analysis
├── 04-computer-vision
├── requirements.txt
└── README.md
```

## Examples

| Directory | Description |
|-----------|-------------|
| `01-model-chat-completion` | Chat completion using Azure OpenAI deployed in Azure AI Foundry |
| `02-hosted-agent-client` | Connect to and interact with a hosted Azure AI Agent |
| `03-text-analysis` | Language detection, sentiment analysis and key phrase extraction |
| `04-computer-vision` | Image analysis and object detection |

## Technologies

- Azure AI Foundry
- Azure OpenAI
- Azure AI Language
- Azure AI Vision
- Azure AI Projects SDK
- Azure Identity
- Python

## Prerequisites

- Python 3.11+
- Azure subscription
- Azure AI Foundry project
- Azure AI resources

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project you want to run and configure the required Azure credentials.

## Status

Implemented:

- Azure OpenAI Chat Completion
- Azure AI Hosted Agents
- Azure AI Language
- Azure AI Vision

Planned:

- Azure AI Speech
- Azure AI Search
- Azure AI Document Intelligence
- Image Generation
- Retrieval-Augmented Generation (RAG)

This repository is intended for learning purposes.
