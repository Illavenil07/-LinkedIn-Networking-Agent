# LinkedIn Networking Agent

A Python-based agent that helps generate personalized LinkedIn networking messages using Google's Gemini AI model.

## Features

- Generates personalized networking messages based on target profile information
- Uses Google's Gemini AI model for natural language generation
- Customizable prompts for different networking scenarios

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

The agent can be used to generate personalized messages by providing:
- Target name
- Target role
- Company name
- Topic of interest

## Requirements

- Python 3.x
- Google Gemini API key
- Required packages listed in `requirements.txt` 