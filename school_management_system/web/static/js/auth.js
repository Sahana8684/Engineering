// JavaScript for handling user authentication and user information display

document.addEventListener('DOMContentLoaded', function() {
    // Check if user is logged in
    checkUserLogin();
    
    // Initialize login form validation
    initLoginForm();
    
    // Initialize logout functionality
    initLogout();
});

/**
 * Check if user is logged in and update UI accordingly
 */
function checkUserLogin() {
    // Get user data from localStorage
    const userData = getUserData();
    
    // Update user dropdown if user is logged in
    if (userData) {
        updateUserDropdown(userData);
    }
}

/**
 * Get user data from localStorage
 * @returns {Object|null} User data object or null if not logged in
 */
function getUserData() {
    const userDataStr = localStorage.getItem('userData');
    if (userDataStr) {
        try {
            return JSON.parse(userDataStr);
        } catch (e) {
            console.error('Error parsing user data:', e);
            return null;
        }
    }
    return null;
}

/**
 * Update user dropdown with user information
 * @param {Object} userData - User data object
 */
function updateUserDropdown(userData) {
    // Update user dropdown toggle
    const userDropdownToggle = document.getElementById('userDropdown');
    if (userDropdownToggle) {
        userDropdownToggle.innerHTML = `<i class="fas fa-user-circle me-1"></i> ${userData.full_name || userData.email}`;
    }
    
    // Update user dropdown menu
    const userDropdownMenu = document.querySelector('[aria-labelledby="userDropdown"]');
    if (userDropdownMenu) {
        // Add user info at the top of the dropdown
        const userInfoItem = document.createElement('li');
        userInfoItem.className = 'dropdown-item-text';
        userInfoItem.innerHTML = `
            <div class="d-flex align-items-center mb-2">
                <div class="flex-shrink-0">
                    <img src="https://ui-avatars.com/api/?name=${encodeURIComponent(userData.full_name || 'User')}&background=0D8ABC&color=fff&size=32" 
                         class="rounded-circle" alt="User Avatar" width="32" height="32">
                </div>
                <div class="flex-grow-1 ms-2">
                    <div class="fw-bold">${userData.full_name || 'User'}</div>
                    <div class="small text-muted">${userData.email}</div>
                </div>
            </div>
            <div class="small text-muted mb-2">Role: ${userData.role || 'User'}</div>
        `;
        
        // Insert user info at the beginning of the dropdown
        userDropdownMenu.insertBefore(userInfoItem, userDropdownMenu.firstChild);
        
        // Add divider after user info
        const divider = document.createElement('li');
        divider.innerHTML = '<hr class="dropdown-divider">';
        userDropdownMenu.insertBefore(divider, userInfoItem.nextSibling);
    }
}

/**
 * Initialize login form validation and submission
 */
function initLoginForm() {
    const loginForm = document.querySelector('form[action="/login"]');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            // Let the form submit normally to the server
            // The server will handle authentication and redirect
            
            // We'll capture the user data after successful login in a separate function
            // that runs on the dashboard page
        });
    }
}

/**
 * Initialize logout functionality
 */
function initLogout() {
    const logoutLink = document.querySelector('a[href="/logout"]');
    if (logoutLink) {
        logoutLink.addEventListener('click', function(event) {
            // Clear user data from localStorage
            localStorage.removeItem('userData');
            
            // Let the default action happen (redirect to logout endpoint)
        });
    }
}

/**
 * Store user data in localStorage after successful login
 * This function is called from the dashboard page
 * @param {number} userId - User ID
 */
function storeUserData(userId) {
    // Fetch user data from API
    fetch(`/api/users/${userId}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch user data');
            }
            return response.json();
        })
        .then(userData => {
            // Store user data in localStorage
            localStorage.setItem('userData', JSON.stringify(userData));
            
            // Update user dropdown
            updateUserDropdown(userData);
        })
        .catch(error => {
            console.error('Error fetching user data:', error);
        });
}
