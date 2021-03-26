from django.shortcuts import render
from django.http import HttpResponse
from random import randint

# Create your views here.
def index(request):
# def index(request, slug):
    # active = ""
    # if slug =="add":
    #     slug = "Addition"
    #     active = "active"
    # if slug =="sub":
    #     slug = "Subtraction"
    #     active = "active"
    # if slug =="mult":
    #     slug = "Multiplication"
    #     active = "active"
    # if slug =="div":
    #     slug = "Division"
    #     active = "active"
    # return HttpResponse("hii this is manish")
    # return HttpResponse("<h1>hii this is manish</h1>")
    # return render(request, "main.html", {"text": slug, "active": active})
    return render(request, "main.html")

def add(request):
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    answer = ""
    txt = "Addition"
    if request.method == "POST":
        answer = int(request.POST["answer"])
        old_num_1 = int(request.POST["old_num_1"])
        old_num_2 = int(request.POST["old_num_2"])
        correct_answer = old_num_1+old_num_2
        if  correct_answer == answer:
            my_answer = "Correct! " + str(old_num_1) + " + " + str(old_num_2) + " = " +str(answer)
            color = "primary"

        else:
            my_answer = "Incorrect! " + str(old_num_1) + " + " + str(old_num_2) + " is not " + str(answer)
            my_answer += " it will be: " + str(correct_answer)
            color = "danger"

        return render(request, "add.html", {"text": txt,
                                            "my_answer": my_answer,
                                            "answer": answer,
                                            "num_1": num_1,
                                            "color": color,
                                            "num_2": num_2
                                            })
    return render(request, "add.html", {"text": txt,
                                        "num_1": num_1,
                                        "num_2": num_2,
                                        "answer": answer,
                                        })

def sub(request):
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    answer = ""
    txt = "Subtraction"
    if request.method == "POST":
        answer = int(request.POST["answer"])
        old_num_1 = int(request.POST["old_num_1"])
        old_num_2 = int(request.POST["old_num_2"])
        print(old_num_1)
        print(old_num_2)
        correct_answer = old_num_1 - old_num_2
        if  correct_answer == answer:
            my_answer = "Correct! " + str(old_num_1) + " - " + str(old_num_2) + " = " +str(answer)
            color = "primary"

        else:
            my_answer = "Incorrect! " + str(old_num_1) + " - " + str(old_num_2) + " is not " + str(answer)
            my_answer += " it will be: " + str(correct_answer)
            color = "danger"

        return render(request, "sub.html", {"text": txt,
                                            "my_answer": my_answer,
                                            "answer": answer,
                                            "num_1": num_1,
                                            "color": color,
                                            "num_2": num_2
                                            })

    return  render(request, "sub.html", {"text": txt,
                                         "num_1": num_1,
                                         "num_2": num_2,
                                         "answer": answer,
                                         })

def mult(request):
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    answer = ""
    txt = "Multiplication"
    if request.method == "POST":
        answer = int(request.POST["answer"])
        old_num_1 = int(request.POST["old_num_1"])
        old_num_2 = int(request.POST["old_num_2"])
        correct_answer = old_num_1 * old_num_2
        if  correct_answer == answer:
            my_answer = "Correct! " + str(old_num_1) + " * " + str(old_num_2) + " = " +str(answer)
            color = "primary"

        else:
            my_answer = "Incorrect! " + str(old_num_1) + " * " + str(old_num_2) + " is not " + str(answer)
            my_answer += " it will be: " + str(correct_answer)
            color = "danger"

        return render(request, "mult.html", {"text": txt,
                                            "my_answer": my_answer,
                                            "answer": answer,
                                            "num_1": num_1,
                                            "color": color,
                                            "num_2": num_2
                                            })
    return  render(request, "mult.html", {"text": txt,
                                          "num_1": num_1,
                                          "num_2": num_2,
                                          "answer": answer,
                                          })

def div(request):
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    answer = ""
    txt = "Division"
    if request.method == "POST":
        answer = int(request.POST["answer"])
        old_num_1 = int(request.POST["old_num_1"])
        old_num_2 = int(request.POST["old_num_2"])
        if old_num_2!=0:
            correct_answer = old_num_1 / old_num_2
        else:
            correct_answer = "infinite"
        if  correct_answer == answer:
            my_answer = "Correct! " + str(old_num_1) + " / " + str(old_num_2) + " = " +str(answer)
            color = "primary"

        else:
            my_answer = "Incorrect! " + str(old_num_1) + " / " + str(old_num_2) + " is not " + str(answer)
            my_answer += " it will be: " + str(correct_answer)
            color = "danger"

        return render(request, "div.html", {"text": txt,
                                            "my_answer": my_answer,
                                            "answer": answer,
                                            "num_1": num_1,
                                            "color": color,
                                            "num_2": num_2
                                            })
    return  render(request, "div.html", {"text": txt,
                                         "num_1": num_1,
                                         "num_2": num_2,
                                         "answer": answer,
                                         })
