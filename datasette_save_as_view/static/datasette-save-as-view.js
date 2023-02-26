document.addEventListener("DOMContentLoaded", () => {
  // Only execute on pages showing a query
  const sqlForm = document.querySelector(".sql");
  if (!sqlForm) {
    return
  }

  const initialViewName = 'view_name';
  const newElement = document.createElement('div');
  const database = window.location.pathname.split('/')[1];
  newElement.innerHTML = `<form id="viewCreateForm" action="/-/write" method="post">
  <input type="hidden" name="csrftoken" value="${getCsrfToken()}">
  <input type="hidden" name="database" value="${database}">
  <label for="viewname" class="sr-only">View Name&nbsp;&nbsp;<input type="text" id="viewname" value="${initialViewName}"></label>
  <input type="hidden" name="sql" id="viewSQL" value="${viewSql(initialViewName)}">
  <input type="submit" value="Save View">
</form>`;
  insertAfter(sqlForm, newElement);
  document.getElementById('viewname').addEventListener('change', updateSQL);
  document.getElementById('viewname').addEventListener('input', updateSQL);
});

function insertAfter(referenceNode, newNode) {
  referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}

function getSqlQuery() {
  return document.getElementById('sql-editor').value;
}

function getCsrfToken() {
  return 'stubbed';
}

function updateSQL (evt) {
  document.getElementById('viewSQL').value = viewSql(evt.target.value);
}

function viewSql(viewName) {
  return `CREATE VIEW ${viewName} AS ${getSqlQuery()}`
}
