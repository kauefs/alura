// Request & Responses:
import            fs                         from           'fs';
import        GeminiDescription              from './service.js';
import {listAllPosts, creatPost, upDatePost} from   './model.js';
// export async function getPosts(req, res) {const posts = await getPosts()// Function to Get All Posts
//                                     res.status(200).json(posts)};      // HTTP Reply 200 (OK) & JSON Posts
export async function getPosts  (req, res){try{const posts      = await listAllPosts();
                                      res.status(200).json(posts)}
                                              catch(error){  console.error('Error Fetching Posts:', error);
                                      res.status(500).json({         error:'Failed to Fetch Posts!'})}};
export async function Posting   (req, res){    const newPost    =req.body ;
                                           try{const Created    = await creatPost(newPost);
                                      res.status(200).json(Created)}
                                              catch(error){  console.error('Error Creating Post:' , error.message);
                                      res.status(500).jason({        error:'Request Failed!'})}};
export async function upLoadIMG (req, res){    const newPost    ={description:''   ,
                                                                    imgURL:req.file.originalname,
                                                                       alt:''};
                                           try{const Created    = await creatPost(newPost);
                                               const UpDateIMG  =`uploads/${Created.insertedId}.png`
                                               fs.renameSync(    req.file.path, UpDateIMG)
                                      res.status(200).json(Created)}
                                              catch(error){  console.error('Error Creating Post:' , error.message);
                                      res.status(500).jason({        error:'Request Failed!'})}};
export async function PostUpDate(req, res){    const id         =req.params.id;
                                               const urlIMG     =`http://localhost:3000/${id}.png`;
                                             //const postUpDate ={  imgURL:urlIMG,
                                             //                description:req.body.description,
                                             //                        alt:req.body.alt};
                                           try{const imgBuffer  = fs.readFileSync(`uploads/${id}.png`);
                                               const description= await GeminiDescription(imgBuffer);
                                               const postUpDate ={  imgURL:urlIMG,
                                                               description:description,
                                                                       alt:req.body.alt};
                                               const Created    = await upDatePost(id, postUpDate);
                                      res.status(200).json(Created)}
                                              catch(error){  console.error('Error Creating Post:' , error.message);
                                      res.status(500).jason({        error:'Request Failed!'})}};
