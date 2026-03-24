document.addEventListener("DOMContentLoaded", () => {
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
