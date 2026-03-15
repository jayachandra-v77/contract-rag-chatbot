async function send(){

let input = document.getElementById("question")
let chatBox = document.getElementById("chatBox")

let question = input.value

if(question.trim() === "") return

// show user message
let userMsg = document.createElement("div")
userMsg.className = "message user"
userMsg.innerText = question
chatBox.appendChild(userMsg)

input.value = ""

// call API
let res = await fetch("/ask",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
question:question
})
})

let data = await res.json()

// show bot message
let botMsg = document.createElement("div")
botMsg.className = "message bot"
botMsg.innerText = data.answer

chatBox.appendChild(botMsg)

chatBox.scrollTop = chatBox.scrollHeight

}

function handleKey(event){
if(event.key === "Enter"){
send()
}
}