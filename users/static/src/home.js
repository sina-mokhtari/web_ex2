// var profileCards = document.querySelectorAll(".profile-card");

// profileCards.forEach(function(card) {
//     card.addEventListener("click", function() {
//         var cardID = card.getAttribute("card-id");

//         window.location.href = "profile_" + cardID + ".html";
//     })
// })

var profileNames = document.querySelectorAll(".profile-name");

var counter = 0;
profileNames.forEach(function(name) {
    // underline the name when mouse over
    name.addEventListener("mouseover", function() {
        name.classList.add("underline");
    })

    // remove the underline when mouse out
    name.addEventListener("mouseout", function() {
        name.classList.remove("underline");
    })
})