document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("degree-form");
    const output = document.getElementById("output");

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const degree = document.getElementById("degree").value;

        try {
            const response = await fetch("/optimize", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: `degree=${encodeURIComponent(degree)}`
            });

            if (!response.ok) throw new Error(`HTTP error ${response.status}`);

            const data = await response.json();
            output.textContent = JSON.stringify(data, null, 4);
        } catch (error) {
            output.textContent = `Error: ${error.message}`;
        }
    });
});
