    const deleteForm = document.getElementById("deleteForm");
    const deleteButton = document.getElementById("deleteButton");
    const confirmButton = document.getElementById("confirm");
    const deleteDialog = document.getElementById("deleteDialog");
    const editButton = document.getElementById("editButton");
    const editDialog = document.getElementById("editDialog");



    // delete button opens the delete dialog
    deleteButton.addEventListener("click", () => {
      deleteDialog.showModal();
    });

    // edit button opens the edit dialog
    editButton.addEventListener("click", () => {
      editDialog.showModal();
    });

    //confirm button submits the delete form
    confirmButton.addEventListener("click", () => {
      deleteForm.submit();
    });