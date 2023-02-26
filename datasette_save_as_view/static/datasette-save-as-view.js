document.addEventListener("DOMContentLoaded", () => {
  // Only execute on table, query and row pages
  if (!document.querySelector(".sql")) {
    return
  }

  alert('save as view script loaded!');
});
