# LinkedIn Post Generator AI Agent

An AI-powered LinkedIn post generator built with Python, Streamlit, LangChain, and Google Gemini. It helps users create professional and engaging LinkedIn posts by selecting a topic, language, tone, and preferred post length.

## Overview

Writing engaging LinkedIn content can be time-consuming. This project simplifies the process by using a Large Language Model (LLM) to generate structured LinkedIn posts based on user preferences.

The application provides a simple web interface where users can enter a topic, customize the writing style, and generate a ready-to-review LinkedIn post.

## Features

- **Topic-Based Generation:** Generate LinkedIn posts from any topic.
- **Multilingual Support:** Create posts in English or Bengali.
- **Customizable Tone:** Choose between Professional, Inspirational, and Storytelling styles.
- **Adjustable Length:** Generate Short, Medium, or Long posts.
- **AI-Powered Writing:** Uses Google Gemini to generate content.
- **Structured Content:** Prompts the model to include an engaging hook, 2–4 paragraphs, a closing question, and five relevant hashtags.
- **Interactive Web Interface:** Generate posts through a simple Streamlit application.

## Tech Stack

- **Programming Language:** Python
- **Frontend / Web Interface:** Streamlit
- **LLM Integration:** LangChain
- **AI Model:** Google Gemini 2.5 Flash
- **Environment Configuration:** python-dotenv

## Project Structure

```text
linkedin-post-agent/
├── app.py          # Streamlit application and AI generation logic
├── .gitignore      # Files excluded from version control
├── .env            # Environment variables (create locally)
└── README.md       # Project documentation
```

## Getting Started

Follow these steps to run the project locally.

### Prerequisites

- Python 3.10 or later
- pip
- A Google Gemini API key

### 1. Clone the Repository

```bash
git clone https://github.com/mhsakibb/linkedin-post-agent.git
cd linkedin-post-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install streamlit python-dotenv langchain-google-genai
```

### 4. Configure the Gemini API Key

Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).

Create a `.env` file in the project root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with your actual API key.

**Important:** Never commit your `.env` file or expose your API key in a public repository.

### 5. Run the Application

Execute the following command in your terminal:

```bash
streamlit run app.py
```

The application will start locally. Open the URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## How to Use

1. Open the application in your browser.
2. Enter the topic for your LinkedIn post.
3. Select your preferred language: English or Bengali.
4. Choose a tone: Professional, Inspirational, or Storytelling.
5. Select the post length: Short, Medium, or Long.
6. Click **Generate Post**.
7. Review the generated content and make any necessary edits before publishing.

## How It Works

The application follows a straightforward AI content-generation workflow:

1. **User Input:** Collects the topic, language, tone, and desired length.
2. **Prompt Construction:** Combines the selected preferences into a structured prompt.
3. **AI Processing:** Sends the prompt to Google Gemini through LangChain.
4. **Content Generation:** The model generates a LinkedIn post based on the specified requirements.
5. **Output Display:** Streamlit displays the generated post in the browser.

## Future Improvements

- Add editing and regeneration options based on user feedback.
- Provide multiple post variations for a single topic.
- Add customizable target audiences and writing styles.
- Include a copy-to-clipboard feature.
- Support additional languages.
- Introduce post history and draft management.
- Explore LinkedIn API integration for publishing, subject to the required permissions.

## Limitations

- An internet connection is required to access the Gemini API.
- A valid Google Gemini API key is required.
- Generated content may require manual review for accuracy, originality, and tone.
- The current implementation generates post content but does not automatically publish it to LinkedIn.

## Author

**MH Sakib**

- GitHub: [@mhsakibb](https://github.com/mhsakibb)

## License

No license has been specified for this repository yet. Add a license file if you intend to distribute the project under an open-source license.
