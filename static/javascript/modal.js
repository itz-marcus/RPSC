document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("myModal");
    const openModalButton = document.getElementById("openModal");
    const closeModalButton = document.querySelector(".close");
    if (openModalButton) {
      openModalButton.addEventListener("click", () => {
        modal.style.display = "flex";
      });
    }
    if (closeModalButton) {
      closeModalButton.addEventListener("click", () => {
        modal.style.display = "none";
      });
    }
    window.addEventListener("click", (event) => {
      if (event.target === modal) {
        modal.style.display = "none";
      }
    });
  });
  console.log(document.getElementById("openModal")); // Should not be null
  console.log(document.getElementById("myModal"));
  console.log(document.querySelector(".close"));