/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/
/* ===================
PART 1: Login and Logout forms
======================*/


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
            const response = await fetch('http://localhost:5000/v1/auth/login/', {
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

/* ============================
PART 2: Index page, place adding and place filtering
=============================== */

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
        console.log("Prices match!");
      } else {
        card.style.display = 'none';
        console.log("No matches found for filter");
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