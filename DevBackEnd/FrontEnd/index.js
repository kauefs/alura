import fetchImages from './fetchAPI.js';
const modal        = document.getElementById('modal')    ;
const modalImg     = document.getElementById('modal-img');
const captionText  = document.getElementById('caption')  ;
const closeBtn     = document.querySelector('.close')    ;
modal.style.display='none';
const imageGrid = document.querySelector('.image-grid');
// Search & DisPlay EndPoint Data:
async function displayImages(){const data = await fetchImages();
    try {const postsList = data.map(item => {return `
        <article data-description='${item.description}'>
            <figure>
                <img src='${item.imgURL}' alt='${item.alt}'/>
            </figure>
        </article>
        `}).join('');
        imageGrid.insertAdjacentHTML('beforeend', postsList)
        // Add Click Events for Each Image:
        addImageClickEvents()}
        catch (error) {console.error('Error Populating Page.', error)}}
// Add Click Events to Images:
function addImageClickEvents() {const images = document.querySelectorAll('.image-grid img');
    images.forEach(img => {img.addEventListener('click', function(){
                                captionText.textContent='';
                                modal.style.display    ='block';
                                modalImg.src           = this.src;
                                const article          = this.closest('article');
                                const description      = article ? article.dataset.description:'';
                                const caption          = description || this.alt;
                                captionText.innerHTML  =`<p>${caption}</p>`})})}
// Close Modal Event:
closeBtn.addEventListener('click', function( ) {modal.style.display = 'none'});
// Close Modal Clicking OutSide of It:
window.addEventListener(  'click', function(event){if(event.target === modal){modal.style.display='none'}});
// Call Search & DisPlay Function When Loading Page:
document.addEventListener('DOMContentLoaded', displayImages);
