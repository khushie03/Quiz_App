Here’s a sample README file for your project. You can modify it according to any additional details or specific instructions you might have.

---

# Quiz App

## Overview

The Quiz App is a web-based application for generating and taking quizzes on various topics. It integrates with Google’s Generative AI for quiz question generation, Firebase for data storage, and provides PDF reports for quiz results and study materials.

## Features

- Generate multiple-choice quizzes on specified topics.
- Tailor quiz difficulty based on user input.
- Store user responses and scores in Firebase.
- Provide PDF reports of quiz results and relevant study materials.
- Send the reports to users via email.

## Technologies

- **FastAPI**: Web framework for building APIs.
- **Crewai**:It would help different LLM agents to connect with each other and have a seamless integration
- **Firebase**: Real-time database for storing user responses.
- **Google Generative AI (Gemini)**: For generating quiz questions.
- **FPDF**: For creating PDF reports.
- **Jinja2**: For templating HTML responses.

## Setup

### Prerequisites

- Python 3.8+
- Virtual environment (recommended)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/khushie03/Quiz_App.git
   cd quiz-app
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Firebase**

   - Download the Firebase Admin SDK JSON file.
   - Place it in the `C:/PROJECTS/Quiz App/quizapp-7bc35-firebase-adminsdk-4denh-cb7f1c9dab.json` path or update the path in `main.py`.

5. **Configure Google Generative AI**

   - Replace `"Your gemini api key"` with your actual API key in `main.py`.

6. **Run the Application**

   ```bash
   uvicorn main:app --reload
   ```

   The application will be available at `http://127.0.0.1:8000`.

## Usage

- **Homepage**: Access the homepage and start a quiz from `http://127.0.0.1:8000/`.
- **Leaderboard**: View the leaderboard at `http://127.0.0.1:8000/leaderboard`.
- **Generate Quiz**: Submit a form to generate a quiz by providing your name, email, topic, number of questions, and difficulty level.
- **Submit Quiz**: After taking the quiz, submit your answers to receive a PDF report of your results and study materials.

## YOUTUBE LINK :
https://youtu.be/QTJABO6i4Tk
## Error Handling

In case of errors, the application will display error pages with details. Common issues include:

- Incorrect Firebase credentials.
- Invalid or missing API key for Google Generative AI.
- Issues with generating or sending emails.

## Contributing

1. **Fork the Repository**: Create your own fork of the repository.
2. **Create a Branch**: For your changes.
3. **Commit Your Changes**: Ensure your changes are well-documented.
4. **Push to Your Fork**: And submit a pull request.

