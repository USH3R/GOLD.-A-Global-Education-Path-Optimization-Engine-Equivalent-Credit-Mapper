document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("degreeForm");
    const resultsDiv = document.getElementById("results");

    form.addEventListener("submit", async function(e) {
        e.preventDefault();
        const degree = document.getElementById("degreeInput").value;
        const response = await fetch("/optimize", {
            method: "POST",
            headers: {"Content-Type": "application/x-www-form-urlencoded"},
            body: `degree=${degree}`
        });
        const data = await response.json();
        resultsDiv.innerHTML = `<pre>${JSON.stringify(data, null, 4)}</pre>`;
    });
});
