// Navbar
let btnNav = document.querySelector(".btn-nav");
let navContainer = document.querySelector(".nav-menu");
let btnClose = document.querySelector(".btn-close");

btnNav.addEventListener("click", openNavMenu);
btnClose.addEventListener("click", closeNavMenu);

function openNavMenu() {
  navContainer.style.display = "block";
}

function closeNavMenu() {
  navContainer.style.display = "none";
}

// Fetch API
const apiBaseUrl = 'https://jsonplaceholder.typicode.com/todos'
let todosContainer = document.querySelector('.todos-container')

getAllTodos()

async function getAllTodos () {
  const response = await fetch(`${apiBaseUrl}`)
  const todos = await response.json()

  todos.map((todo) => {
    const todoContent = `
      <div id="${todo.id}" class="todo-card ${todo.completed ? "completed" : ""} ${todo.highlighted ? "highlighted" : ""}">
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