// JavaScript for adding Pay Now buttons to fee structure cards

document.addEventListener('DOMContentLoaded', function() {
    // Add Pay Now buttons to all fee structure cards
    addPayNowButtons();
});

/**
 * Add Pay Now buttons to all fee structure cards
 */
function addPayNowButtons() {
    // Get all fee structure cards
    const feeStructureCards = document.querySelectorAll('.card-footer');
    
    // Add Pay Now button to each card
    feeStructureCards.forEach((cardFooter, index) => {
        // Get fee type and amount from the card
        const card = cardFooter.closest('.card');
        const feeType = card.querySelector('.card-header h5').textContent.trim();
        const totalAmount = card.querySelector('.table-primary td:nth-child(2) strong').textContent.trim().replace(/[^\d]/g, '');
        
        // Create Pay Now button
        const payNowButton = document.createElement('button');
        payNowButton.className = 'btn btn-success btn-sm btn-pay-fee';
        payNowButton.innerHTML = '<i class="fas fa-money-bill-wave me-1"></i> Pay Now';
        payNowButton.setAttribute('data-fee-type', feeType);
        payNowButton.setAttribute('data-amount', totalAmount);
        payNowButton.setAttribute('data-branch', feeType);
        
        // Add event listener to Pay Now button
        payNowButton.addEventListener('click', function() {
            // Show payment modal
            showPaymentModal(feeType, totalAmount, feeType);
        });
        
        // Create container for button
        const buttonContainer = document.createElement('div');
        buttonContainer.className = 'd-flex justify-content-between align-items-center';
        
        // Move existing buttons to container
        const existingButtons = cardFooter.querySelector('.btn-group');
        buttonContainer.appendChild(existingButtons);
        
        // Add Pay Now button to container
        buttonContainer.appendChild(payNowButton);
        
        // Clear card footer and add container
        cardFooter.innerHTML = '';
        cardFooter.appendChild(buttonContainer);
    });
}

/**
 * Show payment modal
 * @param {string} feeType - Fee type
 * @param {string} amount - Amount
 * @param {string} branch - Branch
 */
function showPaymentModal(feeType, amount, branch) {
    // Format amount with commas
    const formattedAmount = new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR',
        maximumFractionDigits: 0
    }).format(amount);
    
    // Populate modal
    document.getElementById('paymentModalTitle').textContent = `Pay ${feeType}`;
    document.getElementById('paymentModalBranch').textContent = branch;
    document.getElementById('paymentModalAmount').textContent = formattedAmount;
    document.getElementById('paymentFeeType').value = feeType;
    document.getElementById('paymentAmount').value = amount;
    
    // Show modal
    const paymentModal = new bootstrap.Modal(document.getElementById('payFeeModal'));
    paymentModal.show();
}
