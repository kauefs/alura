import {MongoClient} from 'mongodb';
export default async function dbConnect(connect) {let mongoClient;
    try {mongoClient=  new  MongoClient(connect);
         console.log('DataBase Cluster Connection…');
         await mongoClient.connect();
         console.log('MongoDB  Atlas   Connected!' );
         return mongoClient;}
    catch (err) {console.error('Connection Error!', err);
                 process.exit();}};
