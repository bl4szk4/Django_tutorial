// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
});

let alertWrapper = document.querySelector('.alert');
let alertClose = document.querySelector('.alert__close');

if(alertWrapper) {
  alertClose.addEventListener("click",  (event)  => {
    alertWrapper.style.display = "none";
  }
)
}
