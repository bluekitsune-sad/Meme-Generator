function reloadPage() {
  setTimeout(function () {
    location.reload();
  }, 5000); // 5 seconds
}
window.addEventListener("load", reloadPage);
