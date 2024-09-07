// console.log(data)
// function search() {console.log('click')};
function search() {
    // Get HTML section where results will be shown:
    let section      = document.getElementById('results');
    let term         = document.getElementById('search').value.toLowerCase();
    // Checking for empty search term:
    if (!term) {section.innerHTML = '<p>Enter search term.</p>';
                       return;}
    // Start with empty results string:
    let results      = '';
    // Iterate over each painting in the data list:
    for (let item of data) {
        title        = item.title.toLowerCase()
        description  = item.description.toLowerCase()
        symbolism    = item.symbolism.toLowerCase()
        tags         = item.tags.toLowerCase()
        // Check if search term is found in title, description, or symbolism (case-insensitive)
        if (title.includes(term) || description.includes(term) || symbolism.includes(term) || tags.includes(term)) {
            // creating new result element:
            results += `
                <div class='item'>
                    <h2><a href=${item.link} target='_blank'>${item.title}</a></h2>
                    <p class='description'>${item.year}</p>
                    <p class='description'>${item.technique}</p>
                    <p class='description'>${item.size}</p>
                    <p class='description'>${item.description}</p>
                    <p class='description'>${item.museum}</p>
                    <p class='description'>${item.acquisitionDate}</p>
                    <p class='description'>${item.exhibitions}</p>
                    <p class='description'>${item.restorations}</p>
                    <p class='description'>${item.symbolism}</p>
                    <a href=${item.image} target='_blank'>Image</a>
                </div>
            `;
        }
    }
    // Display results to HTML section:
    section.innerHTML = results || '<p>Nothing found!</p>';
};
