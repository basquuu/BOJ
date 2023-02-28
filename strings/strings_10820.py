while True :
    try :
        text = input()
        lower = sum(i.islower() for i in text)
        upper = sum(i.isupper() for i in text)
        num = sum(i.isdigit() for i in text)
        blank = sum(i.isspace() for i in text)
        print(lower,upper,num,blank)

    except EOFError :
        break
#프로그래머스에서 비슷한 문제 풀어봄 그리고 for 문 저렇게 작성했으면 소마 1차 편했겠다..