from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Category, Task
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date
# Create your views here.

#login view
#def index(request):
	    	
	#return render(request, 'myapp/index.html')
 
def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Set the session for the logged-in user
                request.session['user_username'] = user.username
                return redirect('home')  # Redirect to the homepage or another page
    else:
        form = AuthenticationForm()

    return render(request, 'myapp/index.html', {'form': form})

def search(request):
	    	
	return render(request, 'myapp/searchedtask.html')

#homepage view
def home(request):
	
	return render(request, 'myapp/home.html')


#Addcategory

@login_required
def addcategory(request):
    if request.method == 'POST':
        category_name = request.POST.get('categoryName')

        if category_name:
            try:
                category = Category(categoryName=category_name, categoryOwner=request.user.username)
                category.save()
                messages.success(request, 'Category added successfully!')
                return redirect('home')  # Replace 'home' with your desired redirect route
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")
        else:
            messages.error(request, 'Category name is required.')

    return render(request, 'myapp/addcategory.html')
  
  
  
  
#signup view
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after successful signup
            request.session['user_username'] = user.username   # Example: Store some data in the session after successful login/signup

            return redirect('home')  # Redirect to a home page or other after signup
    else:
        form = UserCreationForm()

    return render(request, 'myapp/signup.html', {'form': form})



#todaystasks view
def todaystasks(request):
    if request.method == 'POST':
        today = date.today()
        # Fetch tasks with today's date       
        tasks = Task.objects.filter(taskCreationDate=today, taskCategory__categoryOwner=request.user.username)


        # Pass the tasks to the template
        context = {
            'tasks': tasks
        }
        return render(request, 'myapp/todaystasks.html', context)
    else:
        # Redirect or handle invalid GET requests
        return render(request, 'myapp/viewalltasks.html')

#viewalltasks view
@login_required
def viewalltasks(request):
    if request.method == 'POST' and request.POST.get('view_all_tasks') == 'view_all_tasks':
        current_user = request.user.username
        
        # Fetch all categories owned by the user
        user_categories = Category.objects.filter(categoryOwner=current_user)
        
        # Create a dictionary to map categories to their tasks
        category_tasks_map = {
            category: Task.objects.filter(taskCategory=category) for category in user_categories
        }
        
        context = {
            'category_tasks_map': category_tasks_map
        }
        return render(request, 'myapp/viewalltasks.html', context)

    return render(request, 'myapp/viewalltasks.html')

def about(request):

	
	return render(request, 'myapp/about.html')

def logout_view(request):

	logout(request)
	return redirect('index')

def create_task(request):
	if request.method == 'POST':
	# Extract form data
		task_name = request.POST.get('taskName')
		task_description = request.POST.get('taskDescription')
		task_category_id = request.POST.get('taskCategory')
		task_status = 0 # Default to 0 if not provided

	# Validate and save the data
	if task_name and task_description and task_category_id:
		try:
			category = Category.objects.get(id=task_category_id)
			task = Task(
				taskName=task_name,
				taskDescription=task_description,
				taskCategory=category,
				taskStatus=task_status
			)
			task.save()
			messages.success(request, 'Task added successfully!')
			return redirect('home')  # Redirect to a task list or another page
		except Category.DoesNotExist:
			messages.error(request, 'Invalid category.')
	else:
		messages.error(request, 'All fields are required.')
    
    # Render the form if GET or if there was an error
	categories = Category.objects.all()  # Fetch all categories for the dropdown
	return render(request, 'home.html', {'categories': categories})