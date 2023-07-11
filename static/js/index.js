
surveyButton = document.querySelector("#generateSurvey");
surveyList = document.querySelector("#surveylist");

surveyButton.addEventListener("click", () => {
    window.location.href = "http://127.0.0.1:5000/generate"

});

//build the surveylist and display it

fetch("http://127.0.0.1:5000/surveyList")
.then((response) => {return response.json()})
.then((result) => {
    console.log(result);

    const ul = document.createElement("ul")  
    
    result.forEach(element => {
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.href = '/jinja_temp/' + element.title;
        a.textContent = element.title;

        li.appendChild(a);
        ul.appendChild(li);
    });



    surveyList.innerHTML = "";
    surveyList.appendChild(ul);


})