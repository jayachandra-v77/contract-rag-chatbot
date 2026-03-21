async function sendMessage() {
    const input = document.getElementById("question");
    const question = input.value.trim();

    if (!question) return;

    // Show user message
    addMessage(question, "user");
    input.value = "";

    // Show loading
    const loadingMsg = addMessage("Loading...", "bot");

    try {
        const response = await fetch("http://127.0.0.1:8000/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question: question })
        });

        const data = await response.json();

        // Replace loading text
        loadingMsg.innerText = data.answer;

    } catch (error) {
        loadingMsg.innerText = "Error connecting to server!";
    }
}

// Add message to UI
function addMessage(text, sender) {
    const chat = document.getElementById("chat");

    const msg = document.createElement("div");
    msg.classList.add("message");

    if (sender === "user") {
        msg.classList.add("user");
    } else {
        msg.classList.add("bot");
    }

    msg.innerText = text;
    chat.appendChild(msg);

    chat.scrollTop = chat.scrollHeight;

    return msg;
}

// Enter key support
function handleEnter(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}