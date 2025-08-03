function checkAuthentication() {
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link')

  if (token) {
    loginLink.style.display = 'block';
    console.log("Cookies not fetched. User, please login!")
  } else {
    console.log('We made it: cookie generated and fetched!');
    console.log("token is:", token) // checking token
    loginLink.innerHTML = '';
    const logoutLink = document.createElement('a');
    logoutLink.textContent = 'Logout';
    logoutLink.href= '#';
    logoutLink.id = 'logout-link';
    loginLink.appendChild(logoutLink);
    logoutUser()
    fetchPlaces(token);
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

async function logoutUser() {
  const logoutLink = document.getElementById('logout-link')
  logoutLink.addEventListener('click', async function(event) {
    event.preventDefault();

    if (!logoutLink) {
      console.warn("Logout link not rendered, skipping setup");
      return;
    }
    const token = getCookie('token');
    if (!token) {
      console.warn("No token here");
      return;
    }

    try{
      const response = await fetch("http://localhost:5000/v1/auth/logout", {
        method: "POST",
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`
        }
      });

      if (response.ok) {
        console.log("User logged out");
        alert("You have logged out. Goodbye.", + response.statusText)
      } else {
        console.error("Logout failed");
      }
    } catch (error) {
      console.error("Error logging out:", error)
    }
  });
}



/* This function is for manually ending session by forcibly expiring cookies*/
document.cookie.split(";").forEach(cookie => {
  const name = cookie.split("=")[0].trim();
  document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;path=/;';
});


/* function ends here*/





document.addEventListener("DOMContentLoaded", () => {
    checkAuthentication();
    //logoutUser();
});

async function fetchPlaces(token) {

  try{
    console.log("Fetching places")
    const response = await fetch('http://127.0.0.1:5000/v1/place/all', {
    method: 'GET',
    header: {'Authorization': `Bearer ${token}`
    }
  });
  if (!response.ok) throw new Error ("Cannot fetch places. Response not recieved!")
  
  const places = await response.json();
  displayPlaces(places);
  setupPriceFilter();
  console.log("Places have been fetched")
  } catch (error) {
    console.error("Could not fetch", error); //this error is being thrown
  }
}

function displayPlaces(places) {
  const placeList = document.getElementById('place-list');
  const template = document.getElementById("place-template");
  placeList.innerHTML = '';

  places.forEach(place => {
    const clone = template.content.cloneNode(true); //creates the div tag for places

    clone.querySelector('.place-name').textContent = place.title;
    clone.querySelector('.place-price').textContent = `Price: ${place.price}`;

    const placeDiv = clone.querySelector('.place-card');
    placeDiv.setAttribute('data-price', place.price);
    placeList.appendChild(clone);
  });

  console.log("Displaying places")
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
        console.log("Found a match for the filter!");
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