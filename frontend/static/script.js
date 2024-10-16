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