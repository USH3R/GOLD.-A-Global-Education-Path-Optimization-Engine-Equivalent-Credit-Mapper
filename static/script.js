document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("degreeForm");
    const resultsDiv = document.getElementById("results");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const degreeInput = document.getElementById("degree").value.trim();
        if (!degreeInput) {
            resultsDiv.innerHTML = "<p style='color:red;'>Please enter a degree.</p>";
            return;
        }

        resultsDiv.innerHTML = "<p>Fetching optimized path...</p>";

        try {
            const formData = new FormData();
            formData.append("degree", degreeInput);

            const response = await fetch("/optimize", {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                const errorData = await response.json();
                resultsDiv.innerHTML = `<p style='color:red;'>Error: ${errorData.error}</p>`;
                return;
            }

            const data = await response.json();

            // Pretty-print JSON results
            resultsDiv.innerHTML = `<pre>${JSON.stringify(data, null, 4)}</pre>`;
        } catch (error) {
            console.error(error);
            resultsDiv.innerHTML = "<p style='color:red;'>An unexpected error occurred. Check console.</p>";
        }
    });
});
