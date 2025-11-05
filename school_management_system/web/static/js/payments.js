// JavaScript for handling payments functionality

document.addEventListener('DOMContentLoaded', function() {
    // Initialize payment form validation
    initPaymentFormValidation();
    
    // Initialize payment buttons
    initPaymentButtons();
    
    // Initialize payment method selection
    initPaymentMethodSelection();
});

/**
 * Initialize payment form validation
 */
function initPaymentFormValidation() {
    const paymentForm = document.getElementById('paymentForm');
    if (paymentForm) {
        paymentForm.addEventListener('submit', function(event) {
            event.preventDefault();
            
            // Validate form
            if (validatePaymentForm()) {
                // Show payment processing
                showPaymentProcessing();
                
                // Simulate payment processing
                setTimeout(function() {
                    // Show success message
                    showPaymentSuccess();
                    
                    // Reset form
                    paymentForm.reset();
                    
                    // Close modal
                    const modal = bootstrap.Modal.getInstance(document.getElementById('makePaymentModal'));
                    if (modal) {
                        modal.hide();
                    }
                }, 2000);
            }
        });
    }
}

/**
 * Validate payment form
 * @returns {boolean} True if form is valid, false otherwise
 */
function validatePaymentForm() {
    const studentId = document.getElementById('studentId');
    const feeType = document.getElementById('feeType');
    const amount = document.getElementById('amount');
    const paymentMethod = document.getElementById('paymentMethod');
    
    let isValid = true;
    
    // Reset error messages
    document.querySelectorAll('.invalid-feedback').forEach(el => el.style.display = 'none');
    document.querySelectorAll('.is-invalid').forEach(el => el.classList.remove('is-invalid'));
    
    // Validate student ID
    if (!studentId.value) {
        document.getElementById('studentIdFeedback').style.display = 'block';
        studentId.classList.add('is-invalid');
        isValid = false;
    }
    
    // Validate fee type
    if (!feeType.value) {
        document.getElementById('feeTypeFeedback').style.display = 'block';
        feeType.classList.add('is-invalid');
        isValid = false;
    }
    
    // Validate amount
    if (!amount.value || parseFloat(amount.value) <= 0) {
        document.getElementById('amountFeedback').style.display = 'block';
        amount.classList.add('is-invalid');
        isValid = false;
    }
    
    // Validate payment method
    if (!paymentMethod.value) {
        document.getElementById('paymentMethodFeedback').style.display = 'block';
        paymentMethod.classList.add('is-invalid');
        isValid = false;
    }
    
    return isValid;
}

/**
 * Initialize payment buttons
 */
function initPaymentButtons() {
    // Add event listeners to "Pay Now" buttons
    document.querySelectorAll('.btn-pay-now').forEach(button => {
        button.addEventListener('click', function() {
            const studentId = this.getAttribute('data-student-id');
            const studentName = this.getAttribute('data-student-name');
            const amount = this.getAttribute('data-amount');
            const feeType = this.getAttribute('data-fee-type');
            
            // Populate payment modal
            populatePaymentModal(studentId, studentName, amount, feeType);
            
            // Show payment modal
            const paymentModal = new bootstrap.Modal(document.getElementById('makePaymentModal'));
            paymentModal.show();
        });
    });
    
    // Add event listeners to "Record Payment" buttons
    document.querySelectorAll('.btn-record-payment').forEach(button => {
        button.addEventListener('click', function() {
            const studentId = this.getAttribute('data-student-id');
            const studentName = this.getAttribute('data-student-name');
            
            // Populate record payment modal
            populateRecordPaymentModal(studentId, studentName);
            
            // Show record payment modal
            const recordPaymentModal = new bootstrap.Modal(document.getElementById('addPaymentModal'));
            recordPaymentModal.show();
        });
    });
}

/**
 * Populate payment modal with student details
 * @param {string} studentId - Student ID
 * @param {string} studentName - Student name
 * @param {string} amount - Payment amount
 * @param {string} feeType - Fee type
 */
function populatePaymentModal(studentId, studentName, amount, feeType) {
    document.getElementById('paymentStudentId').value = studentId;
    document.getElementById('paymentStudentName').value = studentName;
    document.getElementById('paymentAmount').value = amount;
    document.getElementById('paymentFeeType').value = feeType;
}

/**
 * Populate record payment modal with student details
 * @param {string} studentId - Student ID
 * @param {string} studentName - Student name
 */
function populateRecordPaymentModal(studentId, studentName) {
    const studentSelect = document.getElementById('studentId');
    if (studentSelect) {
        for (let i = 0; i < studentSelect.options.length; i++) {
            if (studentSelect.options[i].value === studentId) {
                studentSelect.selectedIndex = i;
                break;
            }
        }
    }
}

/**
 * Initialize payment method selection
 */
function initPaymentMethodSelection() {
    const paymentMethod = document.getElementById('paymentMethod');
    const cardDetailsContainer = document.getElementById('cardDetailsContainer');
    const upiDetailsContainer = document.getElementById('upiDetailsContainer');
    const bankDetailsContainer = document.getElementById('bankDetailsContainer');
    
    if (paymentMethod && cardDetailsContainer && upiDetailsContainer && bankDetailsContainer) {
        paymentMethod.addEventListener('change', function() {
            // Hide all payment details containers
            cardDetailsContainer.style.display = 'none';
            upiDetailsContainer.style.display = 'none';
            bankDetailsContainer.style.display = 'none';
            
            // Show selected payment details container
            switch (paymentMethod.value) {
                case 'credit_card':
                case 'debit_card':
                    cardDetailsContainer.style.display = 'block';
                    break;
                case 'upi':
                    upiDetailsContainer.style.display = 'block';
                    break;
                case 'bank_transfer':
                    bankDetailsContainer.style.display = 'block';
                    break;
            }
        });
    }
}

/**
 * Show payment processing UI
 */
function showPaymentProcessing() {
    const payButton = document.getElementById('payButton');
    if (payButton) {
        payButton.disabled = true;
        payButton.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Processing...';
    }
}

/**
 * Show payment success message
 */
function showPaymentSuccess() {
    // Create toast element
    const toastContainer = document.getElementById('toastContainer');
    if (!toastContainer) {
        const container = document.createElement('div');
        container.id = 'toastContainer';
        container.className = 'toast-container position-fixed bottom-0 end-0 p-3';
        document.body.appendChild(container);
    }
    
    // Create toast
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'assertive');
    toast.setAttribute('aria-atomic', 'true');
    
    toast.innerHTML = `
        <div class="toast-header bg-success text-white">
            <strong class="me-auto">Payment Successful</strong>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">
            Your payment has been processed successfully. A receipt has been sent to your email.
        </div>
    `;
    
    // Add toast to container
    document.getElementById('toastContainer').appendChild(toast);
    
    // Show toast
    const bsToast = new bootstrap.Toast(toast);
    bsToast.show();
    
    // Reset pay button
    const payButton = document.getElementById('payButton');
    if (payButton) {
        payButton.disabled = false;
        payButton.innerHTML = 'Pay Now';
    }
    
    // Reload page after a delay
    setTimeout(function() {
        location.reload();
    }, 3000);
}

/**
 * Format currency
 * @param {number} amount - Amount to format
 * @param {string} currency - Currency code
 * @returns {string} Formatted currency
 */
function formatCurrency(amount, currency = 'INR') {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: currency,
        maximumFractionDigits: 0
    }).format(amount);
}
