fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then((response) => response.json())
    .then((rawData) => {
        const data = rawData["results"];
        const movieList = document.querySelector("#list_movies");
        for (const movie of data) {
            const title = document.createElement("li");
            title.textContent = movie["title"];
            movieList.appendChild(title);
        }
    })
    .catch((error) => {
        console.error("Error fetching the data", error);
    });
