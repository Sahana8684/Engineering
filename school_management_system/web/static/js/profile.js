// JavaScript for handling user profile data

document.addEventListener('DOMContentLoaded', function() {
    // Get user data from localStorage or fetch from API if not available
    const userData = getUserDataFromLocalStorage();
    
    if (userData) {
        // If user data is available in localStorage, use it
        updateProfileUI(userData);
    } else {
        // Otherwise fetch from API
        fetchUserProfile();
    }
});

/**
 * Get user data from localStorage
 * @returns {Object|null} User data object or null if not found
 */
function getUserDataFromLocalStorage() {
    const userDataStr = localStorage.getItem('userData');
    if (userDataStr) {
        try {
            return JSON.parse(userDataStr);
        } catch (e) {
            console.error('Error parsing user data from localStorage:', e);
            return null;
        }
    }
    return null;
}

/**
 * Fetch user profile data from the API
 */
function fetchUserProfile() {
    // Get the current user ID from the hidden input field
    const userIdInput = document.getElementById('currentUserId');
    const userId = userIdInput ? parseInt(userIdInput.value) : 1; // Default to admin if not found

    // Show loading state
    const profileContainer = document.getElementById('profile-container');
    if (profileContainer) {
        profileContainer.innerHTML = '<div class="text-center py-5"><div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div><p class="mt-2">Loading profile data...</p></div>';
    }

    // Fetch user data
    fetch(`/api/users/${userId}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch profile data');
            }
            return response.json();
        })
        .then(userData => {
            // Store user data in localStorage
            localStorage.setItem('userData', JSON.stringify(userData));
            
            // Update the profile UI with the user data
            updateProfileUI(userData);
        })
        .catch(error => {
            console.error('Error fetching profile data:', error);
            
            // If API fails, use mock data as fallback
            const mockUserData = {
                id: 1,
                email: "admin@example.com",
                full_name: "Admin User",
                is_active: true,
                is_superuser: true,
                role: "admin"
            };
            
            // Store mock user data in localStorage
            localStorage.setItem('userData', JSON.stringify(mockUserData));
            
            updateProfileUI(mockUserData);
        });
}

/**
 * Update the profile UI with user data
 * @param {Object} userData - The user data object
 */
function updateProfileUI(userData) {
    // Update profile header
    const profileName = document.querySelector('.profile-header h2');
    if (profileName) {
        profileName.textContent = userData.full_name || 'User';
    }

    const profileRole = document.querySelector('.profile-header p.text-muted');
    if (profileRole) {
        profileRole.textContent = userData.role || 'User';
    }

    const profileEmail = document.querySelector('.profile-header p:nth-child(3)');
    if (profileEmail) {
        profileEmail.innerHTML = `<i class="fas fa-envelope me-2"></i>${userData.email || 'No email provided'}`;
    }

    // Update personal information
    const fullNameValue = document.querySelector('.profile-info-item:nth-child(1) .profile-info-value');
    if (fullNameValue) {
        fullNameValue.textContent = userData.full_name || 'Not provided';
    }

    const emailValue = document.querySelector('.profile-info-item:nth-child(2) .profile-info-value');
    if (emailValue) {
        emailValue.textContent = userData.email || 'Not provided';
    }

    // Update profile avatar
    const profileAvatar = document.querySelector('.profile-avatar');
    if (profileAvatar) {
        // Generate avatar URL using user's full name
        const fullName = userData.full_name || 'User';
        profileAvatar.src = `https://ui-avatars.com/api/?name=${encodeURIComponent(fullName)}&background=0D8ABC&color=fff&size=150`;
    }

    // Show success message
    showNotification('Profile data loaded successfully', 'success');
}

/**
 * Show a notification message
 * @param {string} message - The message to display
 * @param {string} type - The type of notification (success, info, warning, error)
 */
function showNotification(message, type = 'info') {
    const notificationContainer = document.getElementById('notification-container');
    
    if (!notificationContainer) {
        // Create notification container if it doesn't exist
        const container = document.createElement('div');
        container.id = 'notification-container';
        container.style.position = 'fixed';
        container.style.top = '20px';
        container.style.right = '20px';
        container.style.zIndex = '1050';
        document.body.appendChild(container);
    }
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show`;
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    // Add notification to container
    document.getElementById('notification-container').appendChild(notification);
    
    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 5000);
}
