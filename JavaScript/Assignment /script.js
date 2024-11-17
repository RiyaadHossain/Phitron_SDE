let meals = [];
const mealCards = document.getElementById("mealCards");
const search_input = document.getElementById("search_input");
const selectedmealsList = document.getElementById("selectedmealsList");
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
  meals = await fetch(url)
    .then((res) => res.json())
    .then((res) => res.meals);

  console.log(meals);
  mealCards.innerHTML = "";
  rendermeals(meals);
};

const showDetails = async (id) => {
  const url = "https://www.themealdb.com/api/json/v1/1/lookup.php?i=" + id;
  const meal = await fetch(url)
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
  } = meal;
  detailsModal.innerHTML = `
        <div class="modal-content">
        <span class="close-btn" id="closeModal" onclick="handleOnClose()">&times;</span>
        <h2>meal Details</h2>
        <div class="meal-image">
          <img src="${strMealThumb}" alt="meal Image" />
        </div>
        <div class="meal-details">
          <h2 class="meal-name">${strMeal}</h2>
          <p class="meal-description">
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

const rendermeals = (meals) => {
  if (!meals) {
    mealCards.innerHTML = `<h1>No Item Found</h1>`;
    return;
  }

  let selectedmeals = [];

  function updateSelectedmeals() {
    selectedmealsList.innerHTML = selectedmeals
      .map((meal) => `<li>${meal}</li>`)
      .join("");
    selectedCount.textContent = selectedmeals.length;
  }

  meals.slice(0, 10).forEach((meal) => {
    const {
      strMeal,
      idMeal,
      strMealThumb,
      strTags,
      strCategory,
      strArea,
      strInstructions,
      strYoutube,
    } = meal;

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
      if (selectedmeals.length > 11) {
        alert("You can't add more than 11 palyers");
        return;
      }
      if (!selectedmeals.includes(strMeal)) {
        selectedmeals.push(strMeal);
        updateSelectedmeals();
      }
    });
    card.querySelector(".show-details").addEventListener("click", () => {
      showDetails(idMeal);
    });
    mealCards.appendChild(card);
  });
};

document.addEventListener("DOMContentLoaded", async () => {
  const url = "https://www.themealdb.com/api/json/v1/1/search.php?s=a";
  meals = await fetch(url)
    .then((res) => res.json())
    .then((res) => res.meals);

  rendermeals(meals);
});
