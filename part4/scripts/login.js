document.addEventListener("DOMContentLoaded", () => {
const loginForm = document.getElementById("login-form");
const message = document.getElementById('message');

    if (loginForm) {
      loginForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const email = document.getElementById('email').value.trim()
        const password = document.getElementById('password').value.trim()

        try {
            const response = await fetch('https://reqres.in/api/login', {
                method: 'POST',
                headers: {'Content-type': 'application/json'},
                body: JSON.stringify({email, password})
            });
            
            const result = await response.json()

            if(response.ok) {
                document.cookie = token=$(response.access_token);
                window.location.href = 'index.html';
                document.textContent = 'Login successful';
                message.style.color = 'green';
                console.log('Token:', result.token);
            }
            else {
                message.textContent = `Error: ${result.error}`;
                message.style.color = 'red';
                alert('Login failed:' + response.statusText)
            }
        } catch (errors) {
            message.textContent = 'Network Error';
            message.style.color = 'red';
            console.error('Error', errors)
        }
      });
    }
});