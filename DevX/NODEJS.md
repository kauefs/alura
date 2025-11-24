# 🤖 KnowLedge DataBase Generator Using Gemini

This is a technical documentation detailing the functionality and execution of a **Node.js script** designed to automate the expansion of a technology knowledge base using the Gemini API.

-----

## 📝 Short Description

This script automatically creates and expands a **JSON knowledge base** by adding **25 new, unique entries** about technologies (languages, frameworks, tools, databases, methodologies) on each run. The logic leverages the **Gemini API** for structured content generation and validates/merges the result with the local file, `KnowLedgeDataBase.json`.

-----

## 🎯 Summary of Functionality

  * Generates **exactly 25 new entries** in a predefined JSON format.
  * **Prevents repetition** by excluding names already present in the existing base.
  * Performs **basic response validation** (ensures the response is an array with 25 objects).
  * Implements **exponential backoff retries** in case of API failures.
  * **Updates (overwrites)** the local `KnowLedgeDataBase.json` file with the combined data.

-----

## ⚙️ Prerequisites

  * **Node.js** installed (v16+ recommended).
  * A **Gemini API Key**.

-----

## 🚀 How to Execute (Summary)

1.  **Install dependencies:**

    ```javascript
    npm install
    ```

2.  **Create a `.env` file** in the project root with your key:

    ```javascript
    GEMINI_API_KEY="YOUR_KEY_HERE"
    ```

3.  **Execute the script:**

    ```javascript
    npm start
    ```

-----

## 🖥️ What to Expect

  * Upon completion, the **`KnowLedgeDataBase.json`** file will be updated with the old entries plus the 25 newly generated ones.
  * **Console logs** will report success, the final number of items, and any potential errors.

-----

## 🔧 Where to Adjust Behavior

  * To change the quantity generated, edit the constant **`TOTAL_ITEMS`** in `generator.js`.
  * The function responsible for generation is **`generateNewKnowledge`** in `generator.js`.
  * The main execution flow is in the **`main`** function in `generator.js`.

-----

## 📁 Key Files

  * [`generator.js`](generator.js): main script that calls the API and updates the base.
  * [`KnowLedgeDataBase.json`](KnowLedgeDataBase.json): data file that will be updated.
  * [`package.json`](https://www.google.com/search?q=package.json): project configuration and the start script definition.
  * Create **`.env`** in the root with the `GEMINI_API_KEY` variable.

-----

## ⚠️ Quick Warnings

  * The **`KnowLedgeDataBase.json`** file will be **overwritten** at the end of the process.
  * Check **Gemini API limits & costs** before running the script at scale.
