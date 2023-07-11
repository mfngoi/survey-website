
const resultBtn = document.querySelector("#result_btn");
const userSurveyBtn = document.querySelector("#user_survey_btn");

const h1 = document.querySelector("#title");
const title = h1.innerHTML;

resultBtn.addEventListener('click', () => {
    window.location.href = "http://127.0.0.1:5000/result/" + title;
});

userSurveyBtn.addEventListener('click', () => {
    window.location.href = "http://127.0.0.1:5000/user_survey/" + title;
})

