var form = document.getElementById("new-profile-form");

form.addEventListener("submit", function(event) {
    var username = document.getElementById("username").value;
    var fullName = document.getElementById("fullName").value;

    var isValid = true;

    document.getElementById("usernameError").textContent = "";
    document.getElementById("fullNameError").textContent = "";

    var usernameRegex = /^[a-zA-Z0-9]+$/;
    if((username.length != 0) && !usernameRegex.test(username))
    {
        document.getElementById("usernameError").textContent = "نام کاربری باید تنها شامل حروف و اعداد انگلیسی باشد";
        isValid = false;
    }

    var fullNameRegex = /^[\u0600-\u06FF\s]+$/
    if((fullName.length != 0) && !fullNameRegex.test(fullName))
    {
        document.getElementById("fullNameError").textContent = "نام کاربری باید تنها شامل حروف فارسی باشد";
        isValid = false;
    }

    
    if(!isValid)
    {
        event.preventDefault();
    }        
});