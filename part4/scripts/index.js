function checkAuthentication() {
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link')

  if (!token) {
    loginLink.style.display = 'block';
  } else {
    loginLink.style.display = `none`; //we will attempt to reveal the user's name
    fetchPlaces('token');
  }
}

function getCookie(name) {
  const cookie = `; ${document.cookie}`; //gets the cookie
  const parts = cookie.split(`; ${name}=`);
  if (parts.length === 2) {
    return parts.pop().split(';').shift;
  }
  return null
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
    /* clear the current content of the places list(the empty slots)
    -> so, we would create an event to tap into the select the templates and make
    an empty list in preparation for the children to be appended


    iterate over the place data with 'places.forEACH' or with 'for place of places'
    
    create a div for each place and set its contents there with element.textContent
    append the created element to the new list with appendChild */
}

document.getElementById('place-filter').addEventListener('change', (event) => {
    //get the selected place value
    //iterate over the places and show/hide them based on selected prices
})

document.getElementById('amenity-filter').addEventListener('change', (event) => {
    //get the selected amenity values and 
    //iterate over the places and show/hide them based on selected amenities
})