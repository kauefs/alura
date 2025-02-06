// Get 'greeting' element reference:
const greetingElement=document.getElementById('greeting');
// Get system actual time:
const currentHour    =new Date().getHours();
// Define Greeting Based on Actual Time:
// if      (currentHour >=  5 && currentHour < 12) {greetingElement.textContent=  'Morning!';}
// else if (currentHour >= 12 && currentHour < 18) {greetingElement.textContent='AfterNoon!';}
// else                                            {greetingElement.textContent=    'Night!';}
// Simpler Way:
const greetingMessage =
    currentHour >= 5 && currentHour < 12
        ? 'Morning!'
        : currentHour >= 12 && currentHour < 18
        ? 'AfertNoon!'
        : 'Night!';
greetingElement.textContent=greetingMessage;
// Intelligent Grid:
const container=document.querySelector('.list-item');
// Element SiZe Change:
const observer =new ResizeObserver(()=>{
    // Element Total Width, Including Content Width & Borders & Filling:
    const containerWidth=container.offsetWidth;
    // Columns Quantity Based on Container Width:
    const numColumns=Math.floor(containerWidth/200);
    // Minimum Width of 200px & Maximum of 1fr (a fraction of the available space):
    container.style.gridTemplateColumns=`repeat(${numColumns}, minmax(13.5rem, 1fr))`;
    console.log({container });
    console.log({numColumns});});
// Observing Element Changes:
observer.observe(container);
