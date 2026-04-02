document.addEventListener('DOMContentLoaded',( )=>{
	const perfilLinks   =document.querySelectorAll('.ProFile');
	perfilLinks.forEach(link=>{
		link.addEventListener('click',(event)=>{
			// Find Name & Image InSide Selected ProFile
			const item  =link.closest('.ProFileItem');
			if(!item)return;
			const nomeEl=item.querySelector('.ProFileName');
			const imgEl =item.querySelector('img');
			const nome  =nomeEl ?  nomeEl.textContent.trim( ):'';
			let imgSrc  = imgEl ?   imgEl.getAttribute('src'):'';
            // Adjust relative path to catalogue.html
            // Prefix '../' pointing to root
			if (imgSrc&&!imgSrc.startsWith('http')&&!imgSrc.startsWith('/')&&!imgSrc.startsWith('..')){imgSrc='../'+imgSrc;}
			try {
				localStorage.setItem('ActiveProFileName' ,   nome);
				localStorage.setItem('ActiveProFileImage', imgSrc);
			} catch (e) {
				// Silence localStorage errors (ex: private mode)
				console.warn('Saving Active ProFile to localStorage not possible', e);
			}
			// Link goes to catalogue.html
		});
	});
