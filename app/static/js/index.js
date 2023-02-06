const form = document.querySelector("#formData");
const saveBtn = document.querySelector("#submitBtn");
const dataContainer = document.querySelector("#dataContainer");
const messageContainer = document.querySelector("#messageContainer");

function showMessage(messageText, isSuccess) {
    const toggleClass = isSuccess ? "alert-success" : "alert-danger";
    messageContainer.classList.toggle(toggleClass);
    messageContainer.innerHTML = "";
    messageContainer.insertAdjacentHTML(
        "afterbegin",
        `<span>${messageText}</span>`
    );
    setTimeout(() => {
        messageContainer.classList.remove(toggleClass);
        messageContainer.innerHTML = "";
    }, 1000);
}

async function handleSaveData(e) {
    try {
        const isValid = form.checkValidity();
        e.preventDefault();
        e.stopPropagation();

        if (isValid) {
            const formData = new FormData(form);
            const userData = await fetch("", {
                method: "POST",
                body: formData,
            });

            saveBtn.disabled = true;
            if (!userData) {
                saveBtn.disabled = false;
                showMessage("Error, something went wrong!", false);
                return;
            }
            showMessage("User was successfully created!", true);

            form.reset();
            setTimeout(() => {
                form.classList.remove("was-validated");
            }, 0);
            setTimeout(async () => {
                const data = await fetch("get_data");
                saveBtn.disabled = false;

                dataContainer.innerHTML = "";
                dataContainer.insertAdjacentHTML("afterbegin", await data.text());
            }, 60000);
        }
        form.classList.add("was-validated");

    } catch (error) {
        console.log(error);
    }
}

saveBtn.addEventListener("click", handleSaveData);
