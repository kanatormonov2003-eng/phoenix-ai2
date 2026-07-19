const chatButton = document.querySelector(".ai-chat-button");

const chatWindow = document.querySelector(".ai-chat-window");

const sendButton = document.querySelector(".chat-input button");

const input = document.querySelector(".chat-input input");

const chatBody = document.querySelector(".chat-body");




// Открытие / закрытие чата

chatButton.addEventListener("click", function(){


    if(chatWindow.style.display === "flex"){

        chatWindow.style.display = "none";

    }

    else {

        chatWindow.style.display = "flex";

    }


});




// Отправка сообщения


sendButton.addEventListener("click", sendMessage);



input.addEventListener("keydown", function(event){


    if(event.key === "Enter"){

        sendMessage();

    }


});






async function sendMessage(){


    let message = input.value.trim();



    if(message === ""){

        return;

    }



    // сообщение пользователя


    chatBody.innerHTML += `

    <p style="color:white; margin-top:15px;">
    
    👤 ${message}

    </p>

    `;



    input.value = "";



    // индикатор загрузки


    chatBody.innerHTML += `

    <p id="loading" style="margin-top:15px;">

    🤖 Печатает...

    </p>

    `;



    chatBody.scrollTop = chatBody.scrollHeight;




    try {


        const response = await fetch(
            "https://phoenix-ai-api.onrender.com/chat",
            {

                method: "POST",


                headers: {

                    "Content-Type": "application/json"

                },


                body: JSON.stringify({

                    message: message

                })


            }

        );



        const data = await response.json();



        document.getElementById("loading").remove();



        chatBody.innerHTML += `

        <p style="margin-top:15px;">

        🤖 ${data.answer}

        </p>

        `;



    }


    catch(error){



        document.getElementById("loading").remove();



        chatBody.innerHTML += `

        <p style="margin-top:15px;">

        ❌ Не удалось подключиться к Phoenix AI

        </p>

        `;



        console.log(error);



    }



    chatBody.scrollTop = chatBody.scrollHeight;



}