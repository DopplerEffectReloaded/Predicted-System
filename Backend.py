PE1_WEIGHTAGE = 0.1
PE2_WEIGHTAGE = 0.1
PE_3WEIGHTAGE = 0.3
PE_Y2WEIGHTAGE = 0.4

#All grade boundaries are the Upper grade boundaries

EngSL = [9, 22, 34, 45, 59, 76, 100]
SpanishB = [5, 11, 24, 40, 56, 74, 100]
FrenchB = [9, 20, 32, 48, 64, 79, 100]
HindiBSL = [8, 19, 34, 48, 63, 78, 100]
EngHL = [12, 25, 35, 49, 61, 76, 100]
SpanishAB = [11, 22, 34, 49, 62, 77, 100]
FrenchAB = [10, 22, 36, 52, 65, 81, 100]
MathAAHL = [3, 11, 23, 37, 52, 68, 100]
MathAIHL = [3, 9, 18, 32, 46, 61, 100]
MathAASL = [3, 11, 22, 39, 57, 71, 100]
MathAISL = [3, 12, 24, 38, 54, 69, 100]
PhysicsHL = [13, 19, 28, 38, 53, 68, 100]
PhysicsSL = [9, 14, 25, 36, 49, 62, 100]
ChemistryHL = [14, 19, 34, 49, 66, 79, 100]
ChemistrySL = [4, 9, 23, 45, 60, 75, 100]
BiologyHL = [15, 23, 33, 46, 58, 75, 100]
BiologySL = [11, 21, 30, 43, 58, 74, 100]
PsychologyHL = [7, 16, 28, 41, 52, 65, 100]
PsychologySL = [5, 11, 18, 35, 49, 65, 100]
DigitalSocietiesHL = [29, 39, 49, 59, 71, 84, 100]
DigitalSocietiesSL = [29, 39, 49, 59, 71, 84, 100]
GlobalPoliticsHL = [9, 19, 28, 39, 50, 61, 100]
GlobalPoliticsSL = [6, 18, 28, 37, 48, 58, 100]
VisualArtsHL = [7, 17, 33, 47, 62, 76, 100]
VisualArtsSL = [8, 17, 31, 45, 62, 76, 100]
EconomicsHL = [8, 17, 26, 39, 53, 66, 100]
EconomicsSL = [9, 19, 30, 43, 58, 71, 100]
BusinessManagementHL = [10, 24, 33, 45, 54, 64, 100]
BusinessManagementSL = [9, 17, 26, 39, 53, 66, 100]

def Predictor(PE1, PE2, PE3, PE_Y2, sub_grade, weightagePE1, weightagePE2, weightagePE3, weightagePE1Y2):

    '''This function takes your marks as input and then predicts 
        how many marks you need to obtain in your next exam to get the next grade according to the 
        IB grade boundaries for all the exams'''
    
    #checking if PE2 exam has been taken
    if PE2 is None:

        current_grade = 1 #lowest possible grade           
        for i in range(0, 7):
            
            d = sub_grade[i] #sub_grade is the IB grade boundary

            if weightagePE1*PE1 >= weightagePE1*d:
                current_grade += 1 #incrementing current grade if marks in PE1 are greater than the grade boundary

        future_grade  = current_grade + 1 #next possible grade

        #Handling case when future grade is 7
        if (future_grade - 7) >= 1:

            future_grade = 'N/A, highest grade achieved'
            future_marks = 'N/A, highest grade achieved'
            return ([current_grade, future_grade, future_marks])

        else:

            boundary = sub_grade[future_grade-1]

            #calculating future marks based on next grade boundary
            future_marks = ((boundary*(weightagePE1+weightagePE2))-weightagePE1*PE1)/weightagePE2
            return ([current_grade, future_grade, round(future_marks, 1)])

    #checking if PE3 exam has been taken
    elif PE3 is None:

        y = weightagePE1*PE1 + weightagePE2*PE2 #calculating current weighted marks

        current_grade = 1

        for i in range(0, 7):

            f = sub_grade[i]

            if y >= (weightagePE1*f) + (weightagePE2*f):

                #same logic as PE2 case
                current_grade += 1

        future_grade  = current_grade + 1

        if (future_grade - 7) >= 1:

            future_grade = 'N/A, highest grade achieved'
            future_marks = 'N/A, highest grade achieved'
            return ([current_grade, future_grade, future_marks])

        else:

            boundary = sub_grade[future_grade-1]
            future_marks = ((boundary*(weightagePE1+weightagePE2+weightagePE3)) - y)/weightagePE3
            return ([current_grade, future_grade, round(future_marks, 1)])
    
    #checking if PEY2 exam has been taken
    elif PE_Y2 is None:

        z = weightagePE1*PE1 + weightagePE2*PE2 + weightagePE3*PE3 #calculatin current marks
        current_grade = 1

        for i in range(0, 7):

            j = sub_grade[i]

            if z >= (weightagePE1*j) + (weightagePE2*j) + (weightagePE3*j):
                current_grade += 1

        future_grade  = current_grade + 1

        if (future_grade - 7) >= 1:

            future_grade = 'N/A, highest grade achieved'
            future_marks = 'N/A, highest grade achieved'
            return ([current_grade, future_grade, future_marks])

        else:

            boundary = sub_grade[future_grade-1]
            future_marks = ((boundary*(weightagePE1+weightagePE2+weightagePE3+weightagePE1Y2)) - z)/weightagePE1Y2
            return ([current_grade, future_grade, round(future_marks, 1)])

    # this is the case when all exams have been taken
    else:

        m = weightagePE1*PE1 + weightagePE2*PE2 + weightagePE3*PE3 + weightagePE1Y2*PE_Y2
        current_grade = 1
        for i in range(0, 7):

            j = sub_grade[i]

            if m >= (weightagePE1*j) + (weightagePE2*j) + (weightagePE3*j) + (weightagePE1Y2*j):
                current_grade += 1
            future_grade = 'N/A, all exams have been taken'
            future_marks = 'N/A, all exams have been taken'
        return ([current_grade, future_grade, future_marks])

def main():
    #test case to check working
    subject_name = "English"
    level = "SL"
    PE1 = 70
    PE2 = 80
    PE3 = 90
    PE_Y2 = None
    sub_grade = [9, 22, 34, 45, 59, 76, 100]

    print(Predictor(PE1, PE2, PE3, PE_Y2, sub_grade, PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE_3WEIGHTAGE, PE_Y2WEIGHTAGE))

#calling main function
if __name__ == '__main__':
    main()
