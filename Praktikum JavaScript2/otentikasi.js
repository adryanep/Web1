function login() {
    let username = document.getElementById("username");
    let password = document.getElementById("password");
    if(username.value == "ahmad2017" && password.value == "integrity"){
        window.location = "sukses.html";
    }else{
        alert("username atau password salah");
        username.value = "";
        password.value = "";
    }
}