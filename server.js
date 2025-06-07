import fetch from "node-fetch";
import express from "express";

const app = express();
const PORT = process.env.PORT || 3000;

const API_URL = "https://script.google.com/macros/s/AKfycbxdCarkggYZJvshEx07ItNVIV2B3zQ4N910AIjWsUyQ_IGCmo51Gceq_uqimJS1C365eA/exec";

app.get("/post/:number", async (req, res) => {
  try {
    const postNumber = parseInt(req.params.number);
    const response = await fetch(API_URL);
    const data = await response.json();

    if (postNumber >= 0 && postNumber < data.length - 1) {
      res.json(data[postNumber + 1]);
    } else {
      res.status(404).json({ error: "投稿が見つかりません" });
    }
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
