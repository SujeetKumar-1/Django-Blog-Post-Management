/* Country Filter Logic */

document.addEventListener("DOMContentLoaded", function () {
    const applyFilterButton = document.getElementById("apply-f");
    const showAllButton = document.getElementById("show_all");
    const countrySelect = document.getElementById("countryFilterToggle");
    const posts = document.querySelectorAll(".post-card"); 

    // Apply filter based on selected country
    applyFilterButton.addEventListener("click", function () {
        const selectedCountry = countrySelect.options[countrySelect.selectedIndex].text.trim();

        // Loop through all posts and toggle visibility based on the selected country
        posts.forEach(post => {
            const postCountry = post.getAttribute("data-country"); 
            if (postCountry === selectedCountry || selectedCountry === "Select Country") {
                post.style.display = "block";
            } else {
                post.style.display = "none";
            }
        });
    });

    // Show all posts when "Show All Posts" is clicked
    showAllButton.addEventListener("click", function () {
        posts.forEach(post => {
            post.style.display = "block";
        });
    });
});
