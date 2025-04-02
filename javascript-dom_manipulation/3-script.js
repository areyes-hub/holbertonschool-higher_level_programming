const header = document.querySelector("header");
const toggle_header = document.querySelector("#toggle_header");

toggle_header.addEventListener("click", () => {
    header.className = (header.className === "green") ? "red" : "green";
});
