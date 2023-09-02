document.addEventListener("DOMContentLoaded", function () {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;

            var locationElement = document.getElementById("location");
            locationElement.textContent = "Latitude: " + latitude + ", Longitude: " + longitude;

            // Set hidden input field values
            document.getElementById("latitude").value = latitude;
            document.getElementById("longitude").value = longitude;
        },
        function (error) {
            var locationElement = document.getElementById("location");
            locationElement.textContent = "Error getting location: " + error.message;
        });
    } else {
        var locationElement = document.getElementById("location");
        locationElement.textContent = "Geolocation is not available in this browser.";
    }
});

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showMap);
  } else {
    alert("Geolocation is not supported by this browser.");
  }
}

//home page scrolling
function scrollToSection(sectionId) {
  const section = document.getElementById(sectionId);
  if (section) {
    section.scrollIntoView({ behavior: 'smooth' });
  }
}

// Add event listeners to the buttons to scroll to specific sections
document.addEventListener("DOMContentLoaded", function () {
  const whyButton = document.querySelector('.navigation-buttons button:nth-child(1)');
  const useButton = document.querySelector('.navigation-buttons button:nth-child(2)');
  
  if (whyButton) {
    whyButton.addEventListener('click', function () {
      scrollToSection('why');
    });
  }

  if (useButton) {
    useButton.addEventListener('click', function () {
      scrollToSection('use');
    });
  }
});
// Add event listeners to the buttons to scroll to specific sections
document.addEventListener("DOMContentLoaded", function () {
  const whyButton = document.querySelector('.navigation-buttons button:nth-child(1)');
  const useButton = document.querySelector('.navigation-buttons button:nth-child(2)');
  
  if (whyButton) {
    whyButton.addEventListener('click', function () {
      scrollToSection('why');
    });
  }

  if (useButton) {
    useButton.addEventListener('click', function () {
      scrollToSection('use');
    });
  }
});