window.onload = function() {
  setTimeout(() => {
    const envelope = document.getElementById('envelope');
    const letter = document.getElementById('letter');
    envelope.style.transform = 'rotateX(0)';
    letter.style.opacity = 1;
  }, 5000);
};

// Generate hearts
function createHeart() {
  const heart = document.createElement('div');
  heart.className = 'heart';
  heart.style.left = `${Math.random() * 100}vw`;
  heart.style.animationDuration = `${Math.random() * 2 + 3}s`;
  document.body.appendChild(heart);
  setTimeout(() => {
    heart.remove();
  }, 5000);
}

setInterval(createHeart, 300);
