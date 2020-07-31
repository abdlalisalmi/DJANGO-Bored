const form = document.getElementById("form");
const select = document.getElementById("select");

select.addEventListener("change", () => {
  if (select.value) {
    select.classList.remove("is-invalid");
    form.submit();
  } else {
    select.classList.add("is-invalid");
  }
});
