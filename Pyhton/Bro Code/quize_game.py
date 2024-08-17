def new_game() :
    question_num = 1 
    anss = []
    score = 0 
    for key in questions :
        print("-------------------------------------") 
        print(key) 
        for i in options[question_num-1] : 
            print(i)
        question_num+=1
        ans = input("Enter A or B , or C  : ").upper()
        anss.append(ans)
        score += check_ans(questions.get(key) , ans) 
    display_score(anss , score)


def check_ans(correct_ans , ans) : 
    return correct_ans == ans

def display_score(anss , score) : 
    print("answers     " , end=" ")
    for key  in questions  : print(questions.get(key) , end= " ")

    print("\nyour choise " , end=" ")

    for i in anss  : print(i , end= " ")
    # for i in score : print(i , end= " ")
    
    final_score = int((score/len(questions))*100)
    print( "\nscore : ", str(final_score)+"%")


def play_agine() : 
    return input("play againe? (y/n) : ").upper() == 'Y'  



questions = {"What is a correct syntax to output \"Hello World\" in Python?" : 'A' ,  
             "Which one is NOT a legal variable name?" : "B" , 
             "How do you create a variable with the numeric value 5?" : "C" ,
             "How do you insert COMMENTS in Python code?" : "C" 
             }


options = [
    ["A. print(\"hello world\")" , "B. p(\"hello wrold\")",  "C. echo(\"hello world\")"],
    ["A. my_var", "B. my-var", "C. _myvar"],
    ["A. both A and B are correct answer", "B. x = 5", "C. x = int(5)"],
    [r"A. / this is comment /", r"B. # this is comment", r"C. // this is comment"]  # Ensure it's part of the list
]

new_game()

while play_agine() : 
    new_game()

print("byeee")