from django.shortcuts import render
from .models import Question
import math

def quiz_view(request):
    questions = Question.objects.all()

    return render(request, 'quiz/quiz.html', {'questions': questions})



def quiz_result(request):
    if request.method == 'POST':
        score = 0
        total_questions = Question.objects.count()
        for question in Question.objects.all():
            user_answer = request.POST.get(str(question.id))
            if user_answer == question.correct_answer:
                score += 1
        grade = (score / total_questions) * 100
        grade = round(grade,2)
        return render(request, 'quiz/result.html', {'score': score, 'grade': grade, 'total': total_questions})
    else:
        return render(request, 'quiz/quiz.html')
