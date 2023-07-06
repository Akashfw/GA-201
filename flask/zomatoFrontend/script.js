// Code to fetch menu items from the backend and display dynamically
function fetchMenuItems() {
    fetch('http://localhost:5000/menu') // Replace with your backend endpoint
      .then(response => response.json())
      .then(data => {
        const menuItemsContainer = document.getElementById('menu-items');
        menuItemsContainer.innerHTML = '';
  
        data.forEach(item => {
          const card = document.createElement('div');
          card.className = 'menu-item';
  
          const image = document.createElement('img');
          image.src = item.dish_img;
          image.alt = item.name;
          card.appendChild(image);
  
          const name = document.createElement('h3');
          name.textContent = item.dish_name;
          card.appendChild(name);
  
          const price = document.createElement('p');
          price.textContent = `Price: ${item.price}`;
          card.appendChild(price);
  
          const editButton = document.createElement('button');
          editButton.textContent = 'Edit';
          editButton.addEventListener('click', () => {
            // Handle edit functionality here
          });
          card.appendChild(editButton);
  
          const deleteButton = document.createElement('button');
          deleteButton.textContent = 'Delete';
          deleteButton.addEventListener('click', () => {
            // Handle delete functionality here
          });
          card.appendChild(deleteButton);
  
          menuItemsContainer.appendChild(card);
        });
      })
      .catch(error => {
        console.error('Error fetching menu items:', error);
      });
  }
  
  // Call the fetchMenuItems function to initially load the menu items
  fetchMenuItems();
  

  // Code to handle form submissions and update menu display
document.getElementById("add-menu-form").addEventListener("submit", function(event) {
    event.preventDefault();
    const dishId = parseInt(document.getElementById("dish_id").value); // Assuming you have an input field for dish_id
    const dishName = document.getElementById("dish-name").value;
    const dishImageURL = document.getElementById("dish-image-url").value;
    const dishPrice = parseFloat(document.getElementById("dish-price").value);
    const dishAvailability = document.getElementById("dish-availability").value === "available";
  
    const newDish = {
      dish_id: dishId,
      dish_name: dishName,
      dish_img: dishImageURL,
      price: dishPrice,
      availability: dishAvailability
    };
  
    fetch('http://localhost:5000/menu', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(newDish)
    })
    .then(response => response.json())
    .then(data => {
      // Handle the response data as needed
      // You may update the menu display or perform other actions
      fetchMenuItems();
      console.log(data);
    })
    .catch(error => {
      console.error('Error adding dish:', error);
    });
  
    // Reset the form
    document.getElementById("add-menu-form").reset();
  });
  