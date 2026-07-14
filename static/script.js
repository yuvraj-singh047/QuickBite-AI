// ==========================================
// QuickBite AI - script.js
// ==========================================

document.addEventListener("DOMContentLoaded", () => {

    // ----------------------------------------
    // Reveal ticket cards on load / on scroll
    // ----------------------------------------
    const cards = document.querySelectorAll(".ticket-card");

    const revealCard = (card, delay) => {
        setTimeout(() => {
            card.style.transition = "opacity .55s ease, transform .55s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, delay);
    };

    if ("IntersectionObserver" in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, i) => {
                if (entry.isIntersecting) {
                    revealCard(entry.target, i * 100);
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.15 });

        cards.forEach(card => observer.observe(card));
    } else {
        cards.forEach((card, index) => revealCard(card, index * 120));
    }

    // ----------------------------------------
    // Scroll to prediction receipt, if present
    // ----------------------------------------
    const result = document.querySelector(".receipt");

    if (result) {
        setTimeout(() => {
            result.scrollIntoView({
                behavior: "smooth",
                block: "center"
            });
        }, 350);
    }

});


// ================================
// Loading Button
// ================================

const form = document.querySelector("#etaForm");
const button = document.querySelector(".predict-btn");

if (form && button) {

    form.addEventListener("submit", () => {
        button.disabled = true;
        button.classList.add("is-loading");
        button.querySelector(".btn-label").textContent = "Calculating...";
    });

}


// ================================
// Highlight & shake invalid inputs
// ================================

const inputs = document.querySelectorAll("input, select");

inputs.forEach(input => {

    input.addEventListener("invalid", () => {
        input.classList.add("shake");
    });

    input.addEventListener("animationend", () => {
        input.classList.remove("shake");
    });

    input.addEventListener("input", () => {
        input.style.borderColor = "";
    });

});


// ================================
// Distance Validation
// ================================

const distance = document.querySelector('input[name="Distance"]');

if (distance) {

    distance.addEventListener("input", () => {

        if (parseFloat(distance.value) < 0) {
            distance.value = "";
        }

    });

}