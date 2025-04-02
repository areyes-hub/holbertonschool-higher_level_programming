document.addEventListener("DOMContentLoaded", () => {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => response.json())
        .then(data => {
            const helloTranslation = data["hello"];
            const hello = document.querySelector("#hello");
            hello.textContent = helloTranslation;
        })
        .catch(error => {
            console.error('Error fetching the translation:', error);
        });
});
