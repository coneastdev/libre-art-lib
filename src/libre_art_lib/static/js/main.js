function toggleTheme() {
    if (localStorage.getItem("theme") == "dark") {
        localStorage.setItem("theme", "light")
        document.body.setAttribute("data-bs-theme", "light");
    } else {
        localStorage.setItem("theme", "dark")
        document.body.setAttribute("data-bs-theme", "dark");
    }
}

function search(search_id) {
    if (search_id == "main") {
        window.location.href = '/search/q=' + document.getElementById('search').value;
    } else if (search_id == "nav") {
        window.location.href = '/search/q=' + document.getElementById('search-nav').value;
    }
}

function start() {
    if (localStorage.getItem("theme") == "dark") {
        document.body.setAttribute("data-bs-theme", "dark");
    }
}
