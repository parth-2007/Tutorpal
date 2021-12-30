/* eslint-disable vue/script-setup-uses-vars */
/// <reference types="cypress" />

describe('TutorPal Test', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000')
  })
  it('non logged in homepage loads', () => {
    cy.contains('Find tutors around the globe')
  })
})
