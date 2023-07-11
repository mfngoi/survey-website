
const analysisBtn = document.querySelector("#analysis_btn");

const h1 = document.querySelector("#title");
const title = h1.innerHTML;

analysisBtn.addEventListener('click', () => {
    window.location.href = "http://127.0.0.1:5000/analysis/" + title;
});