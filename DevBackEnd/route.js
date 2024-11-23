// Importing FrameWork Express for Web Application:
import   express                                  from   'express'      ;
// Importing Multer for File UpLoad:
import    multer                                  from   'multer'       ;
//
import      cors                                  from   'cors'         ;
// Importing Controller Functions for Posting Logic:
import {getPosts, Posting, upLoadIMG, PostUpDate} from './controller.js';
/*
// for WINDOWS
// Multer FileSystem Config:
const storage = multer.diskStorage({destination:function(req, file, cb){cb(null,'uploads/')},           // Specify Directory to Store UpLoaded Files
                                       filename:function(req, file, cb){cb(null, file.originalname)}}) // Keep File Original Name
// MiddleWare Instance:                                       
const upload  = multer({dest:'./uploads', storage})
*/
// MiddleWare Instances:
const   corsOptions   = {origin:'http://localhost:8000',
           optionsSuccessStatus: 200};
const     upload      =  multer({dest:   './uploads'        });
// Routes Using Express:
const          routes = (app) => {app.use(  express.json(   ));      // JSON Requisitions Interpreter
                                  app.use(  cors(corsOptions));     // CORS Options
                                  app.get('/posts'     , getPosts);// Route to Get All Posts
                                                                  // Create Post:
                                  app.post('/posts'    , Posting);
                                                                // Single Image UpLoad:
                                  app.post('/upload'   , upload.single('img'), upLoadIMG);
                                                              // Post UpDate:
                                  app.put('/upload/:id', PostUpDate)
                                                            // General Error Handler:
                                  app.use ((err, req, res, next) => {console.error(err.stack);
                                                      res.status(500).send('SomeThing Went Wrong!')})};
export default routes;
