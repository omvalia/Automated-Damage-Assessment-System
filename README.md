### Damage Detection Application (LNRS Hackathon 2024)
## This project is developed for the LNRS Hackathon 2024 and focuses on the topic: "Damage Detection through Photos or Videos."

## Project Overview
The goal of this application is to extract audio narratives from user-captured videos that document damage areas for insurance claims. The application summarizes the audio and inserts the text summary into a pre-specified template for the insurance company to perform a first-level review using a Q&A approach. It is specifically designed for three types of claims:
1. Car Accident
2. Home Renovation
3. Medical Insurance

## Technology Stack
• Frontend: Streamlit (for creating a simple and interactive interface)
• 2Backend: Python (for processing the video and generating summaries)
• Libraries used:
  1. moviepy: Used to extract audio from the uploaded video.
  2. Whisper API: Converts the extracted audio into text (transcription).
  3. Gemini API: Summarizes the transcription based on a predefined prompt template and generates the summary.
The application provides a clear flow for insurance companies to easily upload videos and get a summarized description of what the user has said about the damage.

## Key Features
• Audio Extraction from Video: The application accepts videos and extracts the audio using the moviepy library.
• Speech-to-Text Conversion: Whisper API is used to transcribe the extracted audio into text for further processing.
• Summarization Using Gemini API: The Gemini API processes the transcription and generates a summary based on a predefined template that matches the specific type of insurance (Car, Home Renovation, or Medical).The API is configured with prompt templates for generating accurate summaries based on the context.
• Pre-Specified Summary Templates: Each type of claim (car accident, home renovation, medical insurance) has a predefined summary template to ensure consistency and clarity in the summaries provided.

## Workflow
• Video Upload: The user or insurance company uploads a video documenting the damage.
• Audio Extraction: The video’s audio is extracted using moviepy.
• Transcription: Whisper API converts the audio to text.
• Summary Generation: The Gemini API uses a prompt template to generate a summary of the damage based on the transcription.
• Q&A Ready Summary: The generated summary is inserted into a pre-specified template, ready for review.
