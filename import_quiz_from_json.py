import os
import json

filenames = os.listdir(os.path.join(os.getcwd(), "samples"))
for filename in filenames:
    if filename.endswith(".json"):
        with open(os.path.join(os.getcwd(), "samples", filename), 'r') as json_file:
            json_data = json.load(json_file)
            for quiz in json_data:
                print("Câu hỏi: " + quiz['question'], end="\n\n")
                print("Các đáp án:" + str(quiz['answers']), end="\n\n")
                print("Đáp án đúng:" + quiz['answers'][quiz['correctAnswer']], end="\n\n")
                print("===========================================", end="\n\n")