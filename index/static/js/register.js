function formValidation() {
    name = document.getElementById("name").value
    email = document.getElementById("email").value
    address = document.getElementById("address").value
    ph = document.getElementById("ph").value
    dob = document.getElementById("dob").value


    name_p = document.getElementById("name_p")
    email_p = document.getElementById("email_p")
    address_p = document.getElementById("address_p")
    ph_p = document.getElementById("ph_p")
    dob_p = document.getElementById("dob_p")

    if (name, email, address, ph, dob == "") {
        name_p.innerHTML = "(required)"
        email_p.innerHTML = "(required)"
        address_p.innerHTML = "(required)"
        ph_p.innerHTML = "(required)"
        dob_p.innerHTML = "(required)"


        name_p.style.color = "rgb(139, 47, 47)"
        email_p.style.color = "rgb(139, 47, 47)"
        address_p.style.color = "rgb(139, 47, 47)"
        ph_p.style.color = "rgb(139, 47, 47)"
        dob_p.style.color = "rgb(139, 47, 47)"


        status = 1
    }
    else {
        name_p.innerHTML = ""
        email_p.innerHTML = ""
        address_p.innerHTML = ""
        ph_p.innerHTML = ""
        dob_p.innerHTML = ""
    }





    username = document.getElementById("username").value
    a = document.getElementById("username1")
    if (username.length < 4 && username.length > 1) {
        a.innerHTML = "must need more than 4 charecter"
        a.style.color = "rgb(139, 47, 47)"
        status = 1
    } else if (username == "") {
        a.innerHTML = "(required)"
        a.style.color = "rgb(139, 47, 47)"
        status = 1
    }
    else {
        a.innerHTML = " "
    }


    password1 = document.getElementById("password1").value
    cPassword = document.getElementById("cPassword").value
    pass_p = document.getElementById("pass_p")
    cPass_p = document.getElementById("cPass_p")
    pass_p.style.color = "rgb(139, 47, 47)"
    cPass_p.style.color = "rgb(139, 47, 47)"
    var lowerCaseLetters = /[a-z]/g;
    var upperCaseLetters = /[A-Z]/g;
    var numbers1 = /[0-9]/g;
    var specialChar = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/;
    if (password1.length < 6) {
        pass_p.innerHTML = "need more than 6 charecter"
        status = 1
    } else if (!password1.match(lowerCaseLetters)) {
        pass_p.innerHTML = "need atleast one lower letter"
        status = 1
    } else if (!password1.match(upperCaseLetters)) {
        pass_p.innerHTML = "need atleast one uppercase letter"
        status = 1
    } else if (!password1.match(numbers1)) {
        pass_p.innerHTML = "need atleast one number"
        status = 1
    }
    else if(!password1.match(specialChar)){
        pass_p.innerHTML = "need atleast any symbol"
        status = 1
    }
    else {
        pass_p.innerHTML = ""
    }


    if (password1 != cPassword) {
        cPass_p.innerHTML = "password should be same"
        status = 1
    } else {
        cPass_p.innerHTML = ""
    }











    if (status == 1) {
        return false
    } else {
        return true
    }

}









