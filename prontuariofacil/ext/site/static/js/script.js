var email = document.getElementById('email');

        email.addEventListener('focus',()=>{
                email.style.borderColor= "#19806d";
        });
        email.addEventListener('blur',()=>{
                email.style.borderColor= "#ccc";
            });
        var password = document.getElementById('password');

        password.addEventListener('focus',()=>{
                password.style.borderColor= "#19806d";
        });
        password.addEventListener('blur',()=>{
                password.style.borderColor= "#ccc";
            });