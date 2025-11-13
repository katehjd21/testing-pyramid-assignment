describe('Display Duties', () => {
  it('It displays a duty called Random Duty', () => {
    cy.visit('/')
    cy.contains('Random Duty')
  })
})