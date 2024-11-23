import                   'dotenv/config';
import { ObjectId } from    'mongodb'   ;
import   dbConnect  from './dbConfig.js';
// Connect to DataBase Using EnvironMent Variable:
const  connect = await dbConnect(process.env.CONNECTION);
// Async Function to  Get All   Posts from DataBase:
                                 // Select DataBase & Collection:
export async function listAllPosts(         ){try{const db        =connect.db(    'instabyte');           // Select Desired DataBase
                                                  const collection=     db.collection('posts');          // Select Desired Collection on DataBase
                                 // Fetch & Return All Posts:
                                                  const posts     =  await collection.find().toArray();// Return Array with All Documents in Collection
                                              return    posts}
                                              catch(error){console.error('Error Fetching Posts:', error);
                                 // Re-Throw Error to Handle It @ Higher Level:
                                              throw error}};
// Async Function to Creat  New Posts on DataBase:
export async function creatPost(     newPost){try{const db        =connect.db(    'instabyte');
                                                  const collection=     db.collection('posts');
                                                  const newpost   =  await collection.insertOne (newPost);
                                              return    newpost}
                                              catch(error){console.error('Error Creating Post:' , error);
                                              throw error}};
// Async Function to  UpDate    Posts on DataBase:
export async function upDatePost(id, newPost){try{const db        =connect.db(    'instabyte');
                                                  const collection=     db.collection('posts');
                                                  const objID     = ObjectId.createFromHexString(id);
                                                  const updatepost= await collection.updateOne ({_id:new ObjectId(objID)},{$set:newPost});
                                              return    updatepost}
                                              catch(error){console.error('Error UpDating Post:' , error);
                                              throw error}};
export    default    {listAllPosts, creatPost, upDatePost };
