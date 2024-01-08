const buttonApplyFilters = document.getElementById("choose_passages_button_apply_filters");
const buttonSelectAll = document.getElementById("choose_passages_button_select_all");
const buttonDeselectAll = document.getElementById("choose_passages_button_deselect_all");
const tablePassages = document.getElementById("choose-passages-table-passages");
const tableRowsPassages = tablePassages.getElementsByTagName("tr");

buttonApplyFilters.addEventListener("click", () => {
    const checkboxes = document.querySelectorAll("input[type='checkbox'][name='topics']")
    const topicCheckboxes = {}

    checkboxes.forEach((checkbox) => {
        topicCheckboxes[checkbox.value.toLowerCase()] = checkbox.checked;
    });

    for (let i = 0; i < tableRowsPassages.length; i++) {
        const row = tableRowsPassages[i];
        const topic = row.getAttribute("topic");

        if (topicCheckboxes[topic.toLowerCase()]) row.classList.remove("hide");
        else row.classList.add("hide");
    }
});

buttonSelectAll.addEventListener("click", () => {
    const checkboxes = document.querySelectorAll("input[type='checkbox'][name='topics']")
    checkboxes.forEach((checkbox) => {
        checkbox.checked = true;
    });
});

buttonDeselectAll.addEventListener("click", () => {
    const checkboxes = document.querySelectorAll("input[type='checkbox'][name='topics']")
    checkboxes.forEach((checkbox) => {
        checkbox.checked = false;
    });
});