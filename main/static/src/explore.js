var searchBtn = document.getElementById("search-button");
var searchInput = document.getElementById("search-input");
var profileCards = document.querySelectorAll(".profile-card");

searchInput.addEventListener("input", function() {
    var searchTerm = searchInput.value.trim().toLowerCase();

    profileCards.forEach(function(card) {
        var name1 = card.querySelector(".profile-name").textContent.toLowerCase();
        var name2 = card.querySelector(".profile-name2").textContent.toLowerCase();
        var bio = card.querySelector(".profile-bio").textContent.toLowerCase();

        if(name1.includes(searchTerm) || 
            name2.includes(searchTerm) ||
            bio.includes(searchTerm))
        {
            card.classList.remove("no-display");
        }
        else
        {
            card.classList.add("no-display");
        }
    });
})

searchBtn.addEventListener("click", function() {})