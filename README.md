# Sentiment & Psychological Analysis



https://github.com/Prathamesh282001/Sentiment_And_Psychological_Analysis_LLM_Project/assets/122107260/bbb77194-1aa3-4566-aba5-caad8e645e5e



## Introduction

This document provides a comprehensive overview of the Sentiment & Psychological Analysis project, including the development of a web interface, integration of speech-to-text functionality, sentiment analysis using OpenAI, and deployment on Vercel.

## Project Overview

The project aims to develop a web interface for analyzing audio conversations to derive sentiment and psychological insights about the speakers involved. This involves the following components:

1. **Web Interface**: A user-friendly interface for users to upload audio files containing conversations.

2. **Speech-to-Text Conversion**: Functionality to convert audio files into text transcripts using the Deepgram API.

3. **Sentiment Analysis**: Utilization of OpenAI's GPT-3.5 model to analyze the transcribed text and provide sentiment and psychological insights.

4. **Deployment**: Deployment of the project on Vercel for accessibility via a public URL.

## Components

### 1. `app.py` (Flask Web Application)

- **Description**: Flask-based web application providing routes for serving HTML templates, handling file uploads, and processing audio files.
  
- **Routes**:
  - `/`: Home route returning a simple message indicating the purpose of the application.
  - `/upload`: POST route for handling file uploads and processing audio files.
  
- **Dependencies**: Flask framework, OpenAI API, Deepgram API.

### 2. `speech_to_text.py` (Speech-to-Text Conversion Module)

- **Description**: Module for converting audio files into text transcripts using the Deepgram API.
  
- **Function**:
  - `transcribe_audio`: Function to transcribe audio files into text using the Deepgram API.

- **Dependencies**: Requests library, Deepgram API.

### 3. `llm.py` (Sentiment Analysis Module)

- **Description**: Module for sentiment analysis and deriving psychological insights using OpenAI's GPT-3.5 model.
  
- **Function**:
  - `analyze_text`: Function to analyze text input and provide sentiment and psychological insights using the GPT-3.5 model.

- **Dependencies**: OpenAI Python SDK, OpenAI API.

### 4. `fastapiapp.py` (FastAPI Web Application)

- **Description**: FastAPI-based web application providing routes for handling file uploads and processing audio files.
  
- **Routes**:
  - `/`: Home route returning a simple message indicating the purpose of the application.
  - `/upload`: POST route for handling file uploads and processing audio files.
  
- **Dependencies**: FastAPI framework, OpenAI API, Deepgram API.

## Deployment

The project is deployed on Vercel, providing a public URL for accessibility. Users can access the web interface via the provided URL to upload audio files and receive sentiment and psychological insights.

URL : [https://voice-vibe-analyzer-mercys-projects-65fb0ef9.vercel.app]

## Conclusion

The Sentiment & Psychological Analysis project combines speech-to-text conversion and sentiment analysis to provide valuable insights from audio conversations. With its user-friendly interface and integration of advanced AI models, the project offers a powerful tool for understanding and analyzing human interactions.
