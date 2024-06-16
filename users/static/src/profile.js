var carrierBtn = document.getElementById("carrier-tablink");
var educationBtn = document.getElementById("education-tablink");
var personalBtn = document.getElementById("personal-tablink");

var carrierTab = document.getElementById("carrier");
var educationTab = document.getElementById("education");
var personalTab = document.getElementById("personal");

carrierBtn.addEventListener("click", function() {
    // change the button style
    educationBtn.classList.remove("active");
    personalBtn.classList.remove("active");
    carrierBtn.classList.add("active");

    // change the displayed tab
    educationTab.classList.add("no-display");
    personalTab.classList.add("no-display");
    carrierTab.classList.remove("no-display");
})

educationBtn.addEventListener("click", function() {
    // change the button style
    personalBtn.classList.remove("active");
    carrierBtn.classList.remove("active");
    educationBtn.classList.add("active");

    // change the displayed tab
    personalTab.classList.add("no-display");
    carrierTab.classList.add("no-display");
    educationTab.classList.remove("no-display");
})

personalBtn.addEventListener("click", function() {
    // change the button style
    educationBtn.classList.remove("active");
    carrierBtn.classList.remove("active");
    personalBtn.classList.add("active");

    // change the displayed tab
    educationTab.classList.add("no-display");
    carrierTab.classList.add("no-display");
    personalTab.classList.remove("no-display");
})

