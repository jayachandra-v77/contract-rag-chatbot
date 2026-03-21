async function sendMessage() {
    const input = document.getElementById("question");
    const chat = document.getElementById("chat");

    const question = input.value.trim();
    if (!question) return;

    // Show user message
    const userMsg = document.createElement("div");
    userMsg.className = "message user";
    userMsg.innerText = question;
    chat.appendChild(userMsg);

    input.value = "";

    // Scroll down
    chat.scrollTop = chat.scrollHeight;

    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question: question })
        });

        const data = await response.json();

        // Show bot message
        const botMsg = document.createElement("div");
        botMsg.className = "message bot";
        botMsg.innerText = data.answer;
        chat.appendChild(botMsg);

        chat.scrollTop = chat.scrollHeight;

    } catch (error) {
        console.error(error);
    }
}