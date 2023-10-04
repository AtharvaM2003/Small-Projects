// Define a collection of Indian recipes
const indianRecipes = [
  {
    name: "Butter Chicken",
    instructions: "1. Marinate chicken in yogurt and spices.\n2. Cook chicken in a tomato-based sauce with butter and cream."
  },
  {
    name: "Chicken Biryani",
    instructions: "1. Cook marinated chicken with rice, spices, and saffron.\n2. Layer rice and chicken, then steam until done."
  },
  // Add more Indian recipes as needed
];

// Rest of the code remains the same

// Function to fetch a recipe based on user input
function fetchRecipe(query) {
  // Replace this with actual logic to fetch a recipe based on the user's input
  // You might use a loop to search through the array of recipes
  // For simplicity, let's assume the user provides the recipe name directly
  const lowerCaseQuery = query.toLowerCase();
  const foundRecipe = indianRecipes.find(recipe => lowerCaseQuery.includes(recipe.name.toLowerCase()));

  return foundRecipe;
}

// Modify the readOutLoud function to handle Indian recipes
function readOutLoud(message) {
  const speech = new SpeechSynthesisUtterance();
  speech.text = "I am not able to understand, sir";

  if (message.includes("Hello.")) {
    const finalText = "Hello! How can I assist you with recipes today?";
    speech.text = finalText;
  } else if (message.includes("recipe")) {
    const recipeName = extractRecipeName(message);
    const recipe = fetchRecipe(recipeName);

    if (recipe) {
      const finalText = `Here is the recipe for ${recipe.name}:\n${recipe.instructions}`;
      speech.text = finalText;
    } else {
      speech.text = "I couldn't find that recipe in my collection.";
    }
  }

  // Add more logic for different recipe-related queries as needed

  speech.volume = 1;
  speech.rate = 1.1;
  speech.pitch = 1;

  window.speechSynthesis.speak(speech);
}

// Rest of the code remains the same
