document.addEventListener('DOMContentLoaded', () => {
    const sendButton = document.getElementById('sendButton') as HTMLButtonElement;
    const userInput = document.getElementById('userInput') as HTMLInputElement;
    const messages = document.getElementById('messages') as HTMLDivElement;

    sendButton.addEventListener('click', () => {
        const userMessage = userInput.value;
        if (userMessage.trim() !== '') {
            addMessage(userMessage, 'user-message');
            userInput.value = '';
            // Simulate bot response
            setTimeout(() => {
                const botMessage = `Bot response to: ${userMessage}`;
                addMessage(botMessage, 'bot-message');
            }, 1000);
        }
    });

    function addMessage(text: string, className: string) {
        const messageElement = document.createElement('div');
        messageElement.textContent = text;
        messageElement.className = `message ${className}`;
        messages.appendChild(messageElement);
        messages.scrollTop = messages.scrollHeight;
    }
});