from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.csrf import csrf_exempt
from .forms import*
from .models import*
from django.http import HttpResponse
import os
import random
import hashlib
import subprocess
import requests

def home(request):
    return render(request,'home.html')

def userlogout(request):
    logout(request)
    return redirect('login')

def userlogin(request):
    if request.user.is_authenticated:
            return redirect('recruit')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('recruit')
       
    return render(request,'log.html')

def register(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    return render(request,'reg.html',{'form':form})


def mytest(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    return render(request,'mytest.html',{'form':form})
    

def recruit(request):
    practicals=Practical.objects.all()
    questions=Theorytest.objects.all()
    progress=Progress.objects.all()
    practicals=random.choice(practicals)

    score=0
    for p in progress:
        if p.engineer==request.user:
            score=p.scorebar

    return render(request,'recruiterx.html',{'practicals':practicals,'questions':questions,'score':score})

def createtest(request):
    form=PracticalForm()
    if request.method=='POST':
         testnumber=request.POST.get('test_number')
         title=request.POST.get('test_title')
         testname=request.POST.get('test_name')
         testdetails=request.POST.get('test_details')
         expectedresult=request.POST.get('expected_result')
         mk=request.POST.get('mark')

         Practical.objects.create(creator=request.user,test_number=testnumber,test_title=title,test_name=testname,test_details=testdetails,expected_result=expectedresult,mark=mk)
        
         return redirect('recruit')
    return render(request,'createprac.html',{'form':form})

@csrf_exempt
def practicaltest(request,id):
    practical=Practical.objects.get(id=id)
    questions=Theorytest.objects.all()
    context = {
            'questions':questions
        }
    
   
    if request.method=='POST':
        total_mark=0
        sol=request.POST.get('code')
        resul=str(request.session.get('result'))
        if resul==practical.expected_result:
            total_mark=10
            Progress.objects.create(engineer=request.user,scorebar=45)
        else:
            total_mark=0
        Answer.objects.create(practical_test=practical,candidate=request.user, solution=sol,candidate_result=resul, score=total_mark)
        #del request.session['result']
        #return redirect('recruit')
    
    return render(request,'practicaltest.html',{"practical":practical,'questions':questions})


@csrf_exempt
def compiler(request):
    if request.method == 'POST':
        language = request.POST.get('language').lower()
        code = request.POST.get('code')
         
        random_string = hashlib.md5(str(random.randint(1, 1000)).encode()).hexdigest()[:7]
        file_path = f"./media/{random_string}.{language}"

        with open(file_path, "w") as program_file:
            program_file.write(code)
        
        if language == "python":
            output = subprocess.getoutput(f"python {file_path}")
            request.session['result']=output
            return HttpResponse(output)
        
        elif language == "node":
            os.rename(file_path, file_path + ".js")
            output = subprocess.getoutput(f"node {file_path}.js 2>&1")
            return HttpResponse(output)
        
        elif language == "c":
            output_exe = random_string + ".exe"
            subprocess.getoutput(f"gcc {file_path} -o {output_exe}")
            output = subprocess.getoutput(f"{output_exe}")
            return HttpResponse(output)
        
        elif language == "cpp":
            output_exe = random_string + ".exe"
            subprocess.getoutput(f"g++ {file_path} -o {output_exe}")
            output = subprocess.getoutput(f"{output_exe}")
            return HttpResponse(output)

def answer(request):
    
    return HttpResponse()


def maketheory(request):
    form = TheoryForm()
    if request.method=='POST':
         que=request.POST.get('question')
         op1=request.POST.get('option1')
         op2=request.POST.get('option2')
         op3=request.POST.get('option3')
         op4=request.POST.get('option4')
         resp=request.POST.get('answer')

         Theorytest.objects.create(creator=request.user,question=que,option1=op1,option2=op2,option3=op3,option4=op4,answer=resp)
         return redirect('recruit')
    
    return render(request,'maketheory.html',{'form':form})

def theorytest(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Theorytest.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.answer == request.POST.get(q.question):
                print(request.POST.get(q.question))
                print("hey")
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        progress=Progress.objects.all()
        for p in progress:
            if p.engineer==request.user:
                if percent==100:
                     Progress.objects.create(engineer=request.user,scorebar=p.scorebar+45)
            
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'theoryresult.html',context)
    else:
        questions=Theorytest.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'theorytest.html',context)

