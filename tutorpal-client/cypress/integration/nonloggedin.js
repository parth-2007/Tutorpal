/* eslint-disable */
/// <reference types="cypress" />

// TODO
// feedback form
// search
//  - rank tutors properly
//  - show correct fields
// registration
//  - tutor
//  - student
//  - test form validation for all fields
// forgot password

describe('TutorPal Test', () => {
  beforeEach(() => {
    // visits homepage before each test
    cy.visit('http://127.0.0.1:3000')
  })
  it('non logged homepage', () => {
    // make sure the non logged in homepage loads properly
    cy.contains('Find tutors around the globe')
  })
  it('bug form with regular inputs', () => {
    // make sure user is able to fill out bug form
    // test regular inputs and for numbers too high/low
    cy.contains('Bugs').click()
    cy.url().should('include', 'bugs')
    cy.get('textarea[name=bugs]').type('Bug form not working')
    cy.get('select[name=buglevel]').select(0) // selects first option
    cy.get('button[type=submit]').click()
  })
})
