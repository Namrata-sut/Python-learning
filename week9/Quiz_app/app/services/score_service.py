from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from fastapi import Request
from app.models.score_model import Score
from app.models.user_model import User
from app.services.question_service import QuestionService


async def process_quiz_submission(request: Request, current_user: User, db: AsyncSession):
    """
    Processes a quiz submission, evaluates answers, and stores the user's score.
    Args:
        request: FastAPI Request object containing submitted form data.
        current_user: The authenticated user submitting the quiz.
        db: Async database session.
    return: A dictionary containing submission results, including correct answer count,
             total questions, and final score percentage.
    """
    # Extract form data
    form_data = await request.form()
    quiz_id_str = form_data.get("quiz_id", "0").strip()
    quiz_id = int(quiz_id_str)

    # Retrieve all questions for the given quiz
    questions = await QuestionService.get_by_quiz_id(quiz_id, db)
    total_questions = len(questions)

    # If no questions exist for the quiz, return an error
    if total_questions == 0:
        return {"error": "No questions found for this quiz."}

    correct_count = 0

    # Evaluate each question
    for question in questions:
        selected_answers = form_data.getlist(f"selected_options_{question.id}[]")
        correct_answers = [question.answer]

        if set(selected_answers) == set(correct_answers):
            correct_count += 1

    # Calculate score percentage
    score_percentage = (correct_count / total_questions) * 100

    # Store the quiz score in the database
    score_entry = Score(
        user_id=current_user.id,
        quiz_id=quiz_id,
        score=score_percentage,
        timestamp=text("'0 seconds'::INTERVAL")  # Placeholder timestamp
    )

    db.add(score_entry)
    await db.commit()

    return {
        "message": "Quiz submitted successfully!",
        "correct_count": correct_count,
        "total_questions": total_questions,
        "score": score_percentage,
        "quiz_id": quiz_id
    }
