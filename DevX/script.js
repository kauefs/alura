let cardContainer=document.querySelector('.card-container');
let searchField  =document.querySelector('header input');
let data=[ ];
// Function to handle initial data fetching and subsequent search operations
async function startSearch( ) {
    // If data hasn't been loaded yet, fetch it from the JSON file.
    if (data.length == 0) {
        try {let response = await fetch('data.json');
            data = await response.json( );
        } catch (error) {console.error('Failed to fetch data:', error);
            return;}} // Stops execution if there's an error
    // Get the search term and convert it to lower case for case-insensitive search
    const searchTerm  =searchField.value.toLowerCase( );
    // Filter the data based on the search term matching the 'name' or 'description'
    const filteredData=data.filter(item => 
        item.name.toLowerCase( ).includes(searchTerm) || 
        item.description.toLowerCase( ).includes(searchTerm));
    renderCards(filteredData);}
// Function to dynamically create and display the cards
function renderCards(data) {
    cardContainer.innerHTML=''; // Clears existing cards before rendering new ones    
    // Loop through the filtered data and create an 'article' element for each item
    for (let item of data) {
        let article = document.createElement('article');
        article.classList.add('card');
        // Populate the card's inner HTML with data properties
        article.innerHTML=`
        <h2>${item.name}</h2>
        <p>${item.date}</p>
        <p>${item.description}</p>
        <a href="${item.link}" target='_blank'>Learn more</a>
        `
        cardContainer.appendChild(article);}}
