import { GoogleGenerativeAI } from '@google/generative-ai';
const genAI = new GoogleGenerativeAI(process.env.API_KEY);
const model =  genAI.getGenerativeModel({ model:'gemini-1.5-flash'});
export default async function GeminiDescription(imageBuffer){const prompt='description to the following image in no more than five words';
    try {const image={inlineData:{data:imageBuffer.toString('base64'), mimeType:'image/png'}};
         const   res=await model.generateContent([prompt, image]);
    return       res.response.text() ||             'Alt-Text Description Not Available.'}
    catch    (error){console.error('Error Generating Alt-Text Description:', error.message, error);
    throw new Error(               'Error Generating Alt-Text Description from Gemini.')}}
