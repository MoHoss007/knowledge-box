const buttonSubmit = document.getElementById("quiz-button-submit");

buttonSubmit.addEventListener("click", () => {
    const radioButtons = document.querySelectorAll("input[type='radio']")
    
    radioButtons.forEach((radioButton) => {
        if (radioButton.checked) {
            console.log(radioButton.getAttribute("correct").toLowerCase());
            if (radioButton.getAttribute("correct").toLowerCase() === "true") {
                radioButton.parentElement.classList.add("correct-option");
            }
            else {
                radioButton.parentElement.classList.add("incorrect-option");
            }
        }
        
        radioButton.disabled = true;
    });

    buttonSubmit.disabled = true;
});