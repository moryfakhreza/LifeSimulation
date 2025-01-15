document.addEventListener('DOMContentLoaded', () => {
    const createCharacterForm = document.getElementById('create-character-form');
    const gameActions = document.getElementById('game-actions');
    const statusEl = document.getElementById('status');
    const notifications = document.getElementById('notifications');

    createCharacterForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(createCharacterForm);
        
        fetch('/create_character', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === "Character created") {
                gameActions.style.display = 'block';
                updateStatus(data.character);
                showNotification(data.status);
            }
        });
    });

    window.ageUp = function() {
        fetch('/age_up', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            updateStatus(data.character);
            showNotification(data.status);
        });
    };

    window.randomEvent = function() {
        fetch('/random_event', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            updateStatus(data.character);
            showNotification(data.status);
        });
    };

    window.education = function() {
        fetch('/education', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            updateStatus(data.character);
            showNotification(data.status);
        });
    };

    window.career = function() {
        fetch('/career', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            updateStatus(data.character);
            showNotification(data.status);
        });
    };

    window.addRelationship = function() {
        const relation_name = prompt("Enter the name of the family member:");
        const relation_type = prompt("Enter the type of relationship (e.g., Parent, Sibling):");
        const formData = new FormData();
        formData.append('relation_name', relation_name);
        formData.append('relation_type', relation_type);

        fetch('/relationships', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            updateStatus(data.character);
            showNotification(data.status);
        });
    };

    window.commitCrime = function() {
        fetch('/crime', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            updateStatus(data.character);
            showNotification(data.status);
        });
    };

    window.manageAssets = function() {
        const action = prompt("Choose asset action (buy/sell):");
        const asset_name = prompt("Enter the name of the asset:");
        const value = prompt("Enter the value of the asset:");
        const formData = new FormData();
        formData.append('action', action);
        formData.append('asset_name', asset_name);
        formData.append('value', value);

        fetch('/assets', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            updateStatus(data.character);
            showNotification(data.status);
        });
    };

    window.health = function() {
        const action = prompt("Choose health action (visit_doctor/plastic_surgery):");
        const formData = new FormData();
        formData.append('action', action);

        fetch('/health', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            updateStatus(data.character);
            showNotification(data.status);
        });
    };

    function updateStatus(character) {
        statusEl.textContent = JSON.stringify(character, null, 2);
    }

    function showNotification(message) {
        notifications.textContent = message;
        notifications.style.display = 'block';
        setTimeout(() => {
            notifications.style.display = 'none';
        }, 3000);
    }
});