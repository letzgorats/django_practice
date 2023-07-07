from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


menu_dict = {
    "who Are U" : "Please enter Your name!",
    "Ranking" : "Here are rankings",
    "about Hint" : "Hint!",
}   


# index
def index(request):

    list_items = ""
    subjects = list(menu_dict.keys())   

    return render(request,"whoMain/index.html",{
        "subjects" : subjects
    })   

    for sub in subjects:
        capitalized_sub = sub.capitalize()
        sub_path = reverse("whoMain-guess",args = [sub])
        list_items += f"<li><a href = \"{sub_path}\">{capitalized_sub}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)





def whoAreU(request):

    return HttpResponse("Please enter Your name!")


def ranking(request):

    return HttpResponse("Ranking!")


def whoamI(request,mainClick):
    
    mainClickPage_text = None

    if mainClick == "whoAreU":
        mainClickPage_text = "Please enter Your name!"
    
    elif mainClick == "ranking":
        mainClickPage_text = "Here are rankings"

    else:
        return HttpResponseNotFound("Go back to MainPage")

    return HttpResponse(mainClickPage_text)



def whoamIstr(request,subject):

    try:
        mainClickPage_text = menu_dict[subject]
        response_data = render(request, 'whoMain/menu_content.html',{
            "text":mainClickPage_text,
            "subject_name": subject.capitalize()
        })
        # response_data = render_to_string("whoMain/menu_content.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Error!</h1>")

def whoamInumber(request,number):

    subjects = list(menu_dict.keys())  

    if number > len(subjects):
        return HttpResponseNotFound("Invalid!")
    redirect_subject = subjects[number-1]
    # originpath = "/whoMain/" +  redirect_subject
    redirect_path = reverse("whoMain-guess",args=[redirect_subject])    #  path('whoMain/whoAreU') 로 인식됨.

    return HttpResponseRedirect(redirect_subject)
