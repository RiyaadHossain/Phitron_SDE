let players = [];
const playerCards = document.getElementById("playerCards");
const search_input = document.getElementById("search_input");
const selectedPlayersList = document.getElementById("selectedPlayersList");
const selectedCount = document.getElementById("selectedCount");
const detailsModal = document.getElementById("detailsModal");
const handleOnClose = () => {
  detailsModal.style.display = "none";
};

const onHandleSearch = async (e) => {
  const search_text = search_input.value;
  console.log(search_text);

  const url =
    "https://www.themealdb.com/api/json/v1/1/search.php?s=" + search_text;
  players = await fetch(url)
    .then((res) => res.json())
    .then((res) => res.meals);
  
  console.log(players);
  playerCards.innerHTML = ''
  renderPlayers(players)
};

const showDetails = async (id) => {
  const url = "https://www.themealdb.com/api/json/v1/1/lookup.php?i=" + id;
  const player = await fetch(url)
    .then((res) => res.json())
    .then((res) => res.meals[0]);

  detailsModal.style.display = "flex";

  const {
    strMeal,
    strIngredient1,
    strIngredient2,
    strIngredient3,
    strIngredient4,
    strIngredient5,
    strInstructions,
    strMealThumb,
  } = player;
  detailsModal.innerHTML = `
        <div class="modal-content">
        <span class="close-btn" id="closeModal" onclick="handleOnClose()">&times;</span>
        <h2>Player Details</h2>
        <div class="user-image">
          <img src="${strMealThumb}" alt="User Image" />
        </div>
        <div class="user-details">
          <h2 class="user-name">${strMeal}</h2>
          <p class="user-description">
          ${strInstructions.slice(0, 250)}
          </p>
          <ul class="ingrediant-info">
            <li>${strIngredient1}</li>
            <li>${strIngredient2}</li>
            <li>${strIngredient3}</li>
            <li>${strIngredient4}</li>
            <li>${strIngredient5}</li>
          </ul>
        </div>
      </div>
      `;
};

const renderPlayers = (players) => {
  if (!players) {
    playerCards.innerHTML = `<h1>No Item Found</h1>`
    return
  }

  let selectedPlayers = [];

  function updateSelectedPlayers() {
    selectedPlayersList.innerHTML = selectedPlayers
      .map((player) => `<li>${player}</li>`)
      .join("");
    selectedCount.textContent = selectedPlayers.length;
  }

  players.slice(0, 10).forEach((player) => {
    const {
      strMeal,
      idMeal,
      strMealThumb,
      strTags,
      strCategory,
      strArea,
      strInstructions,
      strYoutube,
    } = player;

    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `
           <img
              src="${strMealThumb}"
              alt="Card Image"
              class="card-image"
            />
            <div class="card-content">
              <h2 class="card-title">${strMeal}</h2>
              <p class="card-description">
                ${strInstructions.slice(0, 150)}
              </p>
              <div class="card-details">
                <p><strong>Area:</strong> ${strArea}</p>
                <p><strong>Category:</strong> ${strCategory}</p>
                <p><strong>Tags:</strong> ${strTags}</p>
              </div>
              <div class="social-icons">
                <a href="${strYoutube}" target="_blank" class="icon">🌐</a>
                <a href="${strYoutube}" target="_blank" class="icon">📷</a>
              </div>
              <div class="card-actions">
                <button class="btn add-to-group">Add to Group</button>
                <button class="btn show-details">Show Details</button>
              </div>
            </div>
        `;

    card.querySelector(".add-to-group").addEventListener("click", () => {
      if (selectedPlayers.length > 11) {
        alert("You can't add more than 11 palyers");
        return;
      }
      if (!selectedPlayers.includes(strMeal)) {
        selectedPlayers.push(strMeal);
        updateSelectedPlayers();
      }
    });
    card.querySelector(".show-details").addEventListener("click", () => {
      showDetails(idMeal);
    });
    playerCards.appendChild(card);
  });
};

document.addEventListener("DOMContentLoaded", async () => {
  const url = "https://www.themealdb.com/api/json/v1/1/search.php?s=a";
  players = await fetch(url)
    .then((res) => res.json())
    .then((res) => res.meals);

  renderPlayers(players);
});
