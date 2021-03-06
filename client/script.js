const API_BASE = 'https://jsonplaceholder.typicode.com/todos'
let todosContainer = document.querySelector('.todos-container')

getAllTodos()

async function getAllTodos () {
    const response = await fetch(`${API_BASE}`)
    const todos = await response.json()

    todos.map((todo) => {
        let isCompleted = ''
        let isHighlighted = ''
        if(todo.completed){isCompleted = 'completed'}
        if(todo.highlighted){isHighlighted = 'highlighted'}

        const todoContent = `
            <div id="${todo.id}" class="todo-card ${isCompleted} ${isHighlighted}">
                <div class="todo-title-status-container">
                    <img src="./icons/checkbox.svg" class="check-off" />
                    <img src="./icons/checkbox-on.svg" class="check-on" />
                    <span>${todo.title}</span>   
                </div>
                <img src="./icons/star.svg" class="highlight-off" />
                <img src="./icons/star-on.svg" class="highlight-on" />
            </div>
        `
        
        todosContainer.innerHTML += todoContent
    })
}