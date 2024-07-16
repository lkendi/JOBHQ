const flashMessage = document.getElementById('flash-messages');
if (flashMessage) {
  setTimeout(() => {
    flashMessage.style.opacity = '0';
    setTimeout(() => {
      flashMessage.remove();
    }, 500);
  }, 10000);
}
