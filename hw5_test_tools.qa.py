from selene import browser, have, be, command


def test_fill_practice_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Новикова')
    browser.element('#lastName').type('Виолетта')
    browser.element('#userEmail').type('violet@example.com')

    browser.element('[for="gender-radio-1"]').click()

    browser.element('#userNumber').type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('July')
    browser.element('.react-datepicker__year-select').type('2002')
    browser.element('.react-datepicker__day--001').click()

    browser.element('#subjectsInput').type('Maths').press_enter()

    browser.element('[for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').set_value(
        str(__file__)
        .replace('test.google_search.py', 'resources\\avatar.png')
    )

    browser.element('#currentAddress').type('ул. Садовая, д. 1')

    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()

    browser.element('#submit').click()

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text('Виолетта Новикова'))
    browser.element('.table').should(have.text('violet@example.com'))
    browser.element('.table').should(have.text('Female'))
    browser.element('.table').should(have.text('1234567890'))