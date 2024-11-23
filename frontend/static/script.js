// function showResister() {
//     const regi = document.getElementById('regi');
//     const log = document.getElementById('log');
//     const wellcm = document.getElementById("well-pg");

//     regi.style.display = 'block';
//     wellcm.style.display = "none";
//     log.style.display = 'none';
// }

// function showlogin() {
//     const regi = document.getElementById('regi');
//     const log = document.getElementById('log');
//     const wellcm = document.getElementById("well-pg");

//     regi.style.display = 'none';
//     wellcm.style.display = "none";
//     log.style.display = 'block';

// }    

function aboutPGopen() {
    const aboutMain = document.getElementById("about-main")
    const welcomePG = document.getElementById("welcome-meg")
    const servicePG = document.getElementById("service-main")
    aboutMain.style.display = "block";
    welcomePG.style.display = "none";
    servicePG.style.display = "none";
}
function servicePGopen() {
    const aboutMain = document.getElementById("about-main")
    const welcomePG = document.getElementById("welcome-meg")
    const servicePG = document.getElementById("service-main")
    aboutMain.style.display = "none";
    welcomePG.style.display = "none";
    servicePG.style.display = "block";
    
}

function showwellpg() {
    const regi = document.getElementById('regi');
    const log = document.getElementById('log');
    const wellcm = document.getElementById("well-pg");

    regi.style.display = 'none';
    wellcm.style.display = "block";
    log.style.display = 'none';

}
function closeIndexMobiNav() {
    const indexmobinavbar = document.getElementById('index-mobi-nav-bar');
    indexmobinavbar.style.display = "none";
    console.log("hellooooooooooooo")
}
function openIndexMobiNav() {
    const indexmobinavbar = document.getElementById('index-mobi-nav-bar');
    indexmobinavbar.style.display = "flex";
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

function openMobiNav(){
    const mobiNav = document.getElementById("ser-nav-mob-bar")
    mobiNav.style.display = "block";
}
function closeMobiNav(){
    const mobiNav = document.getElementById("ser-nav-mob-bar")
    mobiNav.style.display = "none";
}





// ///////////////////chat 

// function openChat(name) {
//     // Update chat header with the selected user's name
//     document.getElementById('chatHeader').textContent = 'Chat with ' + name;

//     // Clear previous messages (for demo purposes)
//    document.getElementById('messageArea').innerHTML = ''; 
// }
function openChat() {
   const chatWindow = document.getElementById('chat-window')
   const sidebar = document.getElementById('sidebar')
   chatWindow.style.display = "flex"
   sidebar.style.display = "none"
}
function BackChatList() {
    const chatWindow = document.getElementById('chat-window')
    const sidebar = document.getElementById('sidebar')
    chatWindow.style.display = "none"
    sidebar.style.display = "flex"
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

// document.getElementById('messageInput').addEventListener('keydown', function (event) {
//     if (event.key === 'Enter') {
//         sendMessage();
//     }
// });

function closeChat() {
    const chatbox = document.getElementById('connection-list');
    chatbox.style.display = 'none';
}

function showChat() {
    document.getElementById('connection-list').style.display = 'block';
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








//  Profile Settings
function closeSettings() {
    const proSetting = document.getElementById('pro-setting');
    proSetting.style.display = 'none';
}

function openProSetting() {
    const proSetting = document.getElementById('pro-setting');
    proSetting.style.display = 'block';
    const mobiNav = document.getElementById("ser-nav-mob-bar")
    mobiNav.style.display = "none";
}



function closeupdate() {
    const upclose = document.getElementById('statusModal');
    upclose.style.display = 'none';
}

function openupdate() {
    const upclose = document.getElementById('statusModal');
    upclose.style.display = 'flex';
}

function showuBabyUpdate() {
    const showuBabyUpdate = document.getElementById('babysatatus');
    const closeDash = document.getElementById('activity-con');
    closeDash.style.display = 'none';
    showuBabyUpdate.style.display = 'flex';
    const mobiNav = document.getElementById("ser-nav-mob-bar")
    mobiNav.style.display = "none";
}

function showuDash() {
    const showuBabyUpdate = document.getElementById('babysatatus');
    const closeDash = document.getElementById('activity-con');
    closeDash.style.display = 'flex';
    showuBabyUpdate.style.display = 'none';

    const mobiNav = document.getElementById("ser-nav-mob-bar")
    mobiNav.style.display = "none";
}

// function createPostBox() {
//     const feed = document.getElementById("tasker-feeds");
//     const postBox = document.createElement("div")
//     const postImg = document.createElement("img")
//     const postTitle = document.createElement("p")
//     const postLoc = document.createElement("h4")
//     const postpri = document.createElement("h3")
//     const postBtn = document.createElement("button")

//     postBox.setAttribute("class","post-box")
//     postImg.setAttribute("src","/frontend/static/Assets/cooking.jpg")

//     postTitle.textContent = "I can Cook Well"
//     postLoc.textContent = "guindy"
//     postpri.textContent = "7000"
//     postBtn.textContent = "Grow To Gether"

//     feed.appendChild(postBox)
//     postBox.appendChild(postImg,postTitle,postLoc,postpri,postBtn)
// }

function openbabystatus() {
    const babystatus = document.getElementById("babystatus")
    babystatus.style.display = "block";
}
function closeConnection() {
    const connectionlist = document.getElementById("connection-status-list")
    connectionlist.style.display = "none";
}

function openConnection() {
    const connectionlist = document.getElementById("connection-status-list")
    connectionlist.style.display = "flex";
    closeMobiNav()
}
function showAthu() {
    const athuPop  = document.getElementById("auth-pop")
    athuPop.style.display = "block";
}
function closdeAthu() {
    const athuPop  = document.getElementById("auth-pop")
    athuPop.style.display = "none";
}

function closereqt() {
    const connectionreqt = document.getElementById("connection-reqst-list")
    connectionreqt.style.display = "none";
}

function openreqt() {
    const connectionlist = document.getElementById("connection-reqst-list")
    connectionlist.style.display = "flex";
    const mobiNav = document.getElementById("ser-nav-mob-bar")
    mobiNav.style.display = "none";
}

function reqtReject(eleID) {
    const connectionReqst = document.getElementById(eleID)
    connectionReqst.style.display = "none"
}

function reqtaccpt(idBtn, idChat) {
    const reqstButton = document.getElementById(idBtn)
    const ReqtChat = document.getElementById(idChat)
    reqstButton.style.display = "none"
    ReqtChat.style.display = "flex"
}

function closeNoti() {
    const taskerNoti = document.getElementById("tasker-noti")
    taskerNoti.style.display = "none"
}

function openNoti() {
    const taskerNoti = document.getElementById("tasker-noti")
    taskerNoti.style.display = "block"
}

function opentaskeInfo() {
    const taskerinfo = document.getElementById("tasker-pro-info")
    taskerinfo.style.display = "flex"
}

function closeProInfo() {
    const taskerinfo = document.getElementById("tasker-pro-info")
    taskerinfo.style.display = "none"
}
function backPreviousPg() {
    const previousPageUrl = document.referrer;
    const babackPreviousPg = document.getElementById("back-previous-pg")
    babackPreviousPg.href = previousPageUrl;
}
