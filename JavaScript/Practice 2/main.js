const showDetails = async (mealId) => {
  const url = `https://www.themealdb.com/api/json/v1/1/lookup.php?i=${mealId}`;
  const { meals } = await fetch(url)
    .then((res) => res.json())
    .then((res) => res)
    .catch((err) => console.log(err));

  const div = document.createElement("div");
  div.classList.add("card");

  const meal = meals[0];

  div.innerHTML = `
           <img src="${meal.strMealThumb}" alt="Card Image" />
            <div class="card-content">
              <div class="card-content">
                <h3 class="card-title">${meal.strMeal}</h3>
                <div class="card-tags">
                  <span class="card-tag">${meal.strTags || "No Tag"}</span>
                </div>
                <ul class="card-list">
                  <li class="card-list-item">${meal.strIngredient1}</li>
                  <li class="card-list-item">${meal.strIngredient2}</li>
                  <li class="card-list-item">${meal.strIngredient3}</li>
                  <li class="card-list-item">${meal.strIngredient4}</li>
                  <li class="card-list-item">${meal.strIngredient5}</li>
                </ul>
            </div>
            </div>
      `;

  const card_details = document.getElementById("card_details");
  card_details.innerHTML = "";
  card_details.appendChild(div);
};

const createTag = (meal) => {
  const div = document.createElement("div");
  div.classList.add("card");

  div.innerHTML = `
         <img src="${meal.strMealThumb}" alt="Card Image" />
          <div class="card-content">
            <h3 class="card-title">${meal.strMeal}</h3>
            <p class="card-description">
            ${meal.strInstructions.slice(0, 150)}
            </p>
            <button onclick="showDetails('${meal.idMeal}')">Learn More</button>
          </div>
    `;

  return div;
};

const onHandleSearch = async () => {
  const inputText = document.getElementById("search_input").value;

  const url = `https://www.themealdb.com/api/json/v1/1/search.php?s=${inputText}`;
  const { meals } = await fetch(url)
    .then((res) => res.json())
    .then((res) => res)
    .catch((err) => console.log(err));

  const card_container = document.getElementById("card_container");

  const notFound = `<h2>Not Found any food item with '${inputText}'</h2>`;
  if (!meals) {
    card_container.innerHTML = "";
    card_container.innerHTML = notFound;
    return;
  }

  for (const meal of meals) card_container.appendChild(createTag(meal));
};
