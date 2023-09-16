document
  .getElementById("nutritionForm")
  .addEventListener("submit", function (e) {
    //e.preventDefault();

    const predictionArray = prediction_array;
    print(predictionArray);
    // Get a reference to the <ul> element
    const predictionList = document.getElementById("predictionList");

    // Iterate through the array and create list items
    predictionArray.forEach((item) => {
      const listItem = document.createElement("li");
      listItem.textContent = item;
      predictionList.appendChild(listItem);
    });

    //   const userInput = document.getElementById("user_input").value;

    //   fetch("/", {
    //     method: "POST",
    //     body: new URLSearchParams({ user_input }),
    //     headers: {
    //       "Content-Type": "application/x-www-form-urlencoded",
    //     },
    //   })
    //     .then((response) => response.json())
    //     .then((data) => {
    //       document.getElementById(
    //         "prediction"
    //       ).textContent = `user_input: ${data.user_input}`;
    //     });
  });
