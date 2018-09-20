# Creates 35 different quizzes.
# • Creates 50 multiple-choice questions for each quiz, in random order.
# • Provides the correct answer and three random wrong answers for each
# question, in random order.
# • Writes the quizzes to 35 text files.
# • Writes the answer keys to 35 text files.

import random

def main():
    capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New \
     Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West \
    Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

    # os.makedirs('C:\\Users\\dkeshav\\Desktop\\Quiz')

    for quizNum in range(35):
        # Create the quiz and answer key files.
        quizFile= open('C:\\Users\\dkeshav\\Desktop\\Quiz\\capitalquiz%s.doc'%(quizNum+1),'a') 
        answerkeyFile= open('C:\\Users\\dkeshav\\Desktop\\Quiz\\answerKeys%s.doc'%(quizNum+1),'a')


        # Write out the header for the quiz.
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
        quizFile.write('\n\n')

        #Shuffle the order of the states.
        states = list(capitals.keys())
        random.shuffle(states)

        
        for quesNum in range(50):
            
            #Get right and wrong answers.
            correctAnswer = capitals[states[quesNum]]
            wrongAnswers = list(capitals.values())
            del wrongAnswers[wrongAnswers.index(correctAnswer)]
            wrongAnswers = random.sample(wrongAnswers, 3)
            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)

            #update the quiz file with questions and answers
            quizFile.write('%s. What is the capital of %s ?\n'%(quesNum+1,states[quesNum]))
            for i in range(4):
                quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
                quizFile.write('\n')
                # Write the answer key to a file.
                answerkeyFile.write('%s. %s\n' % (quesNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerkeyFile.close()        

if __name__=='__main__':
    main()