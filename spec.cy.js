Cypress.on('uncaught:exception', (err, runnable) => {
    return false;
  });
it('my first test', () => {
    cy.visit('https://www.automationexercise.com/')
    cy.get('.shop-menu > .nav > :nth-child(3) > a').click()
    cy.get('u').click()
    cy.get(':nth-child(1) > .panel-heading > .panel-title > a').click()
    cy.get('.panel-body > ul > :nth-child(3) > a').click()
    cy.get(':nth-child(3) > .product-image-wrapper > .single-products > .productinfo > .btn').click({force: true})
    cy.get('.modal-footer > .btn').click()
    cy.get('.shop-menu > .nav > :nth-child(3) > a').should('be.visible').click()
    cy.get('h4 > a').should('have.text','Cotton Silk Hand Block Print Saree')
    cy.get('.cart_quantity_delete').click()
})

// it.only('cart assestions', () => {
//     cy.visit('https://www.automationexercise.com/view_cart')
// })