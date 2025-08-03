document.addEventListener("DOMContentLoaded", () => {
const loginForm = document.getElementById("login-form");
const message = document.getElementById('message');

    if (loginForm) {
      loginForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const email = document.getElementById('email').value.trim()
        const password = document.getElementById('password').value.trim()
       
        console.log(email, password)
        try {
            const response = await fetch('http://127.0.0.1:5000/v1/auth/login/', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ email, password }),
                credentials: 'include' //including token for credentials
            });

            const result = await response.json()
            if(response.ok) {
                alert('Login successful')
                document.cookie = `token=${result.access_token}; path=/`;
                console.log("Confirming cookie generation:", document.cookie) //temporary
                window.location.href = 'index.html';

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