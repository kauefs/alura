const searchInput   =document.getElementById('search');
const resultArtist  =document.getElementById('artist-result');
const resultPlaylist=document.getElementById('playlist-results');
    
function displayResults(result, searchTerm) {
    resultPlaylist.classList.add('hidden');
    const gridContainer = document.querySelector(".grid-container");
    gridContainer.innerHTML = ''; // Limpa os resultados anteriores
    
    const filteredArtists = result.filter((artist) => artist.name.toLowerCase().includes(searchTerm));
    
    filteredArtists.forEach((artist) => {
        const artistCard = document.createElement('div');
        artistCard.classList.add('artist-card');
        artistCard.innerHTML = `
              <div          class='card-img'>
                  <img      class='artist-img' src='${artist.url}' />
                  <div      class='play'>
                      <span class='fa fa-solid fa-play'></span>
                  </div>
              </div>
          <div              class='card-text'>
                  <span     class='artist-name'>${artist.name}</span>
                  <span     class='artist-categorie'>Artist</span>
              </div>
          `;
        gridContainer.appendChild(artistCard);});
    
    resultArtist.classList.remove('hidden');}

function requestAPI(searchTerm) {
    const url = `http://localhost:3000/artists?name_like=${searchTerm}`;
    fetch(url)
        .then((response) => response.json())
        .then((result)   => displayResults(result, searchTerm));}

document.addEventListener('input', function () {
    const searchTerm = searchInput.value.toLowerCase().trim();
    if (searchTerm === '') {
        resultPlaylist.classList.remove('hidden');
        resultArtist  .classList.add   ('hidden');
        return;}
    requestAPI(searchTerm);});
