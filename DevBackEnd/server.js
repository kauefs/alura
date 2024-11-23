import express from    'express'  ;
import  routes from './route.js'  ;
const     app =         express( );
app.use(express.static('uploads'));
routes(   app);
// Starting Server on Port 3000 & DisPlaying Message:
app.listen(3000, (             ) => {console.log('Server    Ready !')});
// app.get('/index' , (req, res) => {res.status(200).send(  'Welcome!')});
// Error Handler:
app.use((error , req, res, next) => {console.error(error.stack);
                     res.status(500).send(   'SomeThing Went Wrong!')});
