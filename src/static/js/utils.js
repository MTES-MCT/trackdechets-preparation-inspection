(function () {
  document.addEventListener("DOMContentLoaded", function () {
    // Get the Établissements button
    const etablissementsBtn = document.querySelector(
      'button.fr-nav__btn[aria-controls="id_companies"]',
    );

    // Get the submenu
    const submenu = document.getElementById("id_companies");

    if (etablissementsBtn && submenu) {
      // Add click event listener
      etablissementsBtn.addEventListener("click", function () {
        // Get current state
        const wasExpanded =
          etablissementsBtn.getAttribute("aria-expanded") === "true";

        // Toggle the aria-expanded attribute
        etablissementsBtn.setAttribute(
          "aria-expanded",
          (!wasExpanded).toString(),
        );

        // Toggle the fr-collapse--expanded class on the submenu
        if (!wasExpanded) {
          submenu.classList.remove("fr-collapse");
          submenu.classList.add("fr-collapse--expanded");
          submenu.style.maxHeight = submenu.scrollHeight + "px";
        } else {
          submenu.classList.remove("fr-collapse--expanded");
          submenu.classList.add("fr-collapse");
          submenu.style.maxHeight = null;
        }
      });
    }
  });
})();
