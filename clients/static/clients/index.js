
// const dateValue = document.querySelector('#start-date')
// const startDate = dateValue.value
//
//
// let renewalDate = addDate(startDate, 1, 0, 1)
// const formattedDate = `${renewalDate.getDate()}/${renewalDate.getMonth() + 1}/${renewalDate.getFullYear()}`;
//
// console.log(formattedDate)

function addDate(date, days, months, years) {
    let newDate = new Date(date)

    newDate.setFullYear(newDate.getFullYear() + years)
    newDate.setMonth(newDate.getMonth() + months)
    newDate.setDate(newDate.getDate() + days)

    return newDate
}

function addRenewalDate() {
    const dateValue = document.querySelector('#start-date')
    // const endDate = document.querySelector('#end-date')
    const startDate = dateValue.value

    let endDate = addDate(startDate, -1, 0, 1)
    let renewalDate = addDate(startDate, 0, 0, 1)
    const formattedDate = formatDate(renewalDate)
    const endDateFormatted = formatDate(endDate)

    console.log(formattedDate, endDateFormatted)
    document.querySelector('#renewal-date').value = formattedDate
    document.querySelector('#end-date').value = endDateFormatted
}

function formatDate(date) {
    const d = new Date(date);
    const year = d.getFullYear();
    const month = String(d.getMonth() + 1).padStart(2, '0'); // Months are zero-based
    const day = String(d.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

document.addEventListener('input', function(e) {
    if (e.target.matches('#start-date')) {
        addRenewalDate()
    }
})

//
// document.querySelector('#renewal-date').value = formattedDate
//
// document.addEventListener('')


