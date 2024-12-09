from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date, datetime
import logging
from django.utils.timezone import now


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



@login_required
def search(request):
    if request.method == "POST":
        task_name = request.POST.get('taskname')  # Get the task name entered in the search form
        
        
        # If a search query is provided, filter tasks by name
        if task_name:
            tasks = Task.objects.filter(taskName__icontains=task_name, taskOwner=request.user.username)
        else:
            tasks = Task.objects.none()  # No tasks found if no search term is provided

        return render(request, 'myapp/searchedtask.html', {'tasks': tasks})
    else:
        return render(request, 'myapp/searchedtask.html', {'tasks': []})  # Default empty list


#homepage view
def home(request):
	
	return render(request, 'myapp/home.html')
  
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
@login_required
def today_tasks(request):
    if request.method == 'POST':
        # Get today's date
        today_date = now().date()

        # Fetch tasks scheduled for today
        today_tasks = Task.objects.filter(
            taskOwner=request.user.username,
            taskScheduledFor=today_date
        )

        return render(request, 'myapp/todaystasks.html', {
            'today_tasks': today_tasks,
            'today_date': today_date
        })
    return redirect('home')  # Redirect if not a POST request



def about(request):

	
	return render(request, 'myapp/about.html')

def logout_view(request):

	logout(request)
	return redirect('index')

@login_required
def create_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('taskName')
        task_description = request.POST.get('taskDescription')
        task_category = request.POST.get('taskCategory')
        task_scheduled_for = request.POST.get('taskScheduledFor')

        # Check for missing fields
        if not task_name or not task_description or not task_category or not task_scheduled_for:
            messages.error(request, 'All fields are required.')
            return redirect('create_task')

        # Convert taskScheduledFor to a date object
        try:
            task_scheduled_for_date = datetime.strptime(task_scheduled_for, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, 'Invalid date format for Scheduled Date.')
            return redirect('create_task')

        # Save the task
        try:
            task = Task(
                taskName=task_name,
                taskDescription=task_description,
                taskCategory=task_category,
                taskOwner=request.user.username,  # Current logged-in user
                taskScheduledFor=task_scheduled_for_date,  # Save scheduled date
                taskStatus=0,  # Default task status
            )
            task.save()
            messages.success(request, 'Task added successfully!')
            return redirect('home')  # Redirect to the home page or wherever appropriate
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('create_task')

    return render(request, 'myapp/create_task.html')  # Render the form template

@login_required
def user_categories_and_tasks(request):
    print(f"Logged-in User: {request.user.username}")  # Debugging

    user_tasks = Task.objects.filter(taskOwner=request.user.username)
    print(f"User Tasks: {user_tasks}")  # Debugging

    categories_with_tasks = {}
    for task in user_tasks:
        print(f"Task Category: {task.taskCategory}")  # Debugging
        if task.taskCategory not in categories_with_tasks:
            categories_with_tasks[task.taskCategory] = []
        categories_with_tasks[task.taskCategory].append(task)

    print(f"Categories with Tasks: {categories_with_tasks}")  # Debugging

    return render(request, 'myapp/home.html', {
        'categories_with_tasks': categories_with_tasks
    })
    
    
@login_required
def add_task_to_category(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        task_name = request.POST.get('taskName')
        task_description = request.POST.get('taskDescription')
        task_scheduled_for = request.POST.get('taskScheduledFor')

        if category and task_name and task_description and task_scheduled_for:
            try:
                # Create the task and associate it with the category
                Task.objects.create(
                    taskCategory=category,
                    taskOwner=request.user.username,
                    taskName=task_name,
                    taskDescription=task_description,
                    taskScheduledFor=task_scheduled_for,
                )
                messages.success(request, f"Task '{task_name}' added to category '{category}' and scheduled for {task_scheduled_for}.")
            except Exception as e:
                messages.error(request, f"Failed to add task. Error: {str(e)}")
        else:
            messages.error(request, "Failed to add task. Ensure all fields are filled.")

    return redirect('home')

@login_required
def delete_task(request, task_id):
    # Ensure the task exists and belongs to the logged-in user
    task = get_object_or_404(Task, taskID=task_id, taskOwner=request.user.username)

    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully.")
        return redirect('home')
    
    
@login_required
def mark_complete(request, task_id):
    # Ensure the task exists and belongs to the logged-in user
    task = get_object_or_404(Task, taskID=task_id, taskOwner=request.user.username)

    if request.method == "POST":
        task.taskStatus = 1  # Mark as complete
        task.save()
        messages.success(request, "Task marked as complete.")
        return redirect('home')
    

@login_required
def fetch_tasks_by_date(request):
    scheduled_date = request.GET.get('scheduledDate')
    tasks_for_date = []

    if scheduled_date:
        tasks_for_date = Task.objects.filter(taskScheduledFor=scheduled_date, taskOwner=request.user.username)

    return render(request, 'myapp/schedule.html', {
        'scheduled_date': scheduled_date,
        'tasks_for_date': tasks_for_date,
    })
