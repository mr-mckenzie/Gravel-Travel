
    const addButton = document.getElementById("addButton");
    const addDialog = document.getElementById("addDialog");
    const addCancel = document.getElementById("addCancel");
        
    // add button opens the add country dialog
    addButton.addEventListener("click", () => {
    addDialog.showModal();
    });

    // cancel button closes the add country dialog
    addCancel.addEventListener("click", () => {
    addDialog.close();
    });

