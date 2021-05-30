var uname = document.forms['loginform']['uname'];
var password = document.forms['loginform']['password'];

var uname_error = document.getElementById('uname_error');
var pass_error = document.getElementById('pass_error');


uname.addEventListener('textInput', uname_Verify);
password.addEventListener('textInput', pass_Verify);

function uname_Verify(){
    if (uname.value=="admin") {
        uname.style.border = "1px solid silver";
        uname_error.style.display = "none";
        return true;
    }
}
function pass_Verify(){
    if (password.value== "rajagiri") {
        password.style.border = "1px solid silver";
        pass_error.style.display = "none";
        return true;
    }
}

function validated(){
    if (uname.value== "admin") {
        if (password.value== "rajagiri") 
            return true;
        else {
            alert ("Login was unsuccessful, please check your username and password");
            return false;
        }
    }
    else {
        alert ("Login was unsuccessful, please check your username and password");
        return false
    }
}


