function search() {
    // Get HTML section where results will be shown:
    let section     = document.getElementById('results');
    let searchField = document.getElementById('search-field').value
    // if searchField is empty:
    if (!searchField) {section.innerHTML = '<p>Nothing found, try another paiting.</p>'
                       return}
    searchField = searchField.toLowerCase()
    // Start empty fields to store results:
    let results     = '';
    let titulo      = ''; 
    let descricao   = '';
    let tags        = '';
    // Iterate over every item on the data list:
    for (let item of data) {
        title       = item.title.toLowerCase()
        description = item.description.toLowerCase()
        symbolism   = item.symbolism.toLowerCase()
        // including every element in searchField:
        if (title.includes(searchField) || description.includes(searchField) || symbolism.includes(searchField)) {
            // creating new element:
            results += `
            <div class='item-results'>
                <h2>
                    <a href='#' target='_blank'>${item.title}</a>
                </h2>
                <p class='descricao-meta'>${item.description}</p>
                <a href=${item.link} target='_blank'>More information</a>
            </div>
        `;
        }
    }
    if (!results) {results = '<p>Nothing found!</p>'}
    // Display results to HTML section:
    section.innerHTML = results;
};
