function predict() {
    const data = {
        age: parseInt(document.getElementById("age").value),
        sex: document.getElementById("sex").value,
        chest_pain: document.getElementById("chest_pain").value,
        resting_bp: parseInt(document.getElementById("resting_bp").value),
        cholesterol: parseInt(document.getElementById("cholesterol").value),
        fasting_bs: parseInt(document.getElementById("fasting_bs").value),
        resting_ecg: document.getElementById("resting_ecg").value,
        max_hr: parseInt(document.getElementById("max_hr").value),
        exercise_angina: document.getElementById("exercise_angina").value,
        oldpeak: parseFloat(document.getElementById("oldpeak").value),
        st_slope: document.getElementById("st_slope").value
    };

    fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText = data.result;
    });
}
