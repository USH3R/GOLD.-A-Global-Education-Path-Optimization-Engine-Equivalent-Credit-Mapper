document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("degree-form");
    const resultPre = document.getElementById("result");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const degree = document.getElementById("degree").value.trim();
        if (!degree) return;

        resultPre.textContent = "Loading...";

        try {
            const response = await fetch("/optimize", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: new URLSearchParams({ degree })
            });

            if (!response.ok) {
                throw new Error(`Server returned status ${response.status}`);
            }

            const data = await response.json();
            resultPre.textContent = JSON.stringify(data, null, 4);
        } catch (err) {
            console.error(err);
            resultPre.textContent = `An unexpected error occurred. Check console.\n${err}`;
        }
    });
});document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("degreeForm");
    const output = document.getElementById("jsonOutput");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const degreeInput = document.getElementById("degree").value;

        output.textContent = "Processing...";

        try {
            const response = await fetch("/optimize", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: `degree=${encodeURIComponent(degreeInput)}`
            });

            if (!response.ok) throw new Error(`Server error: ${response.status}`);

            const data = await response.json();
            output.textContent = JSON.stringify(data, null, 4);
        } catch (err) {
            output.textContent = `An unexpected error occurred: ${err}`;
        }
    });
});
