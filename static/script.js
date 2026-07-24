// ================================
// Phishing Email Analyzer
// script.js
// ================================

const textarea = document.getElementById("email_content");
const analyzeBtn = document.getElementById("analyzeBtn");
const charCount = document.getElementById("charCount");

// ================================
// Character Counter
// ================================

if (textarea && charCount) {

    function updateCounter() {

        charCount.textContent = textarea.value.length;

    }

    textarea.addEventListener("input", updateCounter);

    updateCounter();

}

// ================================
// Auto Resize Textarea
// ================================

if (textarea) {

    textarea.addEventListener("input", function () {

        this.style.height = "auto";
        this.style.height = this.scrollHeight + "px";

    });

}

// ================================
// Analyze Button Loading
// ================================

if (analyzeBtn && textarea) {

    analyzeBtn.addEventListener("click", function (e) {

        if (textarea.value.trim() === "") {

            e.preventDefault();

            alert("Please paste an email before analyzing.");

            return;

        }

        analyzeBtn.disabled = true;

        analyzeBtn.innerHTML = "⏳ Analyzing...";

    });

}

// ================================
// Ctrl + Enter Shortcut
// ================================

if (textarea) {

    textarea.addEventListener("keydown", function (e) {

        if (e.ctrlKey && e.key === "Enter") {

            e.preventDefault();

            document.querySelector("form").submit();

        }

    });

}

// ================================
// Restore Button if User Goes Back
// ================================

window.addEventListener("pageshow", function () {

    if (analyzeBtn) {

        analyzeBtn.disabled = false;

        analyzeBtn.innerHTML = "🔍 Analyze Email";

    }

});