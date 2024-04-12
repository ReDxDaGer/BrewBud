function toggleNavbar() {
  var x = document.getElementById("myNavbar");
  if (x.className === "navbar") {
    x.className += " responsive";
  } else {
    x.className = "navbar";
  }
}

const slider = document.querySelector('.slider');
  const slides = slider.querySelectorAll('.slide');
  let currentSlide = 0;
  const slideInterval = setInterval(nextSlide, 3000); // Change slide every 5 seconds

  function nextSlide() {
    slides[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add('active');
  }