function showResister() {
    const regi = document.getElementById('regi');
    const log = document.getElementById('log');
    const wellcm = document.getElementById("well-pg");
    
    regi.style.display = 'block';
    wellcm.style.display = "none";
    log.style.display = 'none';
}

function showlogin() {
    const regi = document.getElementById('regi');
    const log = document.getElementById('log');
    const wellcm = document.getElementById("well-pg");

    regi.style.display = 'none';
    wellcm.style.display = "none";
    log.style.display = 'block';

}

function showwellpg() {
    const regi = document.getElementById('regi');
    const log = document.getElementById('log');
    const wellcm = document.getElementById("well-pg");

    regi.style.display = 'none';
    wellcm.style.display = "block";
    log.style.display = 'none';

}


function showSkillsInput() {
    const roleSelect = document.getElementById('role');
    const skillsContainer = document.getElementById('skillsContainer');

    // Show skills input if "Working Woman" is selected
    if (roleSelect.value === "Housewife") {
        skillsContainer.style.display = 'block';
    } else {
        skillsContainer.style.display = 'none';
    }
}
// document.getElementById("show-password").addEventListener("click", showPassword);

function showPassword() {
    const passField = document.getElementById("Upsw");

    // Toggle the type between "password" and "text"
    if (passField.type === "password") {
        passField.type = "name"; // Show password
    } else {
        passField.type = "password"; // Hide password
    }
}

function closeSkil() {
    const skillsbox = document.getElementById('skillsContainer');
    skillsbox.style.display = 'none';
}



       // Mark Task as Completed
       function markCompleted(button) {
        const task = button.parentElement;
        task.classList.add('task-completed');
        button.disabled = true;
        button.textContent = 'Completed';
        showToast('Task marked as completed!');
    }

    // Dismiss Notification
    function dismissNotification(button) {
        const notification = button.parentElement;
        notification.remove();
        showToast('Notification dismissed!');
    }






    // ///////////////////chat 

    function openChat(name) {
        // Update chat header with the selected user's name
        document.getElementById('chatHeader').textContent = 'Chat with ' + name;
  
        // Clear previous messages (for demo purposes)
        document.getElementById('messageArea').innerHTML = '';
      }
  
      function sendMessage() {
        const messageArea = document.getElementById('messageArea');
        const messageInput = document.getElementById('messageInput');
        const messageText = messageInput.value.trim();
  
        if (messageText !== "") {
          const messageDiv = document.createElement('div');
          messageDiv.classList.add('message', 'sent');
          messageDiv.innerHTML = `<p>${messageText}</p><span class="timestamp">${new Date().toLocaleTimeString()}</span>`;
  
          messageArea.appendChild(messageDiv);
          messageArea.scrollTop = messageArea.scrollHeight;
          messageInput.value = "";
        }
      }
  
      document.getElementById('messageInput').addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
          sendMessage();
        }
      });

      function closeChat() {
        const chatbox = document.getElementById('chat');
        chatbox.style.display = 'none';
      }


      function showChat() {
        document.getElementById('chat').style.display = 'flex';
    }





     // Open Service Modal
     function openServiceModal() {
        const modal = document.getElementById('serviceModal');
        modal.style.display = 'flex';
    }

    // Close Service Modal
    function closeServiceModal() {
        const modal = document.getElementById('serviceModal');
        modal.style.display = 'none';
    }

    // Close Modal when clicking outside the content
    window.onclick = function (event) {
        const modal = document.getElementById('serviceModal');
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    };

    // Submit Service Handler
    function submitService(event) {
        event.preventDefault(); // Prevent page reload
        const title = document.getElementById('serviceTitle').value;
        const description = document.getElementById('serviceDescription').value;
        const skills = document.getElementById('skills').value;
        const availability = document.getElementById('availability').value;
        const price = document.getElementById('servicePrice').value;
        const location = document.getElementById('serviceLocation').value;
        const image = document.getElementById('serviceImage').files[0];

        if (!image) {
            alert('Please upload an image!');
            return;
        }

        alert(`Service "${title}" has been offered successfully!`);
        document.getElementById('serviceModal').style.display = 'none';
    }








        // Save Profile Settings
        function saveSettings(event) {
            event.preventDefault(); // Prevent page reload

            const name = document.getElementById('userName').value;
            const email = document.getElementById('userEmail').value;
            const location = document.getElementById('userLocation').value;

            alert(`Profile updated successfully!\nName: ${name}\nEmail: ${email}\nLocation: ${location}`);

            // Add logic to save the changes (e.g., send to the server)
        }

        // Close Profile Settings (if part of a modal or page navigation)
        function closeSettings() {
            const proSetting = document.getElementById('pro-setting');
            proSetting.style.display = 'none';
        }
        function openProSetting() {
            const proSetting = document.getElementById('pro-setting');
            proSetting.style.display = 'block';
        }


