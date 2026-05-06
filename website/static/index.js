let date = new Date();
let socket = io();
socket.emit("join", "public_room");

// Listen for messages from server
socket.on("message", function(data) {
    recieve_message(data);
});

socket.on("user_join", function(data) {
    let messages = document.getElementById("msg_reel");
    messages.innerHTML += `
        <p class="text-sm my-2 px-2"><b>${data.user}</b> Joined the chat.</p>
    `;
});

socket.on("user_left", function(data) {
    let messages = document.getElementById("msg_reel");
    messages.innerHTML += `
        <p class="text-sm my-2 px-2"><b>${data.user}</b> Left the chat.</p>
    `;
});

// Recieve messages
function recieve_message(data) {
    let messages = document.getElementById("msg_reel");
    
    messages.innerHTML += `
        <div class="inline-block md:max-w-[80%]">
            <div class="mb-1">
                <a href="#" class="text-[17px] text-[${data.color}] font-medium lowercase">${data.user}</a>
            </div>

            <div class="px-2 mb-1">
                <p>${data.message}</p>
            </div>

            <div class="flex justify-end">
                <p class="text-[13px] text-[rgb(175,175,175)] font-light mt-[2px]">${date.getHours()}:${date.getMinutes()}</p>
            </div>
        </div>
    `
}

// Send messages
const msg_form = document.getElementById("msg_form");

msg_form.addEventListener("submit", (e) => {
    e.preventDefault;

    let msgInput = document.getElementById("msg_input");
    let message = msgInput.value;
    socket.send(message);
    msgInput.value = "";
});


