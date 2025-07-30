document.addEventListener("DOMContentLoaded", () => {
const loginForm = document.getElementById("login-form");
    if (loginForm) {
      loginForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const email = document.getElementById('email').value.trim()
        const password = document.getElementById('password').value.trim()

        try {
            const response = await fetch('http://localhost:5000/api/v1/login', {
                method: 'POST',
                headers: {'Content-type': 'application/json'},
                body: JSON.stringify({email, password})
            });
            
            const result = await response.json()

            if(response.ok) {
                
            }
        } catch {}
      });
    }
});