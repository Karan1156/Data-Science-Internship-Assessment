# assistant/views.py

import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
import fitz

from backend.utils import get_text_from_file
from backend.summarizer import generate_summary
from backend.qa_engine import get_chunks, create_vector_store, get_qa_chain, answer_question
from backend.challenge import generate_logic_questions, evaluate_user_answer

text_store = ""  # global variable to hold last uploaded document text

class UploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        global text_store
        uploaded_file = request.data.get("file")

        if not uploaded_file:
            return Response({"error": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)

        os.makedirs("temp", exist_ok=True)
        file_path = os.path.join("temp", uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        text_store = get_text_from_file(file_path)

        return Response({"message": "File uploaded and text extracted successfully."})

class SummaryView(APIView):
    def get(self, request):
        if not text_store:
            return Response({"error": "No document uploaded yet."}, status=400)
        summary = generate_summary(text_store)
        return Response({"summary": summary})

class AskQuestionView(APIView):
    def post(self, request):
        question = request.data.get("question")
        if not question:
            return Response({"error": "No question provided."}, status=400)

        chunks = get_chunks(text_store)
        vectorstore = create_vector_store(chunks)
        qa_chain = get_qa_chain(vectorstore)
        answer = answer_question(question, qa_chain)

        return Response({"answer": answer})

from rest_framework.views import APIView
from rest_framework.response import Response
from backend.challenge import generate_logic_questions

from rest_framework.views import APIView
from rest_framework.response import Response
from backend.challenge import generate_logic_questions

class ChallengeView(APIView):
    def get(self, request):
        global text_store

        if not text_store.strip():
            return Response({"error": "No document uploaded yet."}, status=400)

        try:
            questions = generate_logic_questions(text_store, num_questions=15)
            if not questions:
                return Response({"error": "No questions could be generated from the text."}, status=400)

            return Response({"questions": questions})
        except Exception as e:
            return Response({"error": str(e)}, status=500)

class EvaluateAnswerView(APIView):
    def post(self, request):
        question = request.data.get("question")
        answer = request.data.get("answer")
        if not question or not answer:
            return Response({"error": "Both question and answer are required."}, status=400)
        feedback = evaluate_user_answer(question, answer, text_store)
        return Response({"feedback": feedback})
