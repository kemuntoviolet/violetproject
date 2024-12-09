let taskCreationForm = document.getElementById('addTasks');
let categoryCreationForm = document.getElementById('addNewCategory');


//Opening forms
function openNewTaskForm(){
    closeAddCategoryForm();
    taskCreationForm.style.display = 'block';
}
function openNewCategoryForm(){
    closeAddTasksForm();
    categoryCreationForm.style.display = 'block';
}

//Closing forms
function closeAddTasksForm(){
    taskCreationForm.style.display = 'none';
}

function closeAddCategoryForm(){
    categoryCreationForm.style.display = 'none';
}