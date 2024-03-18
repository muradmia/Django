const loadData = (global)=>{
    // console.log("hello");
    const searchText = document.getElementById("input").value;
    console.log(searchText);
    fetch(`https://www.themealdb.com/api/json/v1/1/search.php?f=${searchText? searchText : global}`)
    .then(res => res.json())
    .then(data => displaydata(data.meals));
}

const displaydata = (data) =>{
    // console.log(data);
    document.getElementById("total").innerText= data.length;
   

    const mealcontainer  =document.getElementById("meals-container");

    data.forEach((meal) =>{
        console.log(meal);
        const card = document.createElement("div");
        card.classList.add("box");
        card.innerHTML = `
            <img class = "card-img" src="${meal.strMealThumb}" alt="">
            <h1>${meal?.strMeal}</h1>
            <p>${meal.strInstructions.slice(0,20)}</p>
            <button onclick = "displaymodal(${meal.idMeal})" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
            Details
            </button>
        `;
        mealcontainer.appendChild(card);
    });
};

const displaymodal = async(id) =>{
    try{
        const responce=await (fetch(`www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`));
        const data = await responce.json();
        console.log(data);
    }catch{
        err=>{
            console.log(err);
        }
    }
};

loadData("a");