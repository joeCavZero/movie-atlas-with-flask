const findButton = document.getElementById('find-button')
const randomButton = document.getElementById('random-button')
const findInput = document.getElementById('find-input')

findButton.addEventListener('click' , _=>{
    window.location.href = '/search/' + findInput.value
    
})

randomButton.addEventListener('click' , _=>{
    window.location.href = '/random'
})