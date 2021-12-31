/* eslint-disable */
/// <reference types="cypress" />

// TODO
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
    cy.contains('Successfully submitted a bug report')
  })
  it('feedback form with regular inputs', () => {
    cy.contains('Feedback').click()
    cy.url().should('include', 'feedback')
    cy.get('textarea[id=feedback]').type('Good app!')
    cy.get('button[type=submit]').click()
    cy.contains('Successfully submitted feedback')
  })
  it('search', () => {
    cy.get('input[id=search]').type('saro{enter}')
    cy.url().should('include', 'search/saro')
    cy.contains('Sarosh Thalappil')
  })
  it('register student, login, logout', () => {
    const studentEmail = `automatedstudent${Math.floor(
      Math.random() * 999
    )}@example.com`
    const password = 'automatedpassword'
    cy.contains('register').click()
    cy.contains('Become a student').click()
    cy.get('input[id=firstname]').type('Automated')
    cy.get('input[id=lastname]').type('Student')
    cy.get('input[id=emailaddress]').type(studentEmail)
    cy.get('input[id=password]').type(password)
    cy.get('input[id=confirmpassword]').type(password)
    cy.fixture('png.png').then((fileContent) => {
      cy.get('input[type="file"]').attachFile({
        fileContent: fileContent.toString(),
        fileName: 'png.png',
        mimeType: 'image/png',
      })
    })
    cy.get('input[id=parentemail]').type('automatedparentemail@example.com')
    cy.get('input[id=birthdate]').type('2001-01-31')
    cy.get('input[id=toc]').click()
    cy.get('button[type=submit]').click()
    cy.url().should('include', 'checkemail')
    cy.request(
      `http://127.0.0.1:8000/test/get_register_url_for_user/${studentEmail}`
    ).then((res) => cy.visit(res.body.url))
    cy.url().should('include', 'login')
    cy.get('input[id=email]').type(studentEmail)
    cy.get('input[id=password]').type(password)
    cy.get('button[type=submit]').click()
    cy.contains('Trending') // student homepage shows "Trending"
    cy.get('div[class=name_profile_pic]').click()
    cy.get('a[id=logout]').click()
    cy.contains('Find tutors around the globe')
  })
})
