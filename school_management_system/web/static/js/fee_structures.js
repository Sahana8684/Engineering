// JavaScript for handling fee structures functionality

document.addEventListener('DOMContentLoaded', function() {
    // Initialize fee structure form validation
    initFeeStructureFormValidation();
    
    // Initialize fee structure filters
    initFeeStructureFilters();
    
    // Initialize fee payment buttons
    initFeePaymentButtons();
    
    // Initialize fee component management
    initFeeComponentManagement();
    
    // Initialize payment schedule management
    initPaymentScheduleManagement();
});

/**
 * Initialize fee structure form validation
 */
function initFeeStructureFormValidation() {
    const feeStructureForm = document.getElementById('feeStructureForm');
    if (feeStructureForm) {
        feeStructureForm.addEventListener('submit', function(event) {
            event.preventDefault();
            
            // Validate form
            if (validateFeeStructureForm()) {
                // Show processing
                showProcessing();
                
                // Simulate processing
                setTimeout(function() {
                    // Show success message
                    showSuccess('Fee structure created successfully!');
                    
                    // Reset form
                    feeStructureForm.reset();
                    
                    // Close modal
                    const modal = bootstrap.Modal.getInstance(document.getElementById('addFeeStructureModal'));
                    if (modal) {
                        modal.hide();
                    }
                    
                    // Reload page after a delay
                    setTimeout(function() {
                        location.reload();
                    }, 2000);
                }, 1500);
            }
        });
    }
}

/**
 * Validate fee structure form
 * @returns {boolean} True if form is valid, false otherwise
 */
function validateFeeStructureForm() {
    const structureName = document.getElementById('structureName');
    const academicYear = document.getElementById('academicYear');
    const branch = document.getElementById('branch');
    
    let isValid = true;
    
    // Reset error messages
    document.querySelectorAll('.invalid-feedback').forEach(el => el.style.display = 'none');
    document.querySelectorAll('.is-invalid').forEach(el => el.classList.remove('is-invalid'));
    
    // Validate structure name
    if (!structureName.value) {
        document.getElementById('structureNameFeedback').style.display = 'block';
        structureName.classList.add('is-invalid');
        isValid = false;
    }
    
    // Validate academic year
    if (!academicYear.value) {
        document.getElementById('academicYearFeedback').style.display = 'block';
        academicYear.classList.add('is-invalid');
        isValid = false;
    }
    
    // Validate branch
    if (!branch.value) {
        document.getElementById('branchFeedback').style.display = 'block';
        branch.classList.add('is-invalid');
        isValid = false;
    }
    
    // Validate fee components
    const feeComponents = document.querySelectorAll('.fee-component');
    if (feeComponents.length === 0) {
        document.getElementById('feeComponentsFeedback').style.display = 'block';
        isValid = false;
    } else {
        for (let i = 0; i < feeComponents.length; i++) {
            const nameInput = feeComponents[i].querySelector('[id^="componentName"]');
            const amountInput = feeComponents[i].querySelector('[id^="componentAmount"]');
            
            if (!nameInput.value) {
                nameInput.classList.add('is-invalid');
                isValid = false;
            }
            
            if (!amountInput.value || parseFloat(amountInput.value) <= 0) {
                amountInput.classList.add('is-invalid');
                isValid = false;
            }
        }
    }
    
    return isValid;
}

/**
 * Initialize fee structure filters
 */
function initFeeStructureFilters() {
    const academicYearFilter = document.getElementById('academicYearFilter');
    const branchFilter = document.getElementById('branchFilter');
    const applyFiltersBtn = document.getElementById('applyFiltersBtn');
    
    if (academicYearFilter && branchFilter && applyFiltersBtn) {
        applyFiltersBtn.addEventListener('click', function() {
            // Show loading state
            applyFiltersBtn.disabled = true;
            applyFiltersBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Applying...';
            
            // Get filter values
            const academicYear = academicYearFilter.value;
            const branch = branchFilter.value;
            
            // Apply filters
            filterFeeStructures(academicYear, branch);
            
            // Reset button state
            setTimeout(function() {
                applyFiltersBtn.disabled = false;
                applyFiltersBtn.innerHTML = '<i class="fas fa-filter me-1"></i> Apply Filters';
            }, 500);
        });
    }
}

/**
 * Filter fee structures based on academic year and branch
 * @param {string} academicYear - Academic year
 * @param {string} branch - Branch
 */
function filterFeeStructures(academicYear, branch) {
    const feeStructureCards = document.querySelectorAll('.fee-structure-card');
    
    feeStructureCards.forEach(card => {
        const cardAcademicYear = card.getAttribute('data-academic-year');
        const cardBranch = card.getAttribute('data-branch');
        
        let showCard = true;
        
        if (academicYear && academicYear !== 'all' && cardAcademicYear !== academicYear) {
            showCard = false;
        }
        
        if (branch && branch !== 'all' && cardBranch !== branch) {
            showCard = false;
        }
        
        card.style.display = showCard ? 'block' : 'none';
    });
    
    // Show message if no results
    const noResultsMessage = document.getElementById('noResultsMessage');
    const visibleCards = document.querySelectorAll('.fee-structure-card[style="display: block"]');
    
    if (noResultsMessage) {
        if (visibleCards.length === 0) {
            noResultsMessage.style.display = 'block';
        } else {
            noResultsMessage.style.display = 'none';
        }
    }
}

/**
 * Initialize fee payment buttons
 */
function initFeePaymentButtons() {
    // Add event listeners to "Pay Now" buttons
    document.querySelectorAll('.btn-pay-fee').forEach(button => {
        button.addEventListener('click', function() {
            const feeType = this.getAttribute('data-fee-type');
            const amount = this.getAttribute('data-amount');
            const branch = this.getAttribute('data-branch');
            
            // Show payment modal
            showPaymentModal(feeType, amount, branch);
        });
    });
}

/**
 * Show payment modal
 * @param {string} feeType - Fee type
 * @param {string} amount - Amount
 * @param {string} branch - Branch
 */
function showPaymentModal(feeType, amount, branch) {
    // Populate modal
    document.getElementById('paymentModalTitle').textContent = `Pay ${feeType}`;
    document.getElementById('paymentModalAmount').textContent = formatCurrency(amount);
    document.getElementById('paymentModalBranch').textContent = branch;
    document.getElementById('paymentFeeType').value = feeType;
    document.getElementById('paymentAmount').value = amount;
    
    // Show modal
    const paymentModal = new bootstrap.Modal(document.getElementById('payFeeModal'));
    paymentModal.show();
}

/**
 * Initialize fee component management
 */
function initFeeComponentManagement() {
    const addComponentBtn = document.getElementById('addComponentBtn');
    const feeComponentsContainer = document.getElementById('feeComponents');
    
    if (addComponentBtn && feeComponentsContainer) {
        // Add component button click handler
        addComponentBtn.addEventListener('click', function() {
            // Get current component count
            const componentCount = feeComponentsContainer.querySelectorAll('.fee-component').length + 1;
            
            // Create new component
            const newComponent = document.createElement('div');
            newComponent.className = 'row mb-3 fee-component';
            newComponent.innerHTML = `
                <div class="col-md-4">
                    <label for="componentName${componentCount}" class="form-label">Component Name</label>
                    <input type="text" class="form-control" id="componentName${componentCount}" placeholder="e.g., Tuition Fee" required>
                </div>
                <div class="col-md-3">
                    <label for="componentAmount${componentCount}" class="form-label">Amount (₹)</label>
                    <input type="number" class="form-control" id="componentAmount${componentCount}" required>
                </div>
                <div class="col-md-3">
                    <label for="componentFrequency${componentCount}" class="form-label">Frequency</label>
                    <select class="form-select" id="componentFrequency${componentCount}" required>
                        <option value="per_semester">Per Semester</option>
                        <option value="per_year">Per Year</option>
                        <option value="one_time">One Time</option>
                    </select>
                </div>
                <div class="col-md-2 d-flex align-items-end">
                    <button type="button" class="btn btn-outline-danger w-100 remove-component-btn">
                        <i class="fas fa-trash"></i>
                    </button>
                </div>
            `;
            
            // Add new component to container
            feeComponentsContainer.appendChild(newComponent);
            
            // Add event listener to remove button
            newComponent.querySelector('.remove-component-btn').addEventListener('click', function() {
                newComponent.remove();
                updateTotalAmount();
            });
            
            // Add event listeners to amount input
            newComponent.querySelector('[id^="componentAmount"]').addEventListener('input', updateTotalAmount);
            
            // Update total amount
            updateTotalAmount();
        });
        
        // Remove component button click handler
        feeComponentsContainer.addEventListener('click', function(event) {
            if (event.target.closest('.remove-component-btn')) {
                event.target.closest('.fee-component').remove();
                updateTotalAmount();
            }
        });
    }
}

/**
 * Initialize payment schedule management
 */
function initPaymentScheduleManagement() {
    const addInstallmentBtn = document.getElementById('addInstallmentBtn');
    const paymentScheduleContainer = document.getElementById('paymentSchedule');
    
    if (addInstallmentBtn && paymentScheduleContainer) {
        // Add installment button click handler
        addInstallmentBtn.addEventListener('click', function() {
            // Get current installment count
            const installmentCount = paymentScheduleContainer.querySelectorAll('.payment-schedule-item').length + 1;
            
            // Create new installment
            const newInstallment = document.createElement('div');
            newInstallment.className = 'row mb-3 payment-schedule-item';
            newInstallment.innerHTML = `
                <div class="col-md-5">
                    <label for="installmentName${installmentCount}" class="form-label">Installment Name</label>
                    <input type="text" class="form-control" id="installmentName${installmentCount}" placeholder="e.g., First Installment" required>
                </div>
                <div class="col-md-3">
                    <label for="installmentAmount${installmentCount}" class="form-label">Amount (₹)</label>
                    <input type="number" class="form-control" id="installmentAmount${installmentCount}" required>
                </div>
                <div class="col-md-3">
                    <label for="installmentDueDate${installmentCount}" class="form-label">Due Date</label>
                    <input type="date" class="form-control" id="installmentDueDate${installmentCount}" required>
                </div>
                <div class="col-md-1 d-flex align-items-end">
                    <button type="button" class="btn btn-outline-danger w-100 remove-installment-btn">
                        <i class="fas fa-trash"></i>
                    </button>
                </div>
            `;
            
            // Add new installment to container
            paymentScheduleContainer.appendChild(newInstallment);
            
            // Add event listener to remove button
            newInstallment.querySelector('.remove-installment-btn').addEventListener('click', function() {
                newInstallment.remove();
            });
        });
        
        // Remove installment button click handler
        paymentScheduleContainer.addEventListener('click', function(event) {
            if (event.target.closest('.remove-installment-btn')) {
                event.target.closest('.payment-schedule-item').remove();
            }
        });
    }
}

/**
 * Update total amount
 */
function updateTotalAmount() {
    const amountInputs = document.querySelectorAll('[id^="componentAmount"]');
    const frequencySelects = document.querySelectorAll('[id^="componentFrequency"]');
    let totalAmount = 0;
    
    for (let i = 0; i < amountInputs.length; i++) {
        const amount = parseFloat(amountInputs[i].value) || 0;
        const frequency = frequencySelects[i].value;
        
        // Calculate annual amount based on frequency
        if (frequency === 'per_semester') {
            totalAmount += amount * 2; // Two semesters per year
        } else if (frequency === 'per_year') {
            totalAmount += amount;
        } else if (frequency === 'one_time') {
            totalAmount += amount;
        }
    }
    
    // Update total amount display
    const totalAmountDisplay = document.getElementById('totalAmount');
    if (totalAmountDisplay) {
        totalAmountDisplay.textContent = formatCurrency(totalAmount);
    }
}

/**
 * Show processing UI
 */
function showProcessing() {
    const submitButton = document.querySelector('#feeStructureForm button[type="submit"]');
    if (submitButton) {
        submitButton.disabled = true;
        submitButton.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Processing...';
    }
}

/**
 * Show success message
 * @param {string} message - Success message
 */
function showSuccess(message) {
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
            <strong class="me-auto">Success</strong>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">
            ${message}
        </div>
    `;
    
    // Add toast to container
    document.getElementById('toastContainer').appendChild(toast);
    
    // Show toast
    const bsToast = new bootstrap.Toast(toast);
    bsToast.show();
    
    // Reset submit button
    const submitButton = document.querySelector('#feeStructureForm button[type="submit"]');
    if (submitButton) {
        submitButton.disabled = false;
        submitButton.innerHTML = 'Create Fee Structure';
    }
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
