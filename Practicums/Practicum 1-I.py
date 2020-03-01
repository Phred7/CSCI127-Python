quizScores = [];

numC = int(input("How many quizzes did you have?"));

for i in range(numC):
    score = int(input("What was your score on quiz "+str(i+1)+"?"));
    quizScores.append(score);
finalExam = int(input("What was you score on final exam?"));

for i in range(len(quizScores)):
    quiz = quiz + quizScores[i];
    
quizAverage = quiz/len(quizScores);
grade = (finalExam*0.6)+(quizAverage*0.4);

print("Your final grade percentage: "+str(grade));  

