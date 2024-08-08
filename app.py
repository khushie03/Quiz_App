from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import google.generativeai as genai
import re

genai.configure(api_key="AIzaSyDM9xdKD9JDW_wu6Lp1gnCraUK3Ds-DPNc")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
def generate_questions(topic, number_of_questions):
    prompt = f"""
    You are an AI Quiz generator with respect to the specific topic. Generate {number_of_questions} multiple-choice questions on the topic: {topic}.
    This quiz will be an MCQ-based quiz, so for every question, you need to create 4 options with one correct answer.
    Format the response text as follows:
    **Question 1:**\n\nQuestion?\n\n(A) OptionA\n(B) OptionB\n(C) OptionC\n(D) OptionD\n\nResult: A,B,C,D
    """
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + f" Topic: {topic} Number of questions: {number_of_questions}")
    return response.text

def parse_questions(questions_text):
    question_pattern = re.compile(r"\*\*Question \d+:\*\*\n\n(.+?)\n\n\(A\) (.+?)\n\(B\) (.+?)\n\(C\) (.+?)\n\(D\) (.+?)\n\nResult: (.+)")
    matches = question_pattern.findall(questions_text)
    questions = []
    for match in matches:
        questions.append({
            "question": match[0],
            "option_a": match[1],
            "option_b": match[2],
            "option_c": match[3],
            "option_d": match[4],
            "result": match[5]
        })
    return questions

def provide_question(question):
    prompt = f"""
    You are an AI Quiz provider. Provide all the necessary information required for that question in about 350 words.
    Just in simple paragraph form. So that it would includes no * .
    In the format of paragraph. No highlighted points or bold text . Provide information information in a single paragraph """
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + question)
    return response.text

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate_quiz", response_class=HTMLResponse)
async def generate_quiz(request: Request, name: str = Form(...), email: str = Form(...), topic: str = Form(...), num_questions: int = Form(...)):
    try:
        questions_text = generate_questions(topic, num_questions)
        questions = parse_questions(questions_text)
        return templates.TemplateResponse("quiz.html", {
            "request": request,
            "name": name,
            "email": email,
            "topic": topic,
            "num_questions": num_questions,
            "questions": questions
        })
    except Exception as e:
        print(f"Error generating quiz: {e}")
        return templates.TemplateResponse("error.html", {"request": request, "error": str(e)})


@app.post("/submit_quiz", response_class=HTMLResponse)
async def submit_quiz(request: Request):
    try:
        form = await request.form()
        
        name = form.get("name", "").strip()
        email = form.get("email", "").strip()
        question_keys = [key for key in form.keys() if key.startswith("question_")]
        total_questions = len(question_keys)
        score = 0
        
        questions = []
        
        for i in range(total_questions):
            question_key = f"question_{i}"
            user_answer = form.get(question_key, "").strip()
            
            if not user_answer:  
                continue
            
            correct_answer = form.get(f"correct_answer_{i}", "").strip()
            question_text = form.get(f"question_text_{i}", "").strip()
            option_a = form.get(f"option_a_{i}", "").strip()
            option_b = form.get(f"option_b_{i}", "").strip()
            option_c = form.get(f"option_c_{i}", "").strip()
            option_d = form.get(f"option_d_{i}", "").strip()
            
            if question_text:
                questions.append({
                    "question": question_text,
                    "option_a": option_a,
                    "option_b": option_b,
                    "option_c": option_c,
                    "option_d": option_d,
                    "user_answer": user_answer,
                    "result": correct_answer,
                    "additional_info": provide_question(question_text) if question_text else ""  
                })
            
                if user_answer == correct_answer:
                    score += 10
        
        max_score = len(questions) * 10
        return templates.TemplateResponse("quiz_result.html", {
            "request": request,
            "name": name,
            "email": email,
            "questions": questions,
            "score": score,
            "total_questions": len(questions),
            "max_score": max_score
        })
    except Exception as e:
        print(f"Error submitting quiz: {e}")
        return templates.TemplateResponse("error.html", {"request": request, "error": str(e)})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
