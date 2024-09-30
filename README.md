### Damage Detection Application (LNRS Hackathon 2024)
## This project is developed for the LNRS Hackathon 2024 and focuses on the topic: "Damage Detection through Photos or Videos."

## Project Overview
The goal of this application is to extract audio narratives from user-captured videos that document damage areas for insurance claims. The application summarizes the audio and inserts the text summary into a pre-specified template for the insurance company to perform a first-level review using a Q&A approach. It is specifically designed for three types of claims:
1. Car Accident
2. Home Renovation
3. Medical Insurance

## Technology Stack
1. Frontend: Streamlit (for creating a simple and interactive interface)
2. Backend: Python (for processing the video and generating summaries)
3. Libraries used:
  1. moviepy: Used to extract audio from the uploaded video.
  2. Whisper API: Converts the extracted audio into text (transcription).
  3. Gemini API: Summarizes the transcription based on a predefined prompt template and generates the summary.
The application provides a clear flow for insurance companies to easily upload videos and get a summarized description of what the user has said about the damage.

## Key Features
1. Audio Extraction from Video: The application accepts videos and extracts the audio using the moviepy library.
2. Speech-to-Text Conversion: Whisper API is used to transcribe the extracted audio into text for further processing.
3. Summarization Using Gemini API: The Gemini API processes the transcription and generates a summary based on a predefined template that matches the specific type of insurance (Car, Home Renovation, or Medical).The API is configured with prompt templates for generating accurate summaries based on the context.
4. Pre-Specified Summary Templates: Each type of claim (car accident, home renovation, medical insurance) has a predefined summary template to ensure consistency and clarity in the summaries provided.

## Workflow
1. Video Upload: The user or insurance company uploads a video documenting the damage.
2. Audio Extraction: The video’s audio is extracted using moviepy.
3. Transcription: Whisper API converts the audio to text.
4. Summary Generation: The Gemini API uses a prompt template to generate a summary of the damage based on the transcription.
5. Q&A Ready Summary: The generated summary is inserted into a pre-specified template, ready for review.