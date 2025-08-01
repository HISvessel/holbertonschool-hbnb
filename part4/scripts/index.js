function checkAuthentication() {
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link')

  if (!token) {
    loginLink.style.display = 'block';
    console.log("Cookies not fetched.")
  } else {
    console.log('We made it: cookie generated and fetched');
    loginLink.style.display = `none`; //we will attempt to reveal the user's name
    fetchPlaces(token);
    populatePriceFilter();
  }
}

function getCookie(name) {
  const cookie = `; ${document.cookie}`; //gets the cookie
  const parts = cookie.split(`; ${name}=`);

  if (parts.length === 2) {
    return parts.pop().split(';').shift();
  }
  return null
}

document.addEventListener("DOMContentLoaded", () => {
    checkAuthentication();
});

async function fetchPlaces(token) {
  try{
    const response = await fetch('http://127.0.0.1:5000/v1/place/all', {
    method: 'GET',
    headers: {"Content-Type": 'application/json', 
                'Authorization' : `Bearer ${token}`
    }
  });
  if (!response.ok) throw new Error ("Failed to fetch places")
  
  const places = await response.json();
  displayPlaces(places);
  } catch (error) {
    console.error("Failed to fetch places", error);
  }
}

function displayPlaces(places) {
  const placeList = document.getElementById('place-list');
  const template = document.getElementById("place-template");
  placeList.innerHTML = '';

  places.forEach(place => {
    const clone = template.content.cloneNode(true); //creates the div tag for places

    clone.querySelector('.place-name').textContent = place.title;
    clone.querySelector('.place-price').textContent = place.price;
    //clone.querySelector('amenities').textContent = place.amenities;

    const placeDiv = clone.querySelector('.place-card');
    placeDiv.setAttribute('place-price', place.price)

    placeList.appendChild(clone)
  });
}

function populatePriceFilter() {
  const places = document.querySelectorAll('.place-list');
  const priceFilter = document.getElementById('price-filter');

  priceFilter.innerHTML = '';
  const prices = new set();

  places.forEach(place => {
    const price = parseInt(place.getAttribute('place.price'));
    if (typeof number(price)) {
      prices.add(price)
    }
  });

  const sortedPrices = Array.from(prices).sort((a, b) => a - b)

  const defaultOption = document.createElement('option');
  defaultOption.value = '';
  defaultOption.textContent= 'Any Price';
  priceFilter.appendChild(defaultOption);

  priceFilter.forEach(price => {
    const option = document.createElement('option');
    option.value = price;
    option.textContent = `${price}`;
    priceFilter.appendChild(option);
  });
}

document.getElementById('price-filter').addEventListener('change', (event) => {
    //get the selected place value
    //iterate over the places and show/hide them based on selected prices

  const selectedPrice = parseInt(event.target.value);
  const places = document.querySelectorAll('.place-list');

  places.forEach(place => {
    const price = parseInt(place.getAttribute('place-price'));
    place.style.display = price <= selectedPrice ? 'block' : 'none'; //determines if it fits the criteria or not
  });
})

/*document.getElementById('amenity-filter').addEventListener('change', (event) => {
    //get the selected amenity values and 
    //iterate over the places and show/hide them based on selected amenities
}) */