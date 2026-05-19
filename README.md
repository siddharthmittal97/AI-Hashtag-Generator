# AI Hashtag Generator

A Python CLI tool that generates relevant hashtags for social media posts using the Groq AI API (LLaMA 3.1).

## Setup

1. Install dependencies:
   ```bash
   pip install groq
   ```

2. Set your Groq API key as an environment variable:
   ```bash
   # Windows
   set GROQ_API_KEY=your_api_key_here

   # Mac/Linux
   export GROQ_API_KEY=your_api_key_here
   ```

   Get a free API key at [console.groq.com](https://console.groq.com).

## Usage

```bash
python hashtag_generator.py
```

Enter a description of your image or post when prompted, and the tool will generate relevant hashtags instantly.

## Example

```
What is the image/post about? sunset at the beach
#sunset #beach #ocean #travel #photography #nature #golden hour
```
