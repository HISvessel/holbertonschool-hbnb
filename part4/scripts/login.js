document.addEventListener("DOMContentLoaded", () => {
const loginForm = document.getElementById("login-form");
const message = document.getElementById('message');

    if (loginForm) {
      loginForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const email = document.getElementById('email').value.trim()
        const password = document.getElementById('password').value.trim()
        const userAccountButton = document.getElementById('login-link') //gets the login button

        console.log(email, password)
        try {
            const response = await fetch('http://127.0.0.1:5000/v1/user/login', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ email, password }),
                //credentials: 'include' //including token for credentials
            });

            if(response.ok) {
                const result = await response.json()
                alert('Login successful')
                document.cookie = `token=${result.access_token}; path=/`;
                window.location.href = 'index.html';

                //attempting to convert login button to now say the user's name
                userAccountButton.innerHTML = `<li>${result.name}</li>`; //does not work yet
            }
            else {
                message.textContent = `Error type: ${result.error}`;
                message.style.color = 'red';
                alert('Login failed:' + response.statusText)
            }
        } catch (errors) {
            message.textContent = 'Network Error';
            message.style.color = 'red';
            console.error(errors)
        }
      });
    }
});