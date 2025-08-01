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
    setupPriceFilter();
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
  setupPriceFilter();
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
    placeDiv.setAttribute('data-price', place.price);

    placeList.appendChild(clone);
  });
}


function setupPriceFilter() {
  const priceContainer = document.getElementById('price-filter');
  priceContainer.innerHTML = '';
  
  const defaultOption = document.createElement('option');
  defaultOption.textContent = 'Any Price';
  defaultOption.value= '';
  
  const select = document.getElementById("price-filter");
  select.appendChild(defaultOption);


  const priceOptions = [50, 100, 200, 300, 400, 500];
  priceOptions.forEach(price => {
    const option = document.createElement('option');
    option.value = price;
    option.textContent = `${price}`;
    select.appendChild(option);
  });

  if (!select.dataset.listenerAdded) {
      select.addEventListener('change', (event) => {
    const selectedPrice = parseInt(event.target.value);
    const cards = document.querySelectorAll('#place-list .place-card');

    cards.forEach(card => {
      const cardPrice = parseInt(card.getAttribute("data-price"));
      if (!selectedPrice || cardPrice <= selectedPrice) {
        card.style.display = ''
        console.log("No prices");
      } else {
        card.style.display = 'none';
        console.log("No display")
      }
    });
  });
  select.dataset.listenerAdded = true;
  }
}


/*document.getElementById('amenity-filter').addEventListener('change', (event) => {
    //get the selected amenity values and 
    //iterate over the places and show/hide them based on selected amenities
}) */