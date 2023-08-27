function reloadPage() {
  setTimeout(function () {
    location.reload();
  }, 5000); // 5 seconds
}
window.addEventListener("load", reloadPage);

// // List of URLs
// const urls = [
//   "https://randommeme-five.vercel.app/",
//   "https://randommeme-five.vercel.app/",
//   "https://randommeme-five.vercel.app/",
//   // Add more URLs here
// ];

// function changeWebsite() {
//   const randomIndex = Math.floor(Math.random() * urls.length);
//   const randomUrl = urls[randomIndex];
//   const websiteImage = document.getElementById("websiteImage");
//   websiteImage.src = randomUrl;
// }

// // Call the function to change the website URL initially
// changeWebsite();

// // Reload the page every 60 seconds
// function reloadPage() {
//   setTimeout(function() {
//       location.reload();
//   }, 5000); // 5 seconds
// }

// window.onload = function() {
//   reloadPage();
// };