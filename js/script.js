// Mobile nav toggle
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      links.classList.toggle('open');
    });
  }

  // Homepage hero slideshow: auto-cycles through images every few seconds.
  // Only runs on pages that actually have .hero-slide elements.
  var slides = document.querySelectorAll('.hero-slide');
  if (slides.length > 1) {
    var current = 0;
    setInterval(function () {
      slides[current].classList.remove('active');
      current = (current + 1) % slides.length;
      slides[current].classList.add('active');
    }, 5000); // 5 seconds per photo
  }

  // Inquiry form: submit via fetch to Formspree, then send the visitor to
  // a dedicated thank-you page so there's no mistaking whether it worked.
  var form = document.getElementById('inquiry-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = document.getElementById('form-status');
      var data = new FormData(form);
      var submitBtn = form.querySelector('button[type="submit"]');

      submitBtn.disabled = true;
      submitBtn.textContent = 'Sending...';

      fetch(form.action, {
        method: 'POST',
        body: data,
        headers: { Accept: 'application/json' }
      })
        .then(function (response) {
          if (response.ok) {
            window.location.href = 'thank-you.html';
          } else {
            response.json().then(function (data) {
              status.textContent =
                (data.errors && data.errors.map(function (e) { return e.message; }).join(', ')) ||
                'Something went wrong. Please email me directly instead.';
              status.style.color = '#b94a3a';
            });
          }
        })
        .catch(function () {
          status.textContent = 'Something went wrong. Please email me directly instead.';
          status.style.color = '#b94a3a';
        })
        .finally(function () {
          submitBtn.disabled = false;
          submitBtn.textContent = 'Submit';
        });
    });
  }
});
