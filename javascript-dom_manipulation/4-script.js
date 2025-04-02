const add_item = document.querySelector("#add_item");
const my_list = document.querySelector(".my_list");

add_item.addEventListener("click", () => {
    const list_item = document.createElement("li");
    list_item.textContent = "Item";
    my_list.appendChild(list_item);
});
