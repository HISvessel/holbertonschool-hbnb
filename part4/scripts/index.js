function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link')

    if (!token) {
        loginLink.style.display = 'block';
    } else {
        loginLink.style.display = 'none';
        //this will fetch the place data if user is authenticated
        fetchPlaces('token');
    }
}

function getCookieName() {
    //this will get a cookie value by its name
    //our code goes here
}

async function fetchPlaces(token) {
    const places = await fetch('http://127.0.0.1:5000/v1/place/all', {
        method: 'GET',
        body: {'content-type': 'application/json'},
        bearer: `{Authentication: ${token}}`, //authenticates token to fetch data
        body: '', //empty for now, should fetch place data
    })
}

function displayPlaces(places) {
    //clear the current content of the places list(the empty slots)
    //iterate over the place data with 'for place of places'
    //create a div for each place and set its contents there with textContent
    //append the created element to the new list with appendChild
}

document.getElementById('place-filter').addEventListener('change', (event) => {
    //get the selected place value
    //iterate over the places and show/hide them based on selected prices
})