describe('Testing Home Page', () => {

  it('should have a heading', () => {
    cy.visit('/')
    cy.get('header').should('be.visible')
  })

  it('should have a navbar', () => {
    cy.visit('/')
    cy.get('nav.navbar').should('be.visible')
  })

  it('should route us to the login page', () => {
    // Clicking on the For Business link on the NavBar while logged out
    // Should route to the login page
    cy.visit('/')
    cy.contains('a', 'For Business').click({force:true})
    
    // cy.url().should('include', '/login')
    cy.location('pathname').should('eq', '/login')
  })

  it('should allow us to toggle to Signup', () => {
    // Clicking on the Login link on the NavBar while logged out
    // Should show the Signup form
    cy.visit('/')
    cy.contains('a', 'Login').click({force:true})
    cy.contains('Signup').click()

    cy.get('form:visible').within(() => {
      cy.get('input').should('have.length', 7)
    })
  })
})


// describe('Signup & Login', () => {

//   // !!!!!! This test only fails because the user already exists
//   // !!!!!! Need to research running it in a test db only
//   it('should allow us to signup', () => {
//     // Navigate to Login and toggle to the Signup form
//     // Fill out the Signup form, check the agree box, and submit it
//     cy.visit('/')
//     cy.contains('a', 'Login').click({force:true})
//     cy.contains('Signup').click()

//     cy.get('form:visible').within(() => {
//       cy.get('input').eq(0).type('Vash')
//       cy.get('input').eq(1).type('The Stampede')
//       cy.get('input').eq(2).type('vash@anime.com')
//       cy.get('select').select('US')
//       cy.get('input').eq(3).type('0000000000')
//       cy.get('input').eq(4).type('1234qwer')
//       cy.get('input').eq(5).type('1234qwer')

//       cy.get('input[type="checkbox"]').check()
//       cy.get('button[type="submit"]').should('be.enabled').click()
//     })

//     // User creation should route us to User Dashboard
//     cy.url().should('include', '/user/dashboard')
//   })

//   it('should allow us to login', () => {
//     // Navigate to Login and enter an existing user's information
//     // Submit the Login form
//     cy.visit('/')
//     cy.contains('a', 'Login').click({force:true})

//     cy.get('form:visible').within(() => {
//       cy.get('input').eq(0).type('vash@anime.com')
//       cy.get('input').eq(1).type('1234qwer')

//       cy.get('button[type="submit"]').click()
//     })

//     // Should login the user
//     cy.url().should('not.include', '/login')
//   })

//   it('should allow us to register a business after logging in', () => {
//     // Login and navigate to the For Business page
//     // It should allow us to register a business
//     cy.visit('/')
//     cy.contains('a', 'Login').click({force:true})

//     cy.get('form:visible').within(() => {
//       cy.get('input').eq(0).type('vash@anime.com')
//       cy.get('input').eq(1).type('1234qwer')

//       cy.get('button[type="submit"]').click({force:true})
//     })

//     // Logging in should route us to the user dashboard first
//     cy.url().should('include', '/user/dashboard')

//     // Clicking the link should bring up the business register form
//     cy.contains('a', 'For Business').click({force:true})
//     cy.url().should('include', '/business/register')
//   })
// })