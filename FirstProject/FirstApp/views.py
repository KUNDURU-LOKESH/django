from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register

# Create your views here.
def home(request):
	return HttpResponse("Hi Good Evening to All...")

def htmltag(y):
	return HttpResponse("<h2>welcome to html<h2>")

def usernameprint(request,uname):
	return HttpResponse("<h3>Hi Welcome <span style='color:green'>{}</span><h3>".format(uname))

def usernameage(request,un,ag):
	return HttpResponse("<h1 style='text-align:center;background-color:green'>Hi user<span style='color:yellow'>{}</span> and your age is:<span style='color:red'>{}</span></h1>".format(un,ag))

def empdetails(request,eid,eage,ename):
	return HttpResponse("<script>alert('Hi Welcome {}')</script><h3>Hi Welcome {} and your age is {} and your id is {}</h3>".
		format(eid,eage,ename,ename))

def htm(request):
	return render(request,'html/sample.html')

def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})


def empname(request,id,ename):
	k={'i':id,'n':ename}
	return render(request,'html/ehtml.html',k)

def studentdetails(request):
	return render(request,'html/std.html')

def internaljs(request):
	return render(request,'html/internaljs.html')

def myform(req):
	if req.method=="POST":
		#print(req.POST)
		uname = req.POST['uname']
		rollno = req.POST['rollno']
		email = req.POST.get('email')
		#print(uname,rollno,email)
		data = {'username':uname,'rno':rollno,'emailid':email}
		return render(req,'html/display.html',data)

	return render(req,'html/myform.html')


def regform(request):
	if request.method == "POST":
		#print(request.POST)
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST.get('email')
		address = request.POST['address']
		gender = request.POST['gender']
		languages = request.POST.getlist('languages')
		country = request.POST['country']
		data = {'fname':fname,'lname':lname,'emailid':email,'address':address,'gender':gender,'languages':languages
		,'country':country}
		return render(request,'html/regdisplay.html',data)
	return render(request,'html/regform.html')

def bootstrapfun(request):
	return render(request,'html/sampleboot.html')


def btregi(req):
	return render(req,'html/bootreg.html')

def register(request):
	#name = "siva"
	#email = "siva@gmail.com"
	reg = Register(name = "rasool",email="rasool@gmail.com")
	reg.save()
	return HttpResponse("row inserted successfully...")

def register1(request):
	if request.method == 'POST':
		name1 = request.POST['fname']
		email1 = request.POST['email']
		reg = Register(name=name1,email=email1)
		reg.save()
		return HttpResponse("record inserted successful...")

	return render(request,"html/register1.html")

def display(request):
	data = Register.objects.all()
	return render(request,'html/display1.html',{'data':data})

def sview(request,y):
	w=Register.objects.get(id=y)
	return render(request,'html/sview.html',{'y':w})
	#return HttpResponse("your id is:{} and mail{}".format(w.name,w.email))


def supt(request,q):
	t = Register.objects.get(id=q)
	if request.method == "POST":
		na = request.POST['n']
		em = request.POST['e']
		t.name = na
		t.email = em
		t.save()
		return redirect('/display')
	return render(request,'html/supdate.html',{'p':t})

def sud1(request,p):
	b= Register.objects.get(id=p)
	if request.method == "POST":
		b.delete()
		return redirect('/display')
	return render(request,'html/sndlt.html',{'p':b})